import json
import unittest
import urllib.request

API_URL = "https://l7bbqaunlb.execute-api.us-east-1.amazonaws.com/count"


class TestVisitorCounterAPI(unittest.TestCase):

    def test_api_returns_count(self):
        with urllib.request.urlopen(API_URL) as response:
            self.assertEqual(response.status, 200)

            body = json.loads(response.read().decode("utf-8"))

            self.assertIn("count", body)
            self.assertIsInstance(body["count"], int)


if __name__ == "__main__":
    unittest.main()