#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

echo -e "${GREEN}----- START OPS MASTER ${HOSTS[0]} ------${END}"
start_ops_master ${HOSTS[0]}

