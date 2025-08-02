import pytest
import importlib.util
import os

# Get full path to generate_fake_csv.py
GENERATOR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generate_fake_csv.py'))

# Load the generator module manually
spec = importlib.util.spec_from_file_location("generate_fake_csv", GENERATOR_PATH)
generate_fake_csv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_fake_csv)

generate_fake_users_csv = generate_fake_csv.generate_fake_users_csv


@pytest.fixture(scope="session", autouse=True)
def generate_csv_before_tests():
    print("🔄 Generating fresh CSV files before running tests...")
    generate_fake_users_csv(count=10, save_dir="data")
