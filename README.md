# 🛠️ Setup

### Create and activate a virtual environment

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure pytest

Create a `pytest.ini` file in the root directory with the following content:

```ini
[pytest]
testpaths = tests
python_files = test_*.py *_test.py
markers =
    smoke: Quick smoke tests
    regression: Full regression tests
addopts = --headed -v --html=reports/report.html --self-contained-html --maxfail=2 --reruns=2
log_cli = true
log_cli_level = INFO
```

> **Note:** You can remove or adjust `--headed`, `--maxfail`, and `--reruns` based on your preferences.

---

# 🚀 Running Tests

* Run all tests sequentially:

```bash
pytest
```

* Run tests in parallel:

```bash
pytest -n <number_of_workers>
```

* Generate HTML report:
  The report will be automatically generated in `reports/report.html` with embedded screenshots for failed tests.

---

# 🧩 Project Structure

```
project/
│
├── pages/                # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── adding_to_cart.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                # Test scripts
│   ├── test_cart.py
│   ├── test_inventory_page.py
│   └── test_full_purchase_flow.py
│
├── config/               # Config files (YAML or CSV)
│   └── test_config.yaml
│
├── reports/              # HTML test reports
├── conftest.py           # Fixtures (config, CSV readers, etc.)
├── pytest.ini            # Pytest configuration
└── requirements.txt      # Python dependencies
```

---

# 📦 Features

* **Page Object Model (POM):** Reusable page classes for clean, maintainable tests
* **Data-Driven Testing:** Products and customer data can come from YAML or CSV
* **Headed / Headless Execution:** Visual execution for debugging or CI-friendly headless mode
* **HTML Reporting:** Self-contained report with screenshots for failures
* **Parallel Execution:** Run tests faster using `pytest -n`
* **CI/CD Ready:** Can integrate with GitHub Actions or other pipelines for automatic test runs

---

# ⚡ Example Test Flow

1. Log in to SauceDemo
2. Verify products on the inventory page
3. Add items to the cart
4. Remove items from the cart
5. Proceed to checkout
6. Fill customer information and complete the purchase
7. Validate the confirmation message

---

# 💡 Notes

* Customize your configuration in `config/test_config.yaml`
* Adjust `pytest.ini` options for timeouts, reruns, and reporting as needed
* Screenshots of failed tests are automatically captured in the report
