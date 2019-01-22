# cvrapi-python-client
Official python client for [CVRAPI](https://cvrapi.dk/documentation).
CVRAPI allows you to fetch information about Danish and Norwegian companies in a reliable manner.

Installation
----
Add to requirements.txt:
```
cvrapi-python-client
```
or install with pip3:
```
$ pip3 install cvrapi-python-client
```


Usage
----
```
from cvrapi_client import CVRAPIClient

UA = 'CVRAPI Test - cvrapi-python-client - cvrapi-test-user +45 12341234'
client = CVRAPIClient(UA, 'dk')

# Initialize a client using a different version of the CVRAPI
client = CVRAPIClient(UA, 'dk', '5')

# Get by VAT number, return result as JSON
cvrapi = client.post('?vat=10150817', 'json')
print(cvrapi)

# Get by company name, return result as JSON
cvrapi = client.get('?name=Erhvervsstyrelsen', 'json')
print(cvrapi)

# Get by production unit number, return result as XML
cvrapi = client.post('?produ=1018836250', 'xml')
print(cvrapi)

# Get by phone number, return XML
cvrapi = client.get('?phone=35291000', 'xml')
print(cvrapi)

# Get by VAT number using a token, return result as JSON
cvrapi = client.post('?vat=10150817', 'json', '<your token>')
print(cvrapi)

```

License
----
The MIT License (MIT). Please see [License File](LICENSE) for more information.
