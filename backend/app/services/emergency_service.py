from datetime import datetime, timezone

from backend.app.config import CASES_TABLE
from backend.app.database.dynamodb import get_table


def get_cases_table():
    return get_table(CASES_TABLE)


def create_emergency(data):
    table = get_cases_table()
    table.put_item(Item=data)
    return data


def get_emergency(case_id):
    table = get_cases_table()

    response = table.get_item(
        Key={
            "case_id": case_id
        }
    )

    return response.get("Item")


def update_emergency_status(case_id, status):
    table = get_cases_table()

    updated_at = datetime.now(timezone.utc).isoformat()

    response = table.update_item(
        Key={
            "case_id": case_id
        },
        UpdateExpression="SET #status = :status, updated_at = :updated_at",
        ExpressionAttributeNames={
            "#status": "status"
        },
        ExpressionAttributeValues={
            ":status": status,
            ":updated_at": updated_at
        },
        ReturnValues="ALL_NEW"
    )

    return response.get("Attributes")