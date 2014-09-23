#!/bin/bash

#Unzips the student submissions into the folder one level up - they are now on
# the same level as timestamp.txt

shopt -s nullglob


if [[ "$#" -ne 1 ]]; then 
	echo "Usage: unzip.sh [path_to_base_folder]"
fi

cd "$1"

for f in */ ; do
	cd "$f"Submission\ attachment\(s\)/
	unzip -j *.zip -d ../ > /dev/null
	cd ../../
done

echo "done!"