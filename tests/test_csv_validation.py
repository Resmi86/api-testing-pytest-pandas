import pandas as pd
import os


def test_csv_format_and_values():
    filepath = "data/uploaded_users.csv"
    assert os.path.exists(filepath), "Uploaded CSV file not found"

    df_uploaded = pd.read_csv(filepath)
    df_uploaded.columns = df_uploaded.columns.str.strip()

    assert "username" in df_uploaded.columns
    assert "email" in df_uploaded.columns
    assert df_uploaded.shape[0] > 0

    for email in df_uploaded["email"]:
        assert "@" in email and "." in email
