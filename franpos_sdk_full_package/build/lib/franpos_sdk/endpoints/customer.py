
class CustomerAPI:
    def __init__(self, client):
        self.client = client

    def get_by_id(self, customer_id, location_id):
        return self.client._get(f"api/Customers/{customer_id}", params={"locationId": location_id})

    def search(self, query, filter_type="email"):
        return self.client._get("api/customer/search", params={"query": query, "filterType": filter_type})
