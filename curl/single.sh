#!/bin/bash
# Ejentum Logic API -- Ki mode (single ability)

curl -X POST "https://ejentum-main-ab125c3.zuplo.app/logicv1/" \
  -H "Authorization: Bearer YOUR_EJENTUM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Why did our conversion rate drop 40% after the checkout redesign?", "mode": "single"}'
