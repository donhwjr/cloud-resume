import json
import unittest
from unittest.mock import patch

import lambda_function


class TestLambdaFunction(unittest.TestCase):

    @patch("lambda_function.table")
    def test_lambda_handler_returns_incremented_count(self, mock_table):
        mock_table.update_item.return_value = {
            "Attributes": {
                "count": 42
            }
        }

        response = lambda_function.lambda_handler({}, None)

        self.assertEqual(response["statusCode"], 200)

        body = json.loads(response["body"])
        self.assertEqual(body["count"], 42)

        self.assertEqual(
            response["headers"]["Access-Control-Allow-Origin"],
            "*"
        )

        mock_table.update_item.assert_called_once_with(
            Key={"id": "visitor-count"},
            UpdateExpression="SET #c = #c + :incr",
            ExpressionAttributeNames={"#c": "count"},
            ExpressionAttributeValues={":incr": 1},
            ReturnValues="UPDATED_NEW"
        )


if __name__ == "__main__":
    unittest.main()