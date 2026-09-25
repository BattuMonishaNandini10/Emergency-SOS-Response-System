import os

APP_NAME = os.getenv(
    "APP_NAME",
    "Emergency SOS & Response System"
)

AWS_REGION = os.getenv(
    "AWS_REGION",
    "us-east-1"
)

USERS_TABLE = os.getenv(
    "USERS_TABLE",
    "EmergencySOS-Users"
)

CONTACTS_TABLE = os.getenv(
    "CONTACTS_TABLE",
    "EmergencySOS-Contacts"
)

CASES_TABLE = os.getenv(
    "CASES_TABLE",
    "EmergencySOS-Cases"
)

CASES_USER_INDEX = os.getenv(
    "CASES_USER_INDEX",
    "UserIdIndex"
)