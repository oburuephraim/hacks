import requests
import yaml
import logging
import os

# Configure logging

logging.basicConfig(level=logging.INFO)

def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found: {config_path}")
        return {}
    
    with open(config_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML file: {e}")
            return {}

def fetch_online_code(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request is successful
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching code from {url}: {e}")
        return ""

def execute_code(code: str) -> None:
    # Consider replacing exec with a safer alternative if possible
    try:
        exec(code, globals())
    except Exception as e:
        logging.error(f"Error executing code: {e}")

def main() -> None:
    config = load_config("config.yaml")
    online_code_url = config.get('online_code_url')

    if online_code_url:
        logging.info(f"Fetching code from: {online_code_url}")
        code = fetch_online_code(online_code_url)

        if code:
            logging.info(f"Executing code from: {online_code_url}")
            execute_code(code)
        else:
            logging.warning("No code fetched to execute.")
    else:
        logging.warning("No online code URL found in the configuration.")

if __name__ == "__main__":
    main()
