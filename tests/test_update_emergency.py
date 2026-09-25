from app.services.emergency_service import (
    create_emergency,
    update_emergency_status
)


def test_update_emergency_status():
    data = {
        "case_id": "SOS-2026-TEST-001",
        "user_id": "USER-001",
        "status": "OPEN",
        "description": "Test emergency case"
    }

    create_emergency(data)

    result = update_emergency_status(
        "SOS-2026-TEST-001",
        "IN_PROGRESS"
    )

    assert result["case_id"] == "SOS-2026-TEST-001"
    assert result["status"] == "IN_PROGRESS"
    assert "updated_at" in result