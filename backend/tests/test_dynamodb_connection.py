import boto3

from app.config import AWS_REGION


def test_dynamodb_connection():
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=AWS_REGION
    )

    tables = list(dynamodb.tables.all())

    print("\nDynamoDB tables:", [table.name for table in tables])

    assert "EmergencySOS-Users" in [table.name for table in tables]
    assert "EmergencySOS-Contacts" in [table.name for table in tables]
    assert "EmergencySOS-Cases" in [table.name for table in tables]