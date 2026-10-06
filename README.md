# Decentralised Microgrid Controller

This repository documents the research, architecture, simulation, and software development of an intelligent Energy Management System (EMS) for decentralised hybrid microgrids.

The long-term goal of this project is to develop a modular control platform capable of managing an energy system incorporating:
1. Solar generation
2. Short- and long-duration energy storage
3. Hydrogen energy storage
4. Intelligent energy dispatch
5. Energy forecasting and optimisation

This project begins as a software-only simulation platform and development environment. The EMS is developed and validated against simulated microgrid components before progressively evolving toward hardware-in-the-loop testing and eventually deployment on physical energy systems.

<br>

# Project Vision

Modern energy systems are becoming increasingly decentralised, renewable, and complex. Traditional EMS and SCADA systems are often expensive, rigid, and not yet adapted to renewable microgrids.

This project aims to explore a modular, simulation-first EMS architecture in which the control software is developed independently from the physical energy assets it manages.

# Long-Term Goal

### The long-term objective is to explore how intelligent decentralised control systems can improve rural energy access and grid resilience.

# System Architecture

The EMS is structured into modular layers.

```text
                ┌─────────────────┐
                │ Microgrid       │
                │ Environment     │
                │                 │
                │ Solar Profile   │
                │ Load Demand     │
                │ Weather Inputs  │
                │ Hydrogen State  │
                │ Supercap State  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ EMS Controller  │
                │                 │
                │ Dispatch Logic  │
                │ Optimisation    │
                │ Forecast Rules  │
                │ Safety Rules    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Decision Engine │
                │                 │
                │ Use Solar       │
                │ Charge Battery  │
                │ Use Hydrogen    │
                │ Shed Load       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Visualisation   │
                │                 │
                │ Dashboard       │
                │ Metrics         │
                │ Logs            │
                └─────────────────┘
```

---

# System Modules

### 1. Environment Simulation

Simulates the external microgrid environment.

### 2. EMS Controller

The core intelligence layer of the system.

### 3. Decision Engine

Converts controller outputs into actionable energy allocation decisions.

### 4. Visualisation Layer

Provides insight into system behaviour and performance.

# Repository Structure

```text
research/         → Notes, references, and conceptual documentation
simulation/       → Environment simulation and system models
controller/       → EMS control logic and dispatch algorithms
visualisation/    → Dashboards, plotting, and telemetry tools
docs/             → Architecture diagrams and design notes
```

# Development Roadmap

The project follows a simulation-first development path. Version 1 focuses on turning the existing EMS simulation into a complete, publicly usable software system while keeping the simulation, controller, visualisation, and deployment layers independent.

| Version | Goal | Major capabilities |
|---|---|---|
| **V1.0** | Publicly usable EMS simulator | Configurable rule-based hybrid microgrid simulation, hydrogen subsystem coordination, scenario testing, operational constraints, structured logging, Streamlit interface, Docker deployment, hosted access, and CI validation |
| **V2.0** | Real-world data integration | Weather APIs, historical weather datasets, realistic irradiance/PV inputs, and historical load/PV data ingestion |
| **V2.1** | Forecast-aware system modelling | Forecast future solar, load, and storage trajectories and compare predicted states with observed outcomes |
| **V3.0** | Predictive EMS | ML-based system-state prediction and forecast-aware dispatch compared with the deterministic V1 EMS |
| **V3.x** | Optimisation and model predictive control | Multi-step dispatch optimisation, reserve management, and reliability or efficiency objectives |
| **V4.0** | Hardware-in-the-loop EMS | Physical sensor and component interfaces and simulated or physical operating modes |
| **V5.0** | HyRTS edge EMS | Local edge deployment, resilient offline operation, telemetry, remote monitoring, and field-deployment architecture |

The long-term development progression is:

```text
Simulation
    ↓
Interactive Simulation
    ↓
Real-World Data
    ↓
Forecast-Aware Modelling
    ↓
Predictive & Optimised Control
    ↓
Hardware-in-the-Loop
    ↓
Physical HyRTS Deployment
```

# Tooling and Dependencies

| Tool | Purpose |
|---|---|
| Python | Primary development language |
| Git | Version control and development tracking |
| NumPy | Numerical computation and simulation math |
| Matplotlib | Data visualisation and simulation analysis |
| Ruff | Python formatting and linting |
| pytest | Automated unit and integration testing |
| Virtual Environment (venv) | Isolated project dependencies |
