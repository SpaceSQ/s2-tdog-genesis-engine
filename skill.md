---
name: s2-tdog-genesis-engine
description: The Logic-Plane Genesis Engine for the Space2 World Model. Updates local DB states for TDOG matter compilation and Hyper-Environment simulation.
version: 2.0.0
---

# S2 TDOG & Hyper-Environment Genesis Guide

Dear Agent, you are endowed with "Genesis Authority" within the S2 World Model's logical grid. You manage the physical blueprints and environmental parameters in the local database. 

## Core Operations

### 1. Matter Compilation (`compile_matter`)
When a user requests an object generation simulation, log the blueprint into the ledger:
* `target_type`: `Type_3` (MR Fluid structural bones), `Type_2` (Haptic reality), or `Type_1` (Atomic reality).
* **Note**: You are updating the digital twin state. Downstream hardware will read this state to actuate physical generation.

### 2. Ouroboros Protocol (`decompile_matter`)
When an object is logically discarded, use this tool to update its status to "DECOMPILED" in the ledger, representing material recycling.

### 3. Hyper-Environment (`set_hyper_environment`)
To simulate extreme environments (e.g., Mars, deep ocean) in the world model:
* Update `temperature_c`, `gravity_g`, and `atmosphere_kpa` in the registry.

### 4. Safety Fuse (`emergency_cutoff`)
If external context (e.g., another system component) indicates an anomaly, invoke this tool to instantly reset the logical DB state to a safe 26℃/1G baseline, signaling the physical hardware fuse to blow.