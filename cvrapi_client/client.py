import requests

SEARCH_PARAMS = {
    "vat": "vat",
    "name": "name",
    "produ": "produ",
    "phone": "phone",
}


class CVRApiClient:
    def __init__(self, token=None, version="6", format="json"):
        self.base_url = "https://cvrapi.dk/api"
        self.token = token
        self.version = version
        self.format = format

    def _make_request(self, method, params):
        headers = {"Accept": f"application/{self.format}"}
        if self.token:
            params["token"] = self.token

        params["version"] = self.version
        response = requests.request(
            method, self.base_url, headers=headers, params=params
        )

        if response.status_code == 200:
            return response.json() if self.format == "json" else response.text
        else:
            response.raise_for_status()

    def search(self, country, *args, **kwargs):
        """
        Search the CVR API with the required and optional parameters.

        :param country: The country to search in ('dk' for Denmark, 'no' for Norway).
        :kwargs search: The search term (CVR number, P number, or company name).
        :kwargs vat: (Optional) Search specifically by CVR number.
        :kwargs name: (Optional) Search specifically by company name.
        :kwargs pu: (Optional) Search specifically by production unit.
        :kwaargs phone: (Optional) Search specifically by phone number.
        :return: JSON or XML response based on the format.
        """
        params = {
            "country": country,
            "search": "",
        }

        # Ensure only one specific search option is provided
        specified_params = {
            SEARCH_PARAMS[k]: v for k, v in kwargs.items() if k in SEARCH_PARAMS
        }
        # If no specific search option is provided, use the search term
        if not specified_params:
            params["search"] = args[0]

        print("specified_params", specified_params)

        # Update params with the specific search parameter, if provided
        if specified_params:
            params.pop("search")
            params.update(specified_params)

        if len(specified_params) > 1:
            raise ValueError(
                "Only one specific search option (vat, name, produ, phone) can be used at a time."
            )

        return self._make_request("GET", params)
