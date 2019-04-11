#!/bin/bash
. ./functions.sh

while getopts 'a' OPT; do
    case $OPT in
        a) clean_all; exit 0;;
    esac
done

clean_worker
