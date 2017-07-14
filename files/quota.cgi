#!/bin/sh
echo Content-type: text/plain
echo

# stderr to stdout
exec 2>&1

# allow ONLY 0-9a-z in the gid.  ONLY return this in gid.
gid=$(echo "$QUERY_STRING" | sed -n 's/^.*gid=\([0-9a-z]*\).*$/\1/p' )

if [ -z "$gid" -o "$gid" = 0  -o "$gid" = "root" ] ; then
   echo "invalid gid"
   exit 0
fi

# this command must exactly match sudoers
sudo /bin/lfs quota -g "$gid" /scratch 2>&1 | grep scratch
