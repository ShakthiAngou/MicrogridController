# Decentralised Microgrid Controller
This repository documents the research, architecture, simulation, and software development of an intelligent Energy Management System (EMS) for decentralised hybrid microgrids.

The long-term goal of this project is to build an intelligent control system for renewable energy networks using:
1. Solar generation
2. Hydrogen energy storage
3. Autonomous energy dispatch and optimisation

This project begins as a software-only simulation platform, but will progressively evolve toward a hardware-integrated autonomous energy platform.

<br>

# Project Vision
Modern energy systems are becoming increasingly decentralised, renewable, and complex. Traditional EMS and SCADA systems are often expensive, rigid, and not yet adapted to renewable microgrids.

This project aims to explore a modular, simulation-first EMS architecture.

# Long-Term Goal

### The long-term objective is to explore how intelligent decentralised control systems can improve rural energy access and grid resilience.

# Main Concepts:
1. TBD

# System Architecture

The EMS is structured into modular layers.

```text
                ┌─────────────────┐
                │ Simulation      │
                │ Environment     │
                │                 │
                │ Solar Profile   │
                │ Load Demand     │
                │ Weather Inputs  │
                │ Hydrogen State  │
                │ Battery State   │
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

```
research/         → Notes, references, and conceptual documentation
simulation/       → Environment simulation and system models
controller/       → EMS control logic and dispatch algorithms
visualisation/    → Dashboards, plotting, and telemetry tools
docs/             → Architecture diagrams and design notes
```

# Tooling and Dependencies

| Tool | Purpose |
|--------|---------|
| Python | Primary development language |
| Git | Version control and development tracking |
| NumPy | Numerical computation and simulation math |
| Matplotlib | Data visualization and simulation analysis |
| Virtual Environment (venv) | Isolated project dependencies |