# 1. Create list of currently active contributors with GitHub nicks, but process only one commit per contributor

# Function to fetch or clone and process repository
process_repo() {
    local REPO=$1
    local DIRNAME=$(echo $REPO | sed 's/.*\///')

    echo -e "\n---------------------------------------------------------------"
    echo -e "Processing $DIRNAME...\n"

    if [ -d $DIRNAME ]; then
        cd $DIRNAME
        git fetch --all
        git pull
        cd ..
    else
        git clone "$REPO"
    fi

    cd $DIRNAME

    # Step 1: Get a list of unique contributors (author name + email) from the last year
    git log --since="1 year ago" --format='%aN <%aE>' | sort | uniq > ../contributors.list

    # Step 2: For each contributor, find one commit and process it
    while IFS= read -r contributor; do
        author_name=$(echo "$contributor" | sed 's/ <.*//')  # Extract the author's name
        author_email=$(echo "$contributor" | sed 's/.*<\(.*\)>/\1/')  # Extract the author's email

        # Get one commit by this author
        commit_hash=$(git log --since="1 year ago" --author="$author_email" --format='%H' | head -n 1)

        # Extract GitHub username from commit URL if possible
        github_commit_url="https://github.com/${REPO#*github.com/}/commit/$commit_hash"

        # Scrape GitHub commit page for username using curl and parse HTML
        github_nick=$(curl -s "$github_commit_url" | sed -n 's/.*<a[^>]*class="commit-author user-mention"[^>]*href="\/\([^"]*\).*/\1/p' | head -n 1)

        # Ensure we only extract the username, not the whole commit URL
        github_username=$(echo "$github_nick" | sed 's/.*author=//')

        # Append to list: Name and GitHub hyperlink if available
        if [ -n "$github_username" ]; then
            echo "$author_name (https://github.com/$github_username)" >> ../names.list
        else
            echo "$author_name" >> ../names.list
        fi

    done < ../contributors.list

    echo -e "\nFinished processing $DIRNAME.\n"
    cd ..
}

# Repositories to process
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
