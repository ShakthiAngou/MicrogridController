# Controller

This folder contains Energy Management System control logic that makes dispatch decisions independently of the component models.

| File | Intended purpose |
| --- | --- |
| `energy_manager.py` | Rule-based EMS entry point that receives solar and load inputs, allocates energy, and returns hourly dispatch results. |
| `energy_balance.py` | Calculates generation-minus-demand balance and labels it as surplus, deficit, or balanced. |
| `dispatch.py` | Dispatch rules and energy-allocation actions. |
| `priorities.py` | Storage and load-serving priority policies. |
| `constraints.py` | Operating limits, reserves, and safety constraints. |
