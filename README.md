# Oedo
Oedo is a Python based SSH client that allows you to make connections with a multitude of options. 

# Installation
Git clone the repository into a folder of your choice.

`git clone https://github.com/m-attz/Oedo.git`

# Usage 
`python3 main.py --hostname [example.com:22] --config [somefolder/config.json]` 

You may also modify the configuration file to you suit your needs. 

If you have not yet made a connection to a new host (or are at-least not sure) you can run the provided bash script.
It save the host keys of a server into the programs known_hosts file. 

# Contributions
Any contributions are welcome despite it being a small project.

-> [C1](https://stackoverflow.com/questions/39523216/paramiko-add-host-key-to-known-hosts-permanently) - Portable known_hosts file using BASH/Python 
