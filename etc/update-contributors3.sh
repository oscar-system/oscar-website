#!/bin/bash

# Function to fetch or clone and process repository
process_repo() {
    local REPO=$1
    local DIRNAME=$(echo $REPO | sed 's/.*\///')

    echo -e "\n---------------------------------------------------------------"
    echo -e "Processing $DIRNAME...\n"

    # Clone or pull the repository
    if [ -d "$DIRNAME" ]; then
        cd "$DIRNAME"
        git fetch --all
        git pull
        cd ..
    else
        git clone "$REPO"
    fi

    cd "$DIRNAME"

    # Step 1: Get a list of unique contributors (name + email) from the last year
    git log --since="1 year ago" --format='%aN <%aE>' | sort -u -r > ../contributors.list

    # Step 2: For each contributor, find one commit and process it
    while IFS= read -r contributor; do
        author_name=$(echo "$contributor" | sed 's/ <.*//')  # Extract the author's name
        author_email=$(echo "$contributor" | sed 's/.*<\(.*\)>/\1/')  # Extract the author's email

        # Get one commit by this author
        commit_hash=$(git log --author="$author_email" --format='%H' | head -n 1)

        # If a commit was found for the author, proceed
        if [ -n "$commit_hash" ]; then
            github_commit_url="https://github.com/${REPO#*github.com/}/commit/$commit_hash"

            # Scrape GitHub commit page for the username using curl
            #github_nick=$(curl -s "$github_commit_url" | sed -n 's/.*<a[^>]*class="commit-author user-mention"[^>]*href="\/\([^"]*\).*/\1/p' | head -n 1 | sed 's/^.*=//' )
            #github_nick=$(curl -s "$github_commit_url" | grep "authors" | head -n 1 | sed 's/^.*authors":\[{"login":"//' | sed 's/","displayName".*$//')
            github_nick=$(curl -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" -s "$github_commit_url" | grep "authors" | head -n 1 | sed 's/^.*authors":\[{"login":"//' | sed 's/","displayName".*$//')

            echo "commit url: $github_commit_url"
            echo "author name: $author_name"
            echo "author email: $author_email"
            echo "github_nick: $github_nick"
            echo "-------------------------"

            # Step 3: Write the display name and GitHub username to the output list
            if [ -n "$github_nick" ]; then
                # If GitHub nickname was found, create a link to the profile
                echo "$author_name (https://github.com/$github_nick)" >> ../names.list
            else
                # If no GitHub nickname was found, write the author's name without the link
                echo "$author_name (No GitHub username found)" >> ../names.list
            fi
        else
            echo "$author_name (No commits found)" >> ../names.list
        fi

    done < ../contributors.list

    cd ..
}

# List of repositories to process
repos=(
    "https://github.com/oscar-system/Oscar.jl"
    #"https://github.com/thofma/hecke.jl"
    #"https://github.com/Nemocas/Nemo.jl"
    #"https://github.com/Nemocas/AbstractAlgebra.jl"
    #"https://github.com/oscar-system/GAP.jl"
    #"https://github.com/oscar-system/Polymake.jl"
    #"https://github.com/oscar-system/Singular.jl"
)

# Clear the names.list before starting
> names.list

# Process each repository
for repo in "${repos[@]}"; do
    process_repo "$repo"
done

# Filter duplicates from names.list (if contributors exist in multiple repositories)
awk '!seen[$0]++' names.list > names.unique.list
mv names.unique.list names.list

echo -e "\nProcess completed! The list of contributors is saved in 'names.list'."
