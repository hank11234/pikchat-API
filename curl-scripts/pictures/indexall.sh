
curl "http://localhost:8000/pictures/all/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
