#!/usr/bin/env bash

set -e

# minimal valid receipt
json='{
  "retailer": "SmokeTest",
  "purchaseDate": "2025-05-26",
  "purchaseTime": "15:00",
  "items": [],
  "total": "1.00"
}'

id=$(curl -s -X POST http://localhost:8000/receipts/process \
        -H 'Content-Type: application/json' \
        -d "$json" | jq -r .id)

echo "Got ID: $id"

curl -s http://localhost:8000/receipts/$id/points | jq .