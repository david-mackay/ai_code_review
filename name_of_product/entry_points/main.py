import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="A basic argparse example.")
    parser.add_argument("--name", required=True, help="The name of the person.")
    parser.add_argument("--age", type=int, default=20, help="The age of the person.")
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Hello {args.name}! You are {args.age} years old.")

if __name__ == "__main__":
    main()
