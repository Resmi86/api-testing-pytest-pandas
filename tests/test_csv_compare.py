import pandas as pd
import os


def test_compare_uploaded_vs_expected_csv():
    expected_path = "data/expected_users.csv"
    uploaded_path = "data/uploaded_users.csv"

    assert os.path.exists(expected_path), "Expected CSV file not found"
    assert os.path.exists(uploaded_path), "Uploaded CSV file not found"

    df_expected = pd.read_csv(expected_path)
    df_uploaded = pd.read_csv(uploaded_path)

    # Basic structural checks
    assert df_expected.shape == df_uploaded.shape, "CSV shape mismatch"
    assert list(df_expected.columns) == list(df_uploaded.columns), "CSV column names mismatch"

    # Deep data comparison
    pd.testing.assert_frame_equal(df_expected, df_uploaded, check_dtype=False)
