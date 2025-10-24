# In train_model.py

from lib import train_and_save_model
import sys

if __name__ == "__main__":
    try:
        print("--- Running Model Training ---")
        train_and_save_model()
        print("\n--- Process Complete ---")
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)