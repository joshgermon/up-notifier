curl https://api.up.com.au/api/v1/webhooks \
  -XPOST \
  -H 'Authorization: Bearer up:yeah:PTkUI6G5bux4Dkpx1mODHRiP1RflwlEj7m0CktW6jDLz7IHc9xaOJywXpu3TEJIKlS2d2oLZTHnFaohjRfhkm8ORZxYLJxIKYyV9WskB9S1WIEl9x3AXIFdigWK2OpuE' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "data": {
      "attributes": {
        "url": "https://k5d4ljjvkc.execute-api.ap-southeast-2.amazonaws.com/Prod/webhook",
        "description": "Slack Webhook"
      }
    }
  }'


# {"data":{"type":"webhooks","id":"ec9f5f56-d0de-4b3b-9dab-059951c885e2","attributes":{"url":"https://k5d4ljjvkc.execute-api.ap-southeast-2.amazonaws.com/Prod/webhook","description":"Slack Webhook","secretKey":"w49u9csXv9OI55PRYOZFSNh5X8PCBl2aPV8gjiNJ51sBuKBG2Ndh5zzlTKjExXdk","createdAt":"2023-03-14T21:38:15+11:00"},"relationships":{"logs":{"links":{"related":"https://api.up.com.au/api/v1/webhooks/ec9f5f56-d0de-4b3b-9dab-059951c885e2/logs"}}},"links":{"self":"https://api.up.com.au/api/v1/webhooks/ec9f5f56-d0de-4b3b-9dab-059951c885e2"}}}%
