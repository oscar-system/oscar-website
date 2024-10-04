#!/bin/bash


# 1. Oscar.jl

echo -e "---------------------------------------------------------------"
echo -e "1. OSCAR.jl...\n"
REPO="https://github.com/oscar-system/Oscar.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  > ../names.list
cd ..


# 2. Hecke.jl

echo -e "\n---------------------------------------------------------------"
echo -e "2. Hecke.jl...\n"
REPO="https://github.com/thofma/hecke.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  >> ../names.list
cd ..


# 3. Nemo.jl

echo -e "\n---------------------------------------------------------------"
echo -e "3. Nemo.jl...\n"
REPO="https://github.com/Nemocas/Nemo.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  >> ../names.list
cd ..


# 4. AbstractAlgebra.jl

echo -e "\n---------------------------------------------------------------"
echo -e "4. AbstractAlgebra.jl...\n"
REPO="https://github.com/Nemocas/AbstractAlgebra.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  >> ../names.list
cd ..


# 5. GAP.jl

echo -e "\n---------------------------------------------------------------"
echo -e "5. GAP.jl...\n"
REPO="https://github.com/oscar-system/GAP.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  >> ../names.list
cd ..


# 6. Polymake.jl

echo -e "\n---------------------------------------------------------------"
echo -e "6. Polymake.jl...\n"
REPO="https://github.com/oscar-system/Polymake.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  >> ../names.list
cd ..


# 7. Singular.jl

echo -e "\n---------------------------------------------------------------"
echo -e "7. Singular.jl...\n"
REPO="https://github.com/oscar-system/Singular.jl"
DIRNAME=$(echo $REPO | sed 's/.*\///')
if [ -d $DIRNAME ]; then
    cd $DIRNAME
    git fetch --all ; git pull
    cd ..
else
    git clone "$REPO"
fi
cd $DIRNAME
git shortlog -s --since="1 year ago" | sed 's/^\s*[0-9]*\s*//'  >> ../names.list
cd ..


# 8. Sort contributors

echo -e "\n---------------------------------------------------------------"
echo -e "8. Process information and create contributor list...\n"

# Initialize (clear) the output file
> "names-processed.list"

# Read the input file line by line
while IFS= read -r line
do
    # Check if the line matches a case, then proceed (e.g. skip PIs, remove duplicate ALIAS, change cryptic ALIAS to proper name as far as known
    case "$line" in
        "Simon Brandhorst"|"Wolfram Decker"|"Claus Fieker"|"Tommy Hofmann"|"Max Horn"|"Michael Joswig")
            continue ;;
        "JohnAAbbott")
            echo "John Abbott" >> "names-processed.list" ;;
        "emikelsons")
            echo "Mikelis Emils Mikelsons" >> "names-processed.list" ;;
        "Miķelis Emīls Miķelsons")
            echo "Mikelis Emils Mikelsons" >> "names-processed.list" ;;
        "ThomasBreuer")
            echo "Thomas Breuer" >> "names-processed.list" ;;
        "YueRen")
            echo "Yue Ren" >> "names-processed.list" ;;
        "Alex J Best")
            echo "Alex J. Best" >> "names-processed.list" ;;
        "Andrew P Turner")
            echo "Andrew P. Turner" >> "names-processed.list" ;;
        "BjSchaefer")
            echo "Bjoern Schaefer" >> "names-processed.list" ;;
        "Benjamin Schroeter")
            echo "Benjamin Schröter" >> "names-processed.list" ;;
        "Hans Schoenemann")
            echo "Hans Schönemann" >> "names-processed.list" ;;
        "Janko Boehm")
            echo "Janko Böhm" >> "names-processed.list" ;;
        "Lukas Kuehne")
            echo "Lukas Kühne" >> "names-processed.list" ;;
        "nanleij")
            echo "Nando Leijenhorst" >> "names-processed.list" ;;
        "Sreevatsa2k")
            echo "Sreevatsa Sasisekar" >> "names-processed.list" ;;
        "Nicolas")
            echo "Nicolas Faross" >> "names-processed.list" ;;
        # "Sami-Halaseh")
        #     echo "UNKNONW Sami-Halaseh ZZZ" >> "names-processed.list" ;;
        # "MarieKaltoft")
        #     echo "UNKNONW MarieKaltoft ZZZ" >> "names-processed.list" ;;
        *)
            echo "$line" >> "names-processed.list" ;;
    esac
done < "names.list"

# Sort active contributors by last name
cat names-processed.list | sort -u > contributors-by-first-name.sorted
awk '{print $NF, $0}' contributors-by-first-name.sorted | sort -k1,1 | cut -d' ' -f2- > currently-active-contributors

# Remove unnecessary files
rm names.list
rm names-processed.list
rm contributors-by-first-name.sorted


# 9. Fetch current contributor list from OSCAR website

echo -e "\n---------------------------------------------------------------"
echo -e "9. Fetching OSCAR contributors from the OSCAR website...\n"

# Step 1: Download the file
curl -o contributors.md https://raw.githubusercontent.com/oscar-system/oscar-website/gh-pages/contributors.md

# Step 2: Process the file to keep only the lines between "contributors:" and "# Retired contributors"
awk '
    # Flag to indicate we are inside the relevant section
    /contributors:/ {inside_section=1; next} 
    /# Retired contributors/ {inside_section=0} 
    inside_section' contributors.md > temp-contributors.md

# Step 3: Filter lines that begin with "  - name:", remove comments, and remove the prefix
grep "^  - name:" temp-contributors.md | sed 's/^  - name: //' | sed 's/#.*//' | sed 's/[[:space:]]*$//' > active-contributors-OSCAR-website

# Step 4: Remove the temporary file
rm contributors.md
rm temp-contributors.md



# 10. Identify newly active and newly retired contributors

echo -e "\n---------------------------------------------------------------"
echo -e "10. Identify newly active and newly retired contributors...\n"

# Step 1: Sort both files to prepare for comparison
sort active-contributors-OSCAR-website -o active-contributors-OSCAR-website
sort currently-active-contributors -o currently-active-contributors

# Step 3: Create new-active-contributors (lines in currently-active-contributors not in active-contributors-OSCAR-website)
comm -13 active-contributors-OSCAR-website currently-active-contributors > new-active-contributors

# Step 4: Create new-retired-contributors (lines in active-contributors-OSCAR-website not in currently-active-contributors)
comm -13 currently-active-contributors active-contributors-OSCAR-website > new-retired-contributors

# Step 5: Remove unncessary files
rm currently-active-contributors
rm active-contributors-OSCAR-website


echo -e "---------------------------------------------------------------"
echo -e "11. Try to find information about new contributors on github...\n"

# Create a new output variable to hold the updated content
updated_contributors=""

while IFS= read -r contributor; do
    # Construct the search URL for the GitHub API
    search_url="https://api.github.com/search/users?q=${contributor// /+}"

    # Fetch the user data from the GitHub API
    user_data=$(curl -s "$search_url")

    # Extract the URL of the first user found (if any)
    user_url=$(echo "$user_data" | jq -r '.items[0].html_url // "Not Found"')

    # Append the results to the updated_contributors variable
    if [[ $user_url != "Not Found" ]]; then
        updated_contributors+="$contributor: $user_url\n"
    else
        updated_contributors+="$contributor: No GitHub profile found.\n"
    fi
done < new-active-contributors

# Overwrite the existing file with the results
echo -e "$updated_contributors" > new-active-contributors