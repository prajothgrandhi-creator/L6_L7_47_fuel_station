
import pytest

from fuel_station import fuel_bill, pump_allowed, session_status


# -------------------- FUEL BILL BRANCH TESTS --------------------

def test_invalid_fuel_grade():
    with pytest.raises(ValueError, match="unknown fuel grade"):
        fuel_bill("kerosene", 10, "silver")


def test_negative_litres():
    with pytest.raises(ValueError, match="invalid litres"):
        fuel_bill("regular", -1, "silver")


def test_gold_regular_fuel():
    assert fuel_bill("regular", 20, "gold") == 525


def test_gold_diesel_fuel():
    assert fuel_bill("diesel", 30, "gold") == 900


def test_extra_litres_not_over_30():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_extra_litres_over_30_gold():
    assert fuel_bill("regular", 50, "gold") == 3325


def test_extra_litres_over_30_silver():
    assert fuel_bill("diesel", 60, "silver") == 3360


def test_premium_fuel():
    assert fuel_bill("premium", 20, "silver") == 525


def test_fuel_within_covered_amount():
    assert fuel_bill("regular", 5, "silver") == 0


# -------------------- PUMP PERMISSION BRANCH TESTS --------------------

def test_fleet_within_limit():
    assert pump_allowed(200, 5, True) is True


def test_fleet_over_limit():
    assert pump_allowed(201, 5, True) is False


def test_non_fleet_within_limit_one_container():
    assert pump_allowed(50, 1, False) is True


def test_non_fleet_over_60_litres():
    assert pump_allowed(61, 1, False) is False


def test_non_fleet_multiple_containers():
    assert pump_allowed(40, 2, False) is False


def test_non_fleet_exactly_60_litres():
    assert pump_allowed(60, 1, False) is True


# -------------------- SESSION STATUS BRANCH TESTS --------------------

def test_card_payment_active():
    assert session_status(60, True, False) == "active"


def test_cash_payment_active():
    assert session_status(30, False, False) == "active"


def test_night_session_active():
    assert session_status(90, True, True) == "active"


def test_card_payment_warning():
    assert session_status(50, True, False) == "warning"


def test_night_session_warning():
    assert session_status(45, False, True) == "warning"


def test_session_timed_out():
    assert session_status(10, False, False) == "timed_out"
