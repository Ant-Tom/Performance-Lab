import json
import sys

def fill_report(tests_path, values_path, report_path):
  
  with open("tests.json") as f:
    tests_data = json.load(f)

  with open("values.json") as f:
    values_data = json.load(f)


  def fill_values(data, values):
    if "id" in data and data["id"] in values:
      data["value"] = values[data["id"]]

    for title in data.get("title", []):
      fill_values(title, values)

  fill_values(tests_data, values_data)

  with open("report.json", "w") as f:
    json.dump(tests_data, f, indent=2)


if __name__ == "__main__":
  tests_path, values_path, report_path = sys.argv[1:]

  fill_report(tests_path, values_path, report_path)

  print(f"Файл {report_path} успешно сформирован.")
