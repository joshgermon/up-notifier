import json
from typing import Dict, Any
import requests
import os
from up_api import Transaction, UpAPI

def lambda_handler(event, context: Dict[str, Any]):
    data = json.loads(event['body'])
    handle_transaction_event(data)
    return

def get_transaction_from_event(event) -> Transaction:
    transaction_id = event["data"][0]["id"]
    return UpAPI.get_transaction_by_id(transaction_id)

def handle_transaction_event(event):
    print(event)
    transaction = get_transaction_from_event(event)
    message = prettify_transaction(transaction)
    slack_publish_result = publish_slack_message(message)
    return slack_publish_result

def prettify_transaction(txn: Transaction):
    return f"""
    New Transaction
    Status: {txn.status}
    Amount: {txn.amount.value}
    Description: {txn.raw_text}
    Message: {txn.message}
    """

def publish_slack_message(message: str):
    SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK')
    # TODO: error handle this not existing
    return requests.post(SLACK_WEBHOOK, json={"text": message})
