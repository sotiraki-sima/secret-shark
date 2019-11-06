#!/bin/bash
grep -nrI -E --exclude-dir=.git --exclude-dir=doc --exclude-dir=.svn --exclude-dir=node_modules  "$1" $2

# --color=always
