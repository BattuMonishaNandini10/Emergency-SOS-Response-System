from app.services.emergency_service import get_emergency


def test_get_existing_emergency():
    result = get_emergency("SOS-2026-000001")

    assert result is not None
    assert result["case_id"] == "SOS-2026-000001"