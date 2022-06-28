# Technical info about the web server setup

This document describes how the OSCAR website hosting is set up, to help
people who need to troubleshoot it or migrate it to a new host.

## Required software on the server

To ensure the required software is installed on the server, run this
(assuming a Debian or Ubuntu based environment):

    apt install git bundler


## Where it is

The server can be reached via SSH:

    ssh oscar.computeralgebra.de

There is a dedicated user `oscar-www` who owns a clone of the oscar-website
repository at

    /home/oscar-www/oscar-website

This clone is owned by use `oscar-www` and group `oscar-www`. If anything goes
wrong with these permissions, they can be fixed via

    chown -R oscar-www:oscar-www /home/oscar-www/oscar-website

## Automatic updates via webhook

Whenever a change is pushed to the master branch of the oscar-website
repository, GitHub activates a webhook we provide via `webhook.php` at
<https://oscar.computeralgebra.de/webhook.php>.

The crucial bit is at the end of this .php file, where an empty file
`/home/oscar-www/oscar-website.trigger` is created. This is detected by a
systemd unit `/etc/systemd/system/oscar-website.path` (a copy of this file is
in the `etc` directory of the oscar-website repo).

This then triggers `/etc/systemd/system/oscar-website.service`
(a copy of this file is in the `etc` directory of the oscar-website repo).

This finally executes `etc/update.sh`, which runs jekyll.


For authentication, we set a secret token in `/etc/apache2/sites-enabled/oscar.conf`
which looks like this:

    SetEnv GITHUB_WEBHOOK_SECRET "MY_SECRET"

with the actual secret key taking the place of `MY_SECRET`. The same value
must be entered in the GitHub settings at
<https://github.com/oscar-system/oscar-website/settings/hooks>.


## Troubleshooting

The following assumes you are logged in as root (resp. used `sudo` to become root)
on the webserver.

If updates stop working, a good first place to look at is this output of this:

    systemctl status oscar-website.service

This prints a log with extra info. However, it might also say "service not
found". In that case, make sure that `oscar-website.service` and
`oscar-website.path` are installed and enabled:

    cp /home/oscar-www/oscar-website/etc/oscar-website.* /etc/systemd/system/
    systemctl enable oscar-website.service oscar-website.path

Also helpful is to study the log for the relevant systemd units

    journalctl -f -u oscar-website.*

A problem that sometimes happens (e.g. if one directly pokes into the git
clone) are broken file permissions which can impede further operations, such
as git pulling updates or jekyll updating the website. To fix these, run the
following as root:

    chown -R oscar-www:oscar-www /home/oscar-www/oscar-website
    chown -R oscar-www:oscar-www /var/www/oscar-website
    chmod 0664 /home/oscar-www/oscar-website.trigger


## Initial setup / what if the server VM is upgraded

### Requirements

- Ubuntu or Debian VM
- Apache 2 (`apt install apache2`)
- Ruby 2.7 or newer, including development headers (`apt-get install ruby-dev`)
- PHP (only for the webhook) (`apt install libapache2-mod-php ; a2enmod php7.4`)
- Jekyll (installed via `gem` and `bundler`, see below)


## Further steps as `root`

1. Set up a user `oscar-www` in group `oscar-www`

2. Set up an Apache2 site with data in `/var/www/oscar-website/` (or modify the units
   here for alternate locations); ensure `oscar` owns it, i.e.

        chown -R oscar-www:oscar-www /var/www/oscar-website

   In the config for that site, make sure to set `GITHUB_WEBHOOK_SECRET` as described
   elsewhere in this file, and enable PHP.
   Of course also set up SSL/TLS and a scheme to update the certificates.

3. In the `oscar` home directory add a clone of the `oscar-website` git repository, i.e.,
   in `/home/oscar-www/oscar-website` (otherwise adjust `oscar-website.service`). Also do

        touch /home/oscar-www/oscar-website.trigger
        chmod 0664 /home/oscar-www/oscar-website.trigger

4. Install the systemd units

        cp /home/oscar-www/oscar-website/etc/oscar-website.* /etc/systemd/system/
        systemctl enable oscar-website.service oscar-website.path


## Further steps as `oscar-www`

As `oscar-www:oscar-www`  (`sudo -u oscar-www -g oscar-www bash`):
To ensure all the relevant ruby gems are installed, do this:
```
cd /home/oscar-www/oscar-website
bundle config set --local path 'vendor/bundle'
bundle install
```


## On GitHub

Go to <https://github.com/oscar-system/oscar-website/settings/hooks> and
make sure the webhook there is setup right:

 - Payload URL: <https://oscar.computeralgebra.de/webhook.php>
 - Content-type: `application/x-www-form-urlencoded` (TODO: switch to JSON at some point?)
 - Secret should of course match `GITHUB_WEBHOOK_SECRET` used elsewhere
 - enable SSL validation
 - trigger: "just the push event"
