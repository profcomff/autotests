class KiwiClient:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        pass

    def create_test_run(self, plan_id, build_id, assignee_id):
        print(f"Creating test run for plan {plan_id}, build {build_id}, assignee {assignee_id}")
        return {"id": 123, "name": "Sample Test Run"}
