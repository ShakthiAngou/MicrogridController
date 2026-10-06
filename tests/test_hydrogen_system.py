"""Happy-path tests for hydrogen conversion and inventory coordination."""

import pytest


def test_surplus_is_converted_and_stored(hydrogen_system):
    result = hydrogen_system.store_surplus(10.0)

    expected_hydrogen = 10.0 / 33.33
    assert result["hydrogen_produced_kg"] == pytest.approx(expected_hydrogen)
    assert result["energy_stored_kwh"] == pytest.approx(10.0)
    assert hydrogen_system.current_hydrogen_kg == pytest.approx(0.5 + expected_hydrogen)


def test_stored_hydrogen_supplies_deficit(hydrogen_system):
    result = hydrogen_system.supply_deficit(10.0)

    expected_hydrogen = 10.0 / 33.33
    assert result["hydrogen_used_kg"] == pytest.approx(expected_hydrogen)
    assert result["energy_supplied_kwh"] == pytest.approx(10.0)
    assert hydrogen_system.current_hydrogen_kg == pytest.approx(0.5 - expected_hydrogen)
