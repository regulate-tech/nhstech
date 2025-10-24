
from lib import generate_and_save_data, run_feast_commands
import sys

if __name__ == "__main__":
    try:
        print("--- Running Data Generation ---")
        generate_and_save_data()
        
        print("\n--- Updating Feature Store ---")
        run_feast_commands()
        
        print("\n--- Process Complete ---")
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)