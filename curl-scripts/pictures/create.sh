#!/bin/bash

curl "http://localhost:8000/pictures/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "picture": {
      "title": "'"${TITLE}"'",
      "picture": "'"${PICTURE}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
