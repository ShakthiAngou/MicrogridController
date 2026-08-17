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
