Write a module that will create a passwordless connection for a set of Linux machines.

This means we need to generate an ssh key-pair(s) and distribute it over all the machines supplied.

This can be either a single pair of keys for all machines or each pair distributed over each machine.

Mind the ability of automated clearing ssh key pairs from hosts. *Would be nice to have backup and restore functions.

The set of machine IPs should be taken from a file nearby. Consider password and login are known in constants, or set in the config file.
