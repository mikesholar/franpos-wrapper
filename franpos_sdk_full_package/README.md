
# franpos_sdk

A simple Python SDK for querying the [FranPOS Public API](https://publicapi.franpos.com/Help).

## Installation

```bash
pip install .
```

## Usage

```python
from franpos_sdk import FranPOSClient

client = FranPOSClient(api_key="YOUR_API_KEY")
customer = client.customer.get_by_id(customer_id=1234, location_id=1)
```
