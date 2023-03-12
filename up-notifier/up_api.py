import os
import requests
from pydantic import BaseModel
from typing import Dict, List, Any, Union
from utils import to_camel


class Amount(BaseModel):
    currency_code: str
    value: str
    value_in_base_units: int

    class Config:
        alias_generator = to_camel


class Transaction(BaseModel):
    id: str
    status: str
    raw_text: Union[str, None]
    description: str
    message: Union[str, None]
    is_categorizable: bool
    cashback: Union[str, None]
    amount: Amount
    foreign_amount: Union[str, None]
    settled_at: str
    created_at: str

    class Config:
        alias_generator = to_camel


class UpAPI:
    _BASE_URL = "https://api.up.com.au/api/v1"
    # TODO: error handle this not existing
    _TOKEN = os.environ.get('UP_TOKEN')

    @classmethod
    def _get(self, path: str):
         return requests.get(f"{self._BASE_URL}{path}", headers={"Authorization": f"Bearer {self._TOKEN}"}).json()

    @classmethod
    def get_all_transactions(self, path) -> List[Transaction]:
        transaction_res = self._get('/tranasactions')
        return list(map(self.parse_transaction, transaction_res["data"]))

    @classmethod
    def get_transaction_by_id(self, id):
        transaction = self._get(f"/transaction/{id}")
        return self.parse_transaction(transaction)

    @classmethod
    def parse_transaction(transaction: Dict[str, Any]):
        parsed_transaction = transaction["attributes"]
        parsed_transaction["id"] = transaction["id"]
        return Transaction.parse_obj(parsed_transaction)
