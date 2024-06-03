import hashlib
import argparse
from datetime import datetime

def generate_secret_string(input_string):
    """Generate a random one-way secret string of a given length."""
    hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
    return hashed_string

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--niu", type=str, help="Input from --niu parameter")
    args = parser.parse_args()
    
    # Check if --niu parameter is provided
    if args.niu is None:
        print("Error: No --niu parameter provided.")
    elif len(args.niu) != 6:
        print("Error: Unsupported NIU")
    else:
        # Get the input from --niu parameter
        input_value = args.niu

        # Convert the input to a string representation
        input_string = str(input_value)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Hash the input string using SHA-256 algorithm
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        # Get the current date and time

        # Append timestamp to the hashed string
        hashed_string_with_timestamp = hashed_string + timestamp

        # Print the hashed string
        print("Secret String:", hashed_string_with_timestamp)

if __name__ == '__main__':
    main()
