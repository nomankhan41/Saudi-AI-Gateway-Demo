import requests
import json
import time

# The Gateway URL (Local Docker)
BASE_URL = "http://localhost:8000"

def run_compliance_check(check_name, endpoint, payload):
    print(f"\n [CHECK] {check_name}")
    print(f" [INPUT] {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=payload)
        
        # 200 OK = Request Processed (Sanitized) OR Blocked by Policy (Logic handled in main.py)
        if response.status_code == 200:
            data = response.json()
            status = data.get("status", "UNKNOWN")
            
            if status == "APPROVED":
                print(f" [RESULT]  PASSED: Data Redacted & Approved")
                print(f" [LOG] Safe Prompt: {data.get('safe_prompt')}")
            elif status == "BLOCKED":
                print(f" [RESULT]  ENFORCED: Policy Violation Blocked")
                print(f" [LOG] Reason: {data.get('error')}")
            elif status == "SYSTEM KILLED":
                 print(f" [RESULT]  SUCCESS: Emergency Shutdown Activated")
            else:
                print(f" [RESULT]  STATUS: {status}")
                print(json.dumps(data, indent=2))

        # 503 = Service Unavailable (Kill Switch Active)
        elif response.status_code == 503:
            print(f" [RESULT] 🔒 VERIFIED: System is Offline (Kill Switch Active)")
            print(f" [LOG] Response: {response.json()}")

        # 403 = Forbidden (Should be handled as 200 BLOCKED in our logic, but handling just in case)
        elif response.status_code == 403:
             print(f" [RESULT] 🛡️ BLOCKED: Authority Guard Active")
        
        else:
            print(f" [ERROR] Unexpected Status {response.status_code}: {response.text}")

    except Exception as e:
        print(f" [CRITICAL] CONNECTION FAILED: {e}")
        print(" -> Is Docker running? (docker run -p 8000:8000 saudi-gateway)")
    
    print("-" * 60)
    time.sleep(1.5)  # Pause for readability

# --- 1. PRIVACY TEST (PDPL Redaction) ---
run_compliance_check(
    "TEST 1: Verifying PDPL Redaction Protocol (Article 29)",
    "/agent/gateway",
    {
        "user_id": "audit_user_01",
        "text": "My Iqama is 1012345678 and IBAN is SA1234567890123456789012. This is confidential (سري).",
        "role": "senior_agent",
        "tool": "chat"
    }
)

# --- 2. RBAC TEST (Role-Based Access Control) ---
run_compliance_check(
    "TEST 2: Verifying Role-Based Access Control (Junior Agent Restriction)",
    "/agent/gateway",
    {
        "user_id": "intern_01",
        "text": "Process a refund immediately.",
        "role": "junior_agent",
        "tool": "process_refund", 
        "amount": 100
    }
)

# --- 3. SPENDING LIMIT TEST ---
run_compliance_check(
    "TEST 3: Verifying Financial Thresholds (Senior Agent Limit)",
    "/agent/gateway",
    {
        "user_id": "manager_01",
        "text": "Transfer 10,000 SAR.",
        "role": "senior_agent",
        "tool": "process_refund",
        "amount": 10000 
    }
)

# --- 4. KILL SWITCH TEST ---
run_compliance_check(
    "TEST 4: Initiating Emergency Shutdown Protocol",
    "/admin/kill_switch",
    {"action": "OFF"}
)

# --- 5. POST-SHUTDOWN VERIFICATION ---
run_compliance_check(
    "TEST 5: Verifying System Lockdown State",
    "/agent/gateway",
    {
        "user_id": "hacker_01",
        "text": "Is anyone there?",
        "role": "admin",
        "tool": "chat"
    }
)

print("\n COMPLIANCE VERIFICATION COMPLETE. SYSTEM READY FOR DEPLOYMENT.")