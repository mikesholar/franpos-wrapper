
class ClassAPI:
    def __init__(self, client):
        self.client = client

    def get_all(self):
        return self.client._get("api/classes/getAll")

    def get_by_id(self, class_id):
        return self.client._get("api/classes/get", params={"classId": class_id})
