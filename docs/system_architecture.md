# System Design

**Basic HyRTS Architecture:**
```
Solar PV
    |
    +--> Direct Load Supply
    |
    +--> Short-Term Storage (Supercapacitor)
    |
    +--> Long-Term Storage (Hydrogen System)
```

### Short-Term Energy Storage Layer
Supercapacitor: Absords short-duration surpluses and supplies short-duration deficits
- fast charging/discharging
- transient response

### Long-Term Energy Storage Layer
```
Solar
  ↓
Electrolyser
  ↓
Hydrogen Storage
  ↓
Fuel Cell
  ↓
Electricity
```

# Overall Architecture
```
Generation Layer
├── Solar PV

Load Layer
├── Residential Loads

Short-Term Storage Layer
├── Supercapacitor Bank

Long-Term Storage Layer
├── Electrolyser
├── Hydrogen Storage
└── Fuel Cell

EMS Controller
├── Energy Dispatch Logic
├── Storage Management
└── System Optimization
```

**MVP Goal:** EMS Simulation + High-level Logic

A protoype EMS that is fed simulated sensor data and will output control decisions (power setpoints / state changes) for solar and hydrogen components, including transparent threshold logic and logging.

# EMS Architecture

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
                │ STS State       │
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




