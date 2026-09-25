from app.config import CASES_TABLE, AWS_REGION


def test_dynamodb_configuration():
    assert AWS_REGION == "us-east-1"
    assert CASES_TABLE == "EmergencySOS-Cases"