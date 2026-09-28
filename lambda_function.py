import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ.get("TABLE_NAME", "visitor-counter-tf")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    response = table.update_item(
        Key={"id": "visitor-count"},
        UpdateExpression="SET #c = #c + :incr",
        ExpressionAttributeNames={"#c": "count"},
        ExpressionAttributeValues={":incr": 1},
        ReturnValues="UPDATED_NEW"
    )

    new_count = int(response["Attributes"]["count"])

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({"count": new_count})
    }