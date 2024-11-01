#!/usr/bin/env python3

import os.path
import paramiko
import argparse
import json
import sys


def main(hostname: str, username = None, password = None, config = None):
    # Open a file, read it, then load it as a dictionary

    config_file = open(config, "r")
    config_loaded = json.load(config_file)

    # Initiate client object
    client = paramiko.client.SSHClient()

    client.load_host_keys(os.path.join(os.path.dirname(__file__), "known_hosts"))


    try:
        client.connect(
            hostname,
            port=22,
            username=username,
            password=password,
            banner_timeout=config_loaded["banner_timeout"],
            auth_timeout=config_loaded["auth_timeout"],
            timeout=config_loaded["timeout"]
        )
    except paramiko.ssh_exception.BadHostKeyException:
        raise SystemExit("Server error: Host key could not be verified...")
    except paramiko.ssh_exception.AuthenticationException:
        raise SystemExit("Authentication error...")
    except paramiko.ssh_exception.NoValidConnectionsError:
        raise SystemExit("Connection error: Host unreachable...")
    except paramiko.ssh_exception.SSHException:
        raise SystemExit("SSH error: Could not establish SSH session...")



    # Pipe shell commands to to _stdin then print output
    try:
        while True:
            shell_command = str(input("Oedo: $ "))
            if shell_command == "exit":
                client.close()
                break
            else:
                _stdin, _stdout, _stderr = client.exec_command(shell_command)
                if _stderr != None:
                    print(_stderr.read().decode())

                print(_stdout.read().decode())
    except paramiko.ssh_exception.SSHException as e:
        print(e)
    except paramiko.ssh_exception.ChannelException:
        client.close()






# length of args determine n values passed when calling main
if __name__ == '__main__':
    # Initialize arg parser and add args
    parser = argparse.ArgumentParser(usage="main.py [options]")
    parser.add_argument("--host", type=str, help="main.py --host [hostname]")
    parser.add_argument("--username", type=str, help="main.py --host [hostname] --user [username]")
    parser.add_argument("--password", type=str, help="main.py --host [hostname] --pass [password]")
    parser.add_argument("--config", type=str, help="main.py --host [hostname] --config [file]")

    args = parser.parse_args()

    main(args.host, args.username, args.password, args.config)
