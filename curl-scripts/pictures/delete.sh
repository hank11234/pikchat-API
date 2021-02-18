#!/bin/bash

curl "http://localhost:8000/pictures/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
