openssl genrsa -out private.key 2048
openssl rsa -in private.key -pubout -out public.key

# Script for generating keys for local testing