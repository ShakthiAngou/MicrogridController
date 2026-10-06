"""Happy-path tests for hydrogen inventory storage."""


def test_store_updates_inventory_and_soc():
    from simulation.hydrogen import HydrogenStorage

    storage = HydrogenStorage(capacity_kg=1.0, initial_hydrogen_kg=0.25)

    stored = storage.store(0.25)

    assert stored == 0.25
    assert storage.current_hydrogen_kg == 0.5
    assert storage.get_state_of_charge() == 50.0


def test_withdraw_updates_inventory_and_soc():
    from simulation.hydrogen import HydrogenStorage

    storage = HydrogenStorage(capacity_kg=1.0, initial_hydrogen_kg=0.75)

    withdrawn = storage.withdraw(0.25)

    assert withdrawn == 0.25
    assert storage.current_hydrogen_kg == 0.5
    assert storage.get_state_of_charge() == 50.0
