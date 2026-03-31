## [2.0.0] - 2026-03-30
### 🛡️ Security & Architecture Clarity (World Model Integration)
- **Zero-Trust Boundary Definition**: Explicitly documented the architectural separation between the Logical Control Plane (this plugin) and the Physical Data Plane (downstream IoT actuators).
- **Handler Returns Overhaul**: Updated all `handler.py` outputs to explicitly state `[Logic Plane Updated]` and `[Boundary Notice]`, ensuring Agents understand they are modifying database state, not directly triggering physical high-voltage or bio-atomic hardware.
- **Agent Instruction Constraint**: Revised `skill.md` to remove implications of direct hardware or biometric sensor access, aligning instructions with the true capabilities of the local SQLite simulation.
- **License Update**: Transitioned to MIT license for broader AGI ecosystem adoption.