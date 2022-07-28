#!/bin/sh
export PYTHONPATH=src
# DIRECTORY=${1:-file/openssl_certs}
# echo $DIRECTORY
find file/openssl_certs -mindepth 1 -name \*cert\* -exec python -m pkiviewer {} \;
