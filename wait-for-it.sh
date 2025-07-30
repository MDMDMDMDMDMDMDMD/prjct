#!/usr/bin/env bash
# wait-for-it.sh

host="$1"
shift
cmd="$@"

until nc -z $host; do
  >&2 echo "Waiting for $host..."
  sleep 2
done

>&2 echo "$host is up – executing command"
exec $cmd
