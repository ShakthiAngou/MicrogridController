"""Happy-path tests for the supercapacitor model."""

import pytest


def test_charge_updates_energy_and_soc(supercapacitor):
    charged = supercapacitor.charge(2.0)

    assert charged == 2.0
    assert supercapacitor.current_energy_kwh == 7.0
    assert supercapacitor.get_state_of_charge() == 70.0


def test_discharge_updates_energy_and_soc(supercapacitor):
    discharged = supercapacitor.discharge(2.0)

    assert discharged == 2.0
    assert supercapacitor.current_energy_kwh == 3.0
    assert supercapacitor.get_state_of_charge() == 30.0


def test_storage_limits_requested_charge(supercapacitor):
    charged = supercapacitor.charge(20.0)

    assert charged == 5.0
    assert supercapacitor.current_energy_kwh == 10.0


def test_storage_limits_requested_discharge(supercapacitor):
    discharged = supercapacitor.discharge(20.0)

    assert discharged == 5.0
    assert supercapacitor.current_energy_kwh == 0.0


def test_negative_charge_is_rejected(supercapacitor):
    with pytest.raises(ValueError):
        supercapacitor.charge(-1.0)
