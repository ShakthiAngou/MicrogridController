# Shakthi Energy
This repository is intended to document the work I do for the software and control systems development for Shakthi Energy. I will use this repository to plan, design, research, and develop code for the  project.

## Project Overview
HyRTS - Hydrogen-based Roof Top Solar decentralised microgrid

## Main Concepts
1. Control Systems
2. Electic Power Systems
3. Discrete Optimisation
4. Solar Energy Basics
5. Optionally: Introduction to Mathematical Optimisation

<br>

# 12-Week Development Timeline – Microgrid EMS Controller

| Week | Focus | Learning (Just-in-Time) | Build Output | Success Milestone |
|------|------|------------------------|-------------|------------------|
| 1–2 | Foundations + First Simulation | Basic control (PID, feedback), power flow, battery SOC | Python simulation: solar, load, battery SOC loop | Working simulation (even if simple/ugly) |
| 3–4 | EMS Logic (Rule-Based) | Rule-based control, system constraints | Add decision logic: battery charge/discharge, hydrogen (simulated) | Functional EMS decision engine |
| 5–6 | System Structuring | Intro optimization concepts, multi-timescale thinking | Refactor into clean modules + add logging/plots | Structured, explainable system |
| 7–9 | Intelligence + Refinement | Forecasting basics, system architecture patterns | Add forecasting + improved scheduling + cleaner architecture | “Digital twin” microgrid simulation |
| 10–12 | Hardware Integration (Optional) | Sensors, Raspberry Pi basics (just-in-time) | Connect EMS to simple hardware OR hardware-in-loop | End-to-end prototype (software + optional physical demo) |

<br>

## Week 1–2: Foundations + First Simulation

Build a basic Python simulation of a microgrid with:
- Solar input
- Load demand
- Battery SOC tracking
- Simple energy balancing logic
---

## Week 1

### Day 1: Setup + Direction - 4 April 2026
- [ DONE ] Create repo structure (research/, simulation/)
- [ DONE ] Write initial README (project goal + scope)
- [ DONE ] Create research files:
      - microgrid_basics.md
      - control_systems.md
      - battery_systems.md
      - ems_basics.md
      - hydrogen_energy_storage.md
      - system_architecture.md
      - README file for research folder

---

### Day 2: Microgrid Understanding
- [ ] Study DC microgrid basics (1–2 hrs max)
- [ ] Add to microgrid_basics.md:
      - Energy flow model
      - Power balance equation
- [ ] Draw system diagram (even rough)

---

### Day 3: Control Basics
- [ ] Start :contentReference[oaicite:0]{index=0} (first modules only)
- [ ] Learn:
      - Feedback loop
      - PID intuition (no deep math)
- [ ] Add to control_systems.md:
      - Where control applies in your system

---

### Day 4: Battery + Constraints
- [ ] Study battery SOC basics (1–2 hrs)
- [ ] Add to battery_systems.md:
      - SOC limits
      - Charging/discharging constraints

---

### Day 5: FIRST SIMULATION (start coding)
- [ ] Create simulation script (simulation/main.py)
- [ ] Define:
      - solar(t)
      - load(t)
- [ ] Write basic loop:
      - compute surplus/deficit

---

### Day 6: Add Battery Logic
- [ ] Implement battery SOC tracking
- [ ] Add:
      - charge when surplus
      - discharge when deficit

---

### Day 7: Test + Reflect
- [ ] Run simulation over time (e.g., 24h loop)
- [ ] Print/log outputs
- [ ] Write:
      - Example scenarios in microgrid_basics.md

---

## Week 2

### Day 8: Clean Simulation
- [ ] Refactor code into functions:
      - get_solar()
      - get_load()
      - update_battery()

---

### Day 9: Add Constraints
- [ ] Add:
      - battery max capacity
      - min SOC threshold
- [ ] Handle edge cases:
      - battery full
      - battery empty

---

### Day 10: Introduce Hydrogen (SIMULATED)
- [ ] Add:
      - hydrogen storage variable
- [ ] Logic:
      - excess → hydrogen
      - deficit → use hydrogen

---

### Day 11: EMS Decision Logic
- [ ] Replace raw logic with structured rules:
      - priority-based decisions
- [ ] Document in ems_overview.md

---

### Day 12: Visualization
- [ ] Plot:
      - solar vs load
      - battery SOC over time
- [ ] Use matplotlib

---

### Day 13: Scenario Testing
- [ ] Test:
      - high solar, low load
      - low solar, high load
      - battery edge cases
- [ ] Observe behavior

---

### Day 14: Consolidation
- [ ] Clean code structure
- [ ] Update all research docs
- [ ] Write summary:
      - "How my EMS currently works"
