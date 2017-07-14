# Ansible role for proxying Lustre quotas

Lustre, when re-exported over NFS, doesn't relay quota information.
This setups a simple lighttpd server which answers quota requests.  It
is used from https://github.com/jabl/fancyquota.

Little setup is needed.  The role installs lighttpd, sets a cgi script
(quota.cgi), and installs a sudo rule to allow `lfs quota` to be run.
You need to allow port 80 to reach the host from trusted networks.

# Security

Anyone who can connect can get the quota of any group, there is no
authentication.

# Info

Copyright Richard Darst 2017.  Licensed under GPLv3+.
