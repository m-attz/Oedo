#!/bin/bash


# print output of sub-command
OUTPUT=$(ssh-keygen -F $1)
echo $OUTPUT

echo -e "Would you like to generate a new key (y)? \c"
read choice

# generate a new key if y/yes
if [[ $choice == "y" || $choice == "yes" ]]; then
    echo "Generating SSH key..."
    $(ssh -o GlobalKnownHostsFile=/dev/null -o UserKnownHostsFile=./known_hosts $1)
    echo "Key saved in ./known_hosts file..."
else
    exit 1
fi
