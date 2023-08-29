import json
import base64
from decimal import Decimal, getcontext

# Set decimal precision
getcontext().prec = 20


def parse_message(json_message: str) -> dict:
    decoded_message = json.loads(json_message)

    decoded_message["A"] = Decimal(decoded_message["A"])
    decoded_message["B"] = Decimal(decoded_message["B"])

    decoded_message["D"] = base64.b64decode(decoded_message["D"])

    return decoded_message
