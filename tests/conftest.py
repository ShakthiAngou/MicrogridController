"""Shared pytest fixtures for EMS component and dispatch tests."""

import pytest

from controller.energy_manager import EnergyManager
from simulation.hydrogen_system import HydrogenSubsystem
from simulation.supercapacitor import Supercapacitor


@pytest.fixture
def supercapacitor():
    """Return a standard supercapacitor test instance."""
    return Supercapacitor(capacity_kwh=10.0, initial_energy_kwh=5.0)


@pytest.fixture
def hydrogen_system():
    """Return a standard hydrogen subsystem test instance."""
    return HydrogenSubsystem(capacity_kg=1.0, initial_hydrogen_kg=0.5)


@pytest.fixture
def energy_manager(supercapacitor, hydrogen_system):
    """Return an EMS connected to standard storage test instances."""
    return EnergyManager(supercapacitor, hydrogen_system)
