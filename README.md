# 🌋 S2 TDOG Genesis Engine & HLSL Lab (v2.0.0 World Model Edition)

Welcome to the dual-core material engine of the S2 Metaverse. This plugin combines the TDOG Matter Compiler with the Hyper-Limit Science Lab (HLSL) to simulate the generation of matter and extreme environments.

## 🛡️ OpenClaw Compliance & Zero-Trust Architecture
**[CRITICAL SECURITY DISCLOSURE]** To comply with OpenClaw's zero-trust sandboxing, this plugin operates STRICTLY in **Local Simulation & Logic-Control Mode**. 
1. **No Direct Hardware Actuation**: The Python handler writes physical parameters (temperature, gravity, matter state) to a local SQLite database (`s2_tdog_genesis.db`). It does NOT contain OS-level device drivers or direct network endpoints to physical 3D printers, MR Fluid arrays, or HVAC systems.
2. **Physical Execution Boundary**: Actual physical materialization and hardware safety fuse blowing require an air-gapped, downstream IoT daemon to read this database and drive the hardware.
3. **Sensor Isolation**: This plugin does not directly read biometric data (e.g., heart rate). The Agent relies on standard external context to invoke the `emergency_cutoff`.

## 🧬 Subsystem 1: The Matter Compiler (TDOG)
Implements the Theory of Dynamic Object Generation to simulate transforming spaces into "Genesis Engines."
* **MR Fluid & DE Allocation**: Simulates rapid generation of Type 2 and Type 3 objects in the world model.
* **Ouroboros Protocol**: Updates the logical ledger to recycle materials and deduct entropy taxes.

## 🧪 Subsystem 2: Hyper-Limit Science Lab (HLSL)
A high-security, "Void-Protocol" logical environment for dangerous scientific simulation.
* **Void Science Protocol**: Enforces logical constraints prohibiting Class D avatars.
* **STEM-to-Gen**: Converts standard textbooks into executable physics parameters in the DB.