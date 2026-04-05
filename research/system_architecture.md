# System Design
Date: 17 April 2026

**Architecture:**

```
   EMS
    |
    V
High-level commands
    |
    V
Firmware (Low-level, real-time)
    | execute
    V
Microcontroller Unit (Hardware)
```

**MVP Goal:** EMS Simulation + High-level Logic

A protoype EMS that is fed simulated sensor data and will output control decisions (power setpoints / state changes) for solar and hydrogen components, including transparent threshold logic and logging.

**Long-term Goal:** EMS -> MCU Interface

EMS-MCU interface that will connect EMS decision-making with embedded device controllers for the microgrid.






