# CEO Copilot: Multi-Agent Business Intelligence System

![CEO Copilot Thumbnail](https://raw.githubusercontent.com/rameenmunir06-png/CEO-Copilot-MultiAgent/main/watermarked_img_257387713597007393.png)

An enterprise-grade, automated multi-agent business intelligence ecosystem designed to ingest corporate datasets, analyze operational risks, and synthesize strategic executive-level recommendations. Built as a capstone project for the **Kaggle 5-Day AI Agents: Intensive Vibe Coding Course with Google (June 2026)**.

---

## ⚡ Core Features & Implementation

- **Multi-Agent Orchestration:** A hierarchical intelligence pipeline where specialized sub-agents report directly to an AI CEO Core.
- **Finance Agent:** Parses numerical sheets to flag financial anomalies and track monetary trends.
- **Inventory Agent:** Monitors stock levels and automatically predicts supply chain depletion points.
- **Customer Sentiment Agent:** Synthesizes qualitative reviews and customer feedback trends.
- **Automated Executive Reporting:** The CEO Agent compiles all data streams into a final structured JSON report with risk classification.

---

## 📁 Repository Structure

```text
CEO-Copilot-MultiAgent/
│
├── agents/
│   ├── finance_agent.py
│   ├── inventory_agent.py
│   ├── customer_agent.py
│   └── ceo_agent.py
│
├── data/
├── main.py
├── requirements.txt
└── README.md
---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rameenmunir06-png/CEO-Copilot-MultiAgent.git
cd CEO-Copilot-MultiAgent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root and add your Google Gemini API key.

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Project

```bash
python main.py
```

---

## 📊 System Workflow

```text
                Business Owner
                      │
                      ▼
     Upload Business Data (CSV Files)
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Finance Agent   Inventory Agent   Customer Agent
      │               │                │
      └───────────────┼────────────────┘
                      ▼
          CEO Copilot (Orchestrator)
                      │
          Cross-Agent Analysis & Reasoning
                      │
                      ▼
             Google Gemini AI Model
                      │
                      ▼
     Executive Business Insights & JSON Report
                      │
                      ▼
 Human Approval (Human-in-the-Loop) for High-Risk Actions
```

---

## ✨ Key Highlights

- 🤖 Multi-Agent Business Intelligence Architecture
- 📊 Automated Financial Analysis
- 📦 Inventory Monitoring & Low-Stock Detection
- 💬 Customer Sentiment Analysis
- 🧠 CEO Agent Cross-Department Decision Making
- ⚠️ Business Risk Classification (High / Medium / Low)
- 👤 Human-in-the-Loop Verification
- 📄 Structured Executive JSON Reports
- ⚡ Powered by Google Gemini AI

---

## 🚀 Future Improvements

- Interactive Streamlit Dashboard
- Live Database Integration (PostgreSQL / BigQuery)
- WhatsApp & Email Alert System
- Real-Time Analytics Dashboard
- Cloud Deployment
- Advanced Predictive Business Insights

---

## 🏆 Project Information

**Project Name:** CEO Copilot – Multi-Agent Business Intelligence System

**Track:** Agents for Business

**Built For:** Kaggle 5-Day AI Agents: Intensive Vibe Coding Capstone Project with Google (2026)

**Core Technologies:**
- Python
- Google Gemini API
- Pandas
- CSV Data Processing
- Multi-Agent Architecture

---

⭐ If you found this project useful, consider giving this repository a star.
Complete professional README documentation
