"""Tests for generation and load balance classification."""

from controller.energy_balance import calculate_net_energy, determine_energy_status


def test_surplus_energy_is_positive():
    assert calculate_net_energy(solar=8.0, load=3.0) == 5.0


def test_deficit_energy_is_negative():
    assert calculate_net_energy(solar=3.0, load=8.0) == -5.0


def test_energy_status_matches_balance():
    assert determine_energy_status(5.0) == "SURPLUS"
    assert determine_energy_status(-5.0) == "DEFICIT"
    assert determine_energy_status(0.0) == "BALANCED"
