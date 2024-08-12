# cvrapi-python-client
Official python client for [CVRAPI](https://cvrapi.dk/documentation).
CVRAPI allows you to fetch information about Danish and Norwegian companies in a reliable manner.


Usage
----
```
# Example usage:
from cvrapi_client.client import CVRApiClient
client = CVRApiClient(token="your_token_here")

try:
    response = client.search(search="24256790", country="dk")
    print(response)
except Exception as e:
    print(f"Error: {e}")

```

License
----
The MIT License (MIT). Please see [License File](LICENSE) for more information.
