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

The project follows a simulation-first development path, progressing from deterministic microgrid control toward predictive optimisation and physical system deployment.

| Version | Goal | Major Capabilities |
|---|---|---|
| **V1.0** | Configurable EMS Simulator | Deterministic EMS, operational constraints, configurable system parameters, scenario testing, performance metrics, and simulation visualisation |
| **V1.1** | Interactive Simulation Tool | Streamlit interface, user-configurable microgrid inputs, simulation controls, interactive plots, and summary metrics |
| **V1.2** | Deployable Simulator | Docker deployment, hosted Streamlit application, scenario/configuration management, and improved documentation |
| **V2.0** | Real-World Data Integration | Weather APIs, historical weather datasets, realistic irradiance/PV inputs, and historical load/PV data ingestion |
| **V2.1** | Forecast-Aware System Modelling | Forecast future solar, load, and storage trajectories and evaluate predicted system states against observed outcomes |
| **V3.0** | Predictive EMS | ML-based system-state prediction, forecast-aware dispatch, and comparison against the deterministic V1 EMS |
| **V3.x** | Optimisation & Model Predictive Control | Multi-step dispatch optimisation, reserve management, and reliability/efficiency objectives |
| **V4.0** | Hardware-in-the-Loop EMS | Physical sensor and component interfaces, hardware-in-the-loop testing, and simulated/physical operating modes |
| **V5.0** | HyRTS Edge EMS | Local edge deployment, resilient offline operation, telemetry, remote monitoring, and field-deployment architecture |

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
| Virtual Environment (venv) | Isolated project dependencies |