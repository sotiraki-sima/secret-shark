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
my_array=(
    "(=\ |=)[A-Z0-9]{20}$" 
    "(=\ |=)[A-Z0-9]{40}$"
    "(access_key_id|secret_access_key)"
    "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b"
)

for i in "${my_array[@]}"; 
do 
    grep -nrIi -E "$i" --exclude-dir=.git --exclude-dir=.svn --exclude-dir=node_modules --color=always $1 | cut -c -200
done
