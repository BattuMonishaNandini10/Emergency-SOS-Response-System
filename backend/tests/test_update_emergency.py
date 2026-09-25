from app.services.emergency_service import update_emergency_status


def test_update_emergency_status():
    result = update_emergency_status(
        "SOS-2026-TEST-001",
        "ACKNOWLEDGED"
    )

    assert result["case_id"] == "SOS-2026-TEST-001"
    assert result["status"] == "ACKNOWLEDGED"