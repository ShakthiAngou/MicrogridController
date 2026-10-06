# Simulation

This folder contains the component models and the 24-hour microgrid simulation.

| File | Purpose |
| --- | --- |
| `main.py` | Runs the hourly simulation, supplies inputs to the EMS, records results, and starts the dashboard. |
| `solar.py` | Provides a synthetic hourly solar-generation profile. |
| `load.py` | Provides a synthetic hourly load-demand profile. |
| `supercapacitor.py` | Models short-duration electrical storage, including state of charge, charging, and discharging. |
| `hydrogen.py` | Tracks hydrogen inventory and storage capacity. |
| `electrolyser.py` | Converts surplus electrical energy into hydrogen using the current idealised model. |
| `fuel_cell.py` | Converts stored hydrogen into electrical energy using the current idealised model. |
| `hydrogen_system.py` | Coordinates hydrogen storage, electrolysis, and fuel-cell conversion behind one subsystem interface. |

## Run the simulation

From the project root: ShakthiEnergy

```bash
source venv/bin/activate
python -m simulation.main
```

## Run the tests

From the project root, activate the virtual environment and run the full
pytest suite:

```bash
source venv/bin/activate
python -m pytest
```

Useful alternatives:

```bash
python -m pytest -q                         # concise output
python -m pytest tests/test_energy_manager.py # run one test module
python -m pytest tests/test_supercapacitor.py # run component tests
```

## Current assumptions

- The simulation runs in one-hour steps over a single day.
- Solar and load profiles are synthetic.
- Hydrogen conversion is idealised and instantaneous.
- The supercapacitor responds before hydrogen storage during a deficit.
