import boto3
import os
import json
from datetime import datetime

client = boto3.client("s3")
bucket = os.getenv("BUCKET")


def handler(event, context):

    try:
        widget_name = (
            event["path"][1:] if event["path"].startswith("/") else event["path"]
        )
        method = event["httpMethod"]

        if method == "GET":
            if event["path"] == "/":
                data = client.list_objects_v2(Bucket=bucket)
                if "Contents" in data:
                    body = {"widgets": [x["Key"] for x in data["Contents"]]}
                else:
                    body = []
                return {"statusCode": 200, "headers": {}, "body": json.dumps(body)}
            if widget_name:
                data = client.get_object(Bucket=bucket, Key=widget_name)
                return {"statusCode": 200, "headers": {}, "body": data}

        if method == "POST":
            if not widget_name:
                return {"statusCode": 400, "headers": {}, "body": "Please give a name"}
            now = datetime.now()
            data = widget_name + " created: " + str(now)
            client.put_object(
                Bucket=bucket,
                Key=widget_name,
                ContentType="application/json",
                Body=data,
            )
            return {"statusCode": 201, "headers": {}, "body": ""}
        if method == "DELETE":
            if not widget_name:
                return {"statusCode": 400, "headers": {}, "body": "Please give a name"}
            now = datetime.now()
            data = widget_name + " created: " + now
            client.delete_object(
                Bucket=bucket,
                Key=widget_name,
            )
            return {statusCode: 200, headers: {}, body: f"Deleted {widget_name}"}
        else:
            return {
                "statusCode": 400,
                "headers": {},
                "body": "We only accept GET, POST, and DELETE, not " + method,
            }
    except Exception as e:
        body = str(e)
        return {"statusCode": 400, "headers": {}, "body": body}
