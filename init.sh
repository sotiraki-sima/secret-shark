#!/bin/bash

echo -e \
"
##########################################################
#                                                        #
#          Search for confidential information           #
#                    Version: 0.2                        #
#                Author: Sotiraki Sima                   #
#                                                        #
##########################################################
"
regex_array=(
    "(=\ |=)[A-Z0-9]{20}$" 
    "(=\ |=)[A-Z0-9]{40}$"
    "(access_key_id|secret_access_key)"
)

no_in_use_regex_array=(
    "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b"
)


files_array=(
    "*.pem"
    "id_rsa"
    "authorized_keys"
)

echo -e \
"
##########################################################
#                     Find Command                       #
##########################################################
"

for i in "${files_array[@]}"; 
do 
    find $1 -name "$i" 2>/dev/null
done




echo -e \
"
##########################################################
#                     Grep Command                       #
##########################################################
"

for i in "${regex_array[@]}"; 
do 
    grep -nrI -E "$i" --exclude-dir=.git --exclude-dir=.svn --exclude-dir=node_modules --color=always $1 | cut -c -200 2>/dev/null
done
