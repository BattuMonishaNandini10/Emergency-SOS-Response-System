from app.services.emergency_service import create_emergency


def test_create_emergency():
    data = {
        "case_id": "SOS-2026-TEST-001",
        "user_id": "USER-001",
        "status": "OPEN",
        "description": "Test emergency case"
    }

    result = create_emergency(data)

    assert result["case_id"] == "SOS-2026-TEST-001"
    assert result["status"] == "OPEN"