from google import genai
import os
import subprocess
import time # Add this at the top with your other imports

# Confiure the new Client
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
# We are in /script, so we look u"up and out" to /terraform
def run_security_scan():
    result = subprocess.run(['checkov', '-d', '../terraform', '--quiet'], capture_output=True, text=True)
    if not result.stdout.strip():
        raise RuntimeError(f"Checkov returned no output. stderr: {result.stderr}")
    return result.stdout

def generate_ai_report(scan_results):
    prompt = f"Analyze these security results: {scan_results}"
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⚠️ AI Quota Exceeded. Please wait 60 seconds before retrying."
        else:
            return f"❌ An unexpected error occurred: {e}"
        
    # --- EXECUTION FLOW ---
print("🔍 Starting AI Security Audit...")

# 1. Run the scan and store the result (The missing piece!)
scan_data = run_security_scan()

# 2. Pass that data to the AI
report = generate_ai_report(scan_data)

print("\n--- AI EXECUTIVE SUMMARY ---")
print(report)