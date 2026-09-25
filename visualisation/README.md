# Visualisation

This folder contains the presentation layer for simulation results. It receives completed hourly results and renders them without changing energy-dispatch behaviour.

| File | Purpose |
| --- | --- |
| `dashboard.py` | Builds the Matplotlib dashboard with summary metrics, four time-series plots, storage-capacity markers, and the hourly results table. |

Run the simulation from the project root:

```bash
source venv/bin/activate
python -m simulation.main
```
