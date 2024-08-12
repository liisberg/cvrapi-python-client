import unittest
from unittest.mock import patch

from cvrapi_client.client import CVRApiClient


class CVRApiClientTests(unittest.TestCase):
    def setUp(self):
        self.client = CVRApiClient(token="your_token", version="6", format="json")

    @patch("cvrapi_client.client.requests.request")
    def test_search_with_vat(self, mock_request):
        search_term = "12345678"
        country = "dk"
        vat = "12345678"

        self.client.search(search_term, country, vat=vat)

        mock_request.assert_called_with(
            "GET",
            "https://cvrapi.dk/api",
            headers={"Accept": "application/json"},
            params={
                "country": country,
                "vat": vat,
                "version": "6",
                "token": "your_token",
            },
        )

    @patch("cvrapi_client.client.requests.request")
    def test_search_with_name(self, mock_request):
        search_term = "Company Name"
        country = "dk"
        name = "Company Name"

        self.client.search(search_term, country, name=name)

        mock_request.assert_called_with(
            "GET",
            "https://cvrapi.dk/api",
            headers={"Accept": "application/json"},
            params={
                "country": country,
                "name": name,
                "version": "6",
                "token": "your_token",
            },
        )

    @patch("cvrapi_client.client.requests.request")
    def test_search_with_pu(self, mock_request):
        country = "dk"
        produ = "1010108256"
        search = ""

        self.client.search(search, country, produ=produ)

        mock_request.assert_called_with(
            "GET",
            "https://cvrapi.dk/api",
            headers={"Accept": "application/json"},
            params={
                "country": country,
                "produ": produ,
                "version": "6",
                "token": "your_token",
            },
        )

    @patch("cvrapi_client.client.requests.request")
    def test_search_with_phone(self, mock_request):
        search_term = "123456789"
        country = "dk"
        phone = "123456789"

        self.client.search(search_term, country, phone=phone)

        mock_request.assert_called_with(
            "GET",
            "https://cvrapi.dk/api",
            headers={"Accept": "application/json"},
            params={
                "country": country,
                "phone": phone,
                "version": "6",
                "token": "your_token",
            },
        )


if __name__ == "__main__":
    unittest.main()
