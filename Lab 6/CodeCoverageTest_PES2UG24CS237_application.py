
import pytest

from fuel_station import fuel_bill, pump_allowed, session_status


# -------------------- FUEL BILL TESTS --------------------

def test_fuel_bill_regular_with_extra_litres():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_fuel_bill_gold_discount():
    assert fuel_bill("regular", 50, "gold") == 3325


def test_fuel_bill_diesel():
    assert fuel_bill("diesel", 30, "silver") == 900


def test_fuel_bill_large_diesel_purchase():
    assert fuel_bill("diesel", 60, "silver") == 3360


def test_fuel_bill_invalid_grade():
    with pytest.raises(ValueError, match="unknown fuel grade"):
        fuel_bill("kerosene", 10, "silver")


def test_fuel_bill_negative_litres():
    with pytest.raises(ValueError, match="invalid litres"):
        fuel_bill("regular", -1, "silver")


def test_fuel_bill_within_covered_litres():
    assert fuel_bill("regular", 5, "silver") == 0


def test_fuel_bill_gold_diesel():
    assert fuel_bill("diesel", 25, "gold") == 450


def test_fuel_bill_premium():
    assert fuel_bill("premium", 20, "silver") == 525


def test_fuel_bill_gold_large_purchase():
    assert fuel_bill("premium", 60, "gold") == 3800


# -------------------- PUMP PERMISSION TESTS --------------------

def test_pump_fleet_allowed():
    assert pump_allowed(200, 5, True) is True


def test_pump_fleet_over_limit():
    assert pump_allowed(201, 5, True) is False


def test_pump_non_fleet_allowed():
    assert pump_allowed(50, 1, False) is True


def test_pump_non_fleet_over_limit():
    assert pump_allowed(61, 1, False) is False


def test_pump_multiple_containers():
    assert pump_allowed(40, 2, False) is False


# -------------------- SESSION STATUS TESTS --------------------

def test_session_card_active():
    assert session_status(60, True, False) == "active"


def test_session_night_active():
    assert session_status(90, False, True) == "active"


def test_session_night_warning():
    assert session_status(45, False, True) == "warning"


def test_session_timed_out():
    assert session_status(10, False, False) == "timed_out"


def test_session_card_warning():
    assert session_status(50, True, False) == "warning"
