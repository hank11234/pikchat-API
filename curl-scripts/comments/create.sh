curl "http://localhost:8000/comments/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "comment": {
      "comment": "'"${COMMENT}"'",
      "pictureId": "'"${PICTUREID}"'"
    }
  }'

echo