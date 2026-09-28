"""Работа с CSV и JSON."""
import csv
import json
import pandas as pd

def csv_to_json(csv_path, json_path):
    df = pd.read_csv(csv_path)
    df.to_json(json_path, orient="records", indent=2, force_ascii=False)

def json_to_csv(json_path, csv_path):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)

def validate_json(data, schema):
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"Отсутствует ключ: {key}")
        elif not isinstance(data[key], expected_type):
            errors.append(f"{key}: ожидался {expected_type.__name__}")
    return errors

if __name__ == "__main__":
    # CSV → JSON
    with open("input.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age"])
        writer.writerow([1, "Alice", 30])
        writer.writerow([2, "Bob", 25])
    csv_to_json("input.csv", "output.json")

    # JSON → CSV
    json_to_csv("output.json", "output.csv")

    # Валидация
    sample = {"id": 1, "name": "Alice", "age": 30}
    schema = {"id": int, "name": str, "age": int}
    print("Ошибки:", validate_json(sample, schema))
