import json
import time
import random
import base64
from decimal import Decimal, getcontext

# Set decimal precision
getcontext().prec = 20


def prepare_message(battery_id: str) -> str:
    current_epoch_time = int(time.time())
    double_a = Decimal(random.uniform(0.0, 10.0))
    double_b = Decimal(random.uniform(0.0, 10.0))
    integer_val = random.randint(1, 1000)
    sample_binary_data = bytes([random.randint(0, 255) for _ in range(8)])

    message = {
        "BatteryID": battery_id,
        "Timestamp": current_epoch_time,
        "A": str(double_a),
        "B": str(double_b),
        "C": integer_val,
        "D": base64.b64encode(sample_binary_data).decode()
    }

    json_message = json.dumps(message)
    return json_message
