import json

exam_results = []

with open("students.json", "r") as f:
    data = json.load(f)

    for item in data:
        if item["marks"] < 50:
            result = "fail"
        else:
            result = "pass"

        stu_result = {
            "name": item["name"],
            "age": item["age"],
            "marks": item["marks"],
            "result": result
        }

        exam_results.append(stu_result)

with open("results.json", "w") as f:
    json.dump(exam_results, f, indent=4)

print("Results saved successfully!")