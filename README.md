# AI Customer Support Automation System

##  Overview

This project is an AI-powered customer support automation system that simulates real-world enterprise support workflows. It can detect user intent, generate automated responses, and create support tickets with priority levels.Built an AI-powered customer support automation system with ticket generation, priority classification, and real-time API deployment.

##  Features

* Intent Detection (Order, Refund, Complaint, General)
*  Automated Response Generation
*  Ticket ID Generation
*  Priority Classification (High, Medium, Low)
*  Chat-based UI using Streamlit
*  REST API using FastAPI
  

##  Architecture

User → FastAPI → AI Engine → Automation Logic → Response


## How It Works

1. User sends a message
2. AI detects intent
3. System generates:

   * Ticket ID
   * Priority
   * Response
4. Output is displayed in UI

---

##  Project Structure

```
ai-support-bot/
│
├── app/
│   ├── main.py
│   ├── ai_engine.py
│   ├── automation.py
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md


## Installation

```bash
git clone https://github.com/kvala8585-crypto/AI-Customer-Support-Automation
cd ai-support-bot
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.main:app --reload
```

## Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

##  API Endpoints

### GET /

Returns status message

### POST /chat

Request:

```json
{
  "message": "my order is delayed"
}
```

Response:

```json
{
  "intent": "ORDER_ISSUE",
  "ticket_id": "TICKET-1234",
  "priority": "Medium",
  "response": "Your order is being processed..."
}
```

##  Real-World Use Case

This system mimics real company support workflows:

* Automated ticket creation
* Priority handling
* Intelligent response system

## Tech Stack

* FastAPI
* Streamlit
* Python

## Future Improvements

* Database integration
* Admin dashboard
* Email automation
* AI model integration

##  Deployment

Deployed on Render:

* Backend API live :https://ai-customer-support-automation-1-nqxb.onrender.com

## Author
  kavi vala
