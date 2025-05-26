#!/usr/bin/env bash
set -e
id=$(curl -s -X POST http://localhost:8000/receipts/process \
  -H "Content-Type: application/json" \
  -d '{"retailer":"R","purchaseDate":"2025-05-26","purchaseTime":"14:30","items":[],"total":"1.00"}' | jq -r .id)

echo "Got ID: $id"
curl -s http://localhost:8000/receipts/$id/points | jq .
