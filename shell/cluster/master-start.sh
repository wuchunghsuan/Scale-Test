#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

echo -e "${GREEN}----- START RESOURCEMANAGER ${HOSTS[0]} ------${END}"
start_resourcemanager ${HOSTS[0]}

