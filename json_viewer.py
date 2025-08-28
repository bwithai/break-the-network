import json
from pprint import pprint


def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def show_keys(data):
    """Show all top-level keys in the JSON."""
    if isinstance(data, dict):
        print("\nAvailable keys:")
        for i, key in enumerate(data.keys(), start=1):
            print(f"{i}. {key}")
        return list(data.keys())
    else:
        print("JSON root is not an object (dict).")
        return []


def explore_key(data, key):
    """Show the content of a selected key, parsing inner JSON if needed."""
    value = data.get(key, None)
    if value is None:
        print(f"❌ Key '{key}' not found.")
        return

    # Try parsing if it's a JSON string
    parsed_value = try_parse_json(value)

    print(f"\n📌 Data for key: '{key}'")
    if isinstance(parsed_value, (dict, list)):
        print(json.dumps(parsed_value, indent=4, ensure_ascii=False))
    else:
        print(parsed_value)


def try_parse_json(value):
    """Try to parse a string as JSON, return original if not possible."""
    if isinstance(value, str):
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value
    return value


def main():
    filename = "output.json"  # your saved file
    data = load_json(filename)

    keys = show_keys(data)
    if not keys:
        return

    while True:
        choice = input("\nEnter key name (or number), or 'q' to quit: ").strip()

        if choice.lower() == "q":
            break

        # If user enters number, map it to key
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(keys):
                explore_key(data, keys[idx])
            else:
                print("❌ Invalid choice.")
        else:
            # Treat input as key string
            explore_key(data, choice)


if __name__ == "__main__":
    main()
