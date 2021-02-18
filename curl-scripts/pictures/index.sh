#!/bin/bash

curl "http://localhost:8000/pictures/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
