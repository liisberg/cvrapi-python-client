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

    def search(self, search, country, *args, **kwargs):
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
        # Validate and construct the search parameters
        params = {"country": country}

        # Filter and validate specific search parameters
        specified_params = {
            SEARCH_PARAMS[k]: v for k, v in kwargs.items() if k in SEARCH_PARAMS
        }

        if len(specified_params) > 1:
            raise ValueError(
                "Only one specific search option (vat, name, produ, phone) can be used at a time."
            )

        if specified_params:
            params.update(specified_params)
        elif search:
            params["search"] = search
        else:
            raise ValueError(
                "You must provide either a 'search' term or a specific search option (vat, name, produ, phone)."
            )

        return self._make_request("GET", params)
