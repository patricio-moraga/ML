import requests
import time

max_retries = 30
for i in range(max_retries):
    try:
        response = requests.get("http://api:8000/predict")
        if response.status_code == 200:
            print("API is ready. Running tests...")
            break
    except requests.exceptions.ConnectionError:
        print(f"Waiting for API... Attempt {i+1}/{max_retries}")
        time.sleep(1)
else:
    print("API did not become ready. Exiting.")
    exit(1)
