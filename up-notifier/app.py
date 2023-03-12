import json
from typing import Dict, Any

def lambda_handler(event, context: Dict[str, Any]):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

