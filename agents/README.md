# CEO Copilot - Multi-Agent Business Automation System

CEO Copilot is an advanced multi-agent system designed to automate business intelligence and financial reporting. Powered by Gemini, the system utilizes specialized AI agents that coordinate seamlessly to ingest multi-departmental data and generate structured executive reports.

## Architecture Diagram

```text
Finance CSV     ──► Finance Agent    ──┐
                                       │
Inventory CSV   ─► Inventory Agent   ├──► CEO Agent ──► Gemini ──► Final JSON Report
                                       │
Reviews CSV     ───► Customer Agent  ──┘