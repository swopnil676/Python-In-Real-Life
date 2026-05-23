# Simple Log Analyzer

logs = [
    "INFO User logged in",
    "ERROR Database failed",
    "INFO request received",
    "ERROR timeout"
]

error_count = 0

for log in logs:
    if "ERROR" in log:
        error_count += 1

print("Total Error :", error_count)