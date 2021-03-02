curl "http://localhost:8000/comments/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "comment": {
      "comment": "'"${COMMENT}"'"
    }
  }'

echo
