#!/bin/bash



# 1. Create list of currently active contributors

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
    git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//' >> ../names.list
    cd ..
}

# Repositories to process
repos=(
    "https://github.com/oscar-system/Oscar.jl"
    "https://github.com/thofma/hecke.jl"
    "https://github.com/Nemocas/Nemo.jl"
    "https://github.com/Nemocas/AbstractAlgebra.jl"
    "https://github.com/oscar-system/GAP.jl"
    "https://github.com/oscar-system/Polymake.jl"
    "https://github.com/oscar-system/Singular.jl"
)

# Clear the names.list before starting
> names.list

# Process each repository
for repo in "${repos[@]}"; do
    process_repo "$repo"
done

# Process and create contributor list
echo -e "\n---------------------------------------------------------------"
echo -e "Processing and creating contributor list...\n"

# Initialize the output file
> names-processed.list

# Process the names
while IFS= read -r line; do
    case "$line" in
        "Simon Brandhorst"|"Wolfram Decker"|"Claus Fieker"|"Tommy Hofmann"|"Max Horn"|"Michael Joswig")
            continue ;;
        "JohnAAbbott") echo "John Abbott" >> "names-processed.list" ;;
        "emikelsons"|"Miķelis Emīls Miķelsons") echo "Mikelis Emils Mikelsons" >> "names-processed.list" ;;
        "ThomasBreuer") echo "Thomas Breuer" >> "names-processed.list" ;;
        "YueRen") echo "Yue Ren" >> "names-processed.list" ;;
        "Alex J Best") echo "Alex J. Best" >> "names-processed.list" ;;
        "Andrew P Turner") echo "Andrew P. Turner" >> "names-processed.list" ;;
        "BjSchaefer") echo "Bjoern Schaefer" >> "names-processed.list" ;;
        "Benjamin Schroeter") echo "Benjamin Schröter" >> "names-processed.list" ;;
        "Hans Schoenemann") echo "Hans Schönemann" >> "names-processed.list" ;;
        "Janko Boehm") echo "Janko Böhm" >> "names-processed.list" ;;
        "Lukas Kuehne") echo "Lukas Kühne" >> "names-processed.list" ;;
        "nanleij") echo "Nando Leijenhorst" >> "names-processed.list" ;;
        "Sreevatsa2k") echo "Sreevatsa Sasisekar" >> "names-processed.list" ;;
        "Nicolas") echo "Nicolas Faross" >> "names-processed.list" ;;
        *) echo "$line" >> "names-processed.list" ;;
    esac
done < "names.list"

# Sort contributors by last name
sort -u names-processed.list > contributors-by-first-name.sorted
awk '{print $NF, $0}' contributors-by-first-name.sorted | sort -k1,1 | cut -d' ' -f2- > currently-active-contributors

# Clean up
rm names.list names-processed.list contributors-by-first-name.sorted




# 2. Fetch contributors from the OSCAR website
echo -e "\n---------------------------------------------------------------"
echo -e "Fetching current contributor list from the OSCAR website...\n"

curl -o contributors.md https://raw.githubusercontent.com/oscar-system/oscar-website/gh-pages/contributors.md

# Process active and retired contributors
awk '/contributors:/ {inside_section=1; next} /# Retired contributors/ {inside_section=0} inside_section' contributors.md > temp-active-contributors.md
awk '/retired:/ {inside_section=1; next} inside_section' contributors.md > temp-retired-contributors.md

# Extract and clean active contributors
grep "^  - name:" temp-active-contributors.md | sed 's/^  - name: //' | sed 's/#.*//' | sed 's/[[:space:]]*$//' > active-contributors-OSCAR-website
grep "^  - name:" temp-retired-contributors.md | sed 's/^  - name: //' | sed 's/#.*//' | sed 's/[[:space:]]*$//' > retired-contributors-OSCAR-website

rm contributors.md temp-active-contributors.md temp-retired-contributors.md




# 3. Identify newly active, newly retired contributors, and previously retired but active again contributors
echo -e "\n---------------------------------------------------------------"
echo -e "Identifying contributors...\n"

# Task 1: Previously retired but active again
grep -Fx -f currently-active-contributors retired-contributors-OSCAR-website > previously-retired-but-again-active-contributors

# Task 2: New retired contributors
grep -Fxv -f currently-active-contributors active-contributors-OSCAR-website > new-retired-contributors

# Task 3: New active contributors
grep -Fxv -f active-contributors-OSCAR-website currently-active-contributors | grep -Fxv -f retired-contributors-OSCAR-website > new-active-contributors

# Clean up unused files
rm active-contributors-OSCAR-website retired-contributors-OSCAR-website currently-active-contributors




# 4. GitHub profile lookup for new active contributors
echo -e "\n---------------------------------------------------------------"
echo -e "Looking up GitHub profiles for new active contributors...\n"

updated_contributors=""
while IFS= read -r contributor; do
    search_url="https://api.github.com/search/users?q=${contributor// /+}"
    user_data=$(curl -s "$search_url")
    user_url=$(echo "$user_data" | jq -r '.items[0].html_url // "Not Found"')

    if [[ $user_url != "Not Found" ]]; then
        updated_contributors+="$contributor: $user_url\n"
    else
        updated_contributors+="$contributor: No GitHub profile found.\n"
    fi
done < new-active-contributors
updated_contributors=$(echo -e "$updated_contributors" | sed '$ d') # Remove unnecessary trailing line at the end of file
echo -e "$updated_contributors" > new-active-contributors




# 5. Summary report
echo -e "\n---------------------------------------------------------------"
echo -e "Summary of contributors:\n"

# Count contributors
new_active_count=$(wc -l < new-active-contributors)
new_retired_count=$(wc -l < new-retired-contributors)
prev_retired_active_count=$(wc -l < previously-retired-but-again-active-contributors)

echo "Found $new_active_count new active contributors."
echo "Found $new_retired_count contributors who are now retired."
echo "Found $prev_retired_active_count previously retired contributors who are now active again."

# List some details (optional)
echo -e "\nNew Active Contributors:"
head -n 4 new-active-contributors

echo -e "\nNew Retired Contributors:"
head -n 4 new-retired-contributors

echo -e "\nPreviously Retired but Active Contributors:"
head -n 4 previously-retired-but-again-active-contributors

echo -e "\n---------------------------------------------------------------"
