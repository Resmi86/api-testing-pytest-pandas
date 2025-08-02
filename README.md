# 🧪 REST API Testing Framework (with Pytest, Faker, Pandas, HTML Reports)

A simple yet powerful API testing project that validates CSV data generation and performs REST API POST operations using Pytest.

---

## 🔧 Features

- ✅ REST API testing using `requests`
- ✅ Dynamic test data generation with `faker`
- ✅ CSV file creation and validation using `pandas`
- ✅ HTML reporting via `pytest-html`
- ✅ Pre-test setup automation with `pytest fixtures`
- ✅ File structure designed for real-world test frameworks

---

## 📁 Project Structure
RESTAPI/
├── data/ # ✅ Generated CSV files
│ ├── expected_users.csv
│ └── uploaded_users.csv
│
├── reports/ # ✅ HTML report output
│ └── report.html
│
├── tests/
│ ├── conftest.py # ⚙️ Auto-generates fake users before test run
│ ├── test_csv_compare.py # 📑 Compares expected vs uploaded CSV data
│ ├── test_csv_validation.py # ✅ Validates email format and CSV structure
│ └── test_json_api.py # 🌐 POST user API test using Faker
│
├── generate_fake_csv.py # 🔁 Generates expected and uploaded users
├── requirements.txt
└── README.md


---
yaml

## ▶️ How to Run Tests with HTML Report

1. **Install dependencies**:

```bash
pip install -r requirements.txt

2. Run tests with report:

pytest tests/ --html=reports/report.html --self-contained-html

✅ This will:

Automatically generate CSVs before testing
Validate the files
Test API
Save a test report to reports/report.html

💡 Technologies Used

| Module        | Purpose                          |
| ------------- | -------------------------------- |
| `pytest`      | Test runner                      |
| `faker`       | Random fake data generation      |
| `pandas`      | CSV file creation and validation |
| `requests`    | API calls                        |
| `pytest-html` | Clean test reporting             |
| `importlib`   | Dynamic module loading           |

📌 Sample Test Highlights
CSV header and format validation
Email format checks
Automated POST request with dynamic name/job
Test comparison between two generated CSVs

📎 Requirements
Python 3.7+
pip install -r requirements.txt

📷 Sample Report Screenshot
📍 After running the command, open:
reports/report.html
To view the result in a browser.

👤 Author
Resmi Kurup
📌 Manual + Automation Tester
📌 Skilled in API testing, Pytest, Pandas
📌 Passionate about writing clean and modular test suites
