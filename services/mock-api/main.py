from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import datetime
import uuid

app = FastAPI(title="AI Incident Commander Mock API")

# In-memory database
state = {
    "services": [
        {"id": "api-gateway", "status": "operational", "health": 100},
        {"id": "auth-service", "status": "operational", "health": 100},
        {"id": "payments-service", "status": "degraded", "health": 40},
        {"id": "notification-service", "status": "operational", "health": 100},
        {"id": "postgres-db", "status": "operational", "health": 95},
    ],
    "alerts": [
        {
            "id": str(uuid.uuid4()),
            "service": "payments-service",
            "severity": "critical",
            "message": "High error rate (5xx) detected in payment processing",
            "timestamp": datetime.datetime.now().isoformat()
        }
    ],
    "incidents": []
}

class ActionRequest(BaseModel):
    service_id: str
    action: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/services")
def get_services():
    return state["services"]

@app.get("/alerts")
def get_alerts():
    return state["alerts"]

@app.get("/incidents")
def get_incidents():
    return state["incidents"]

@app.post("/simulate/action")
def perform_action(req: ActionRequest):
    service = next((s for s in state["services"] if s["id"] == req.service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    if req.action == "restart":
        service["status"] = "operational"
        service["health"] = 100
        # Clear alerts for this service
        state["alerts"] = [a for a in state["alerts"] if a["service"] != req.service_id]
        return {"message": f"Service {req.service_id} restarted successfully"}
    
    elif req.action == "rollback":
        service["status"] = "operational"
        service["health"] = 100
        return {"message": f"Service {req.service_id} rolled back to previous version"}
    
    raise HTTPException(status_code=400, detail="Unknown action")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
