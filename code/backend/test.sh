curl -X POST http://127.0.0.1:3005/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create a responsive navigation bar with dropdown menus",
    "type": "component"
  }'


curl -X POST http://127.0.0.1:3005/patterns \
  -H "Content-Type: application/json" \
  -d '{
    "pattern_id": "comp-custom-001",
    "name": "Custom Alert",
    "category": "components",
    "content": "... your component code ...",
    "tags": ["alert", "notification"]
  }'
