import pandas as pd
from faker import Faker
import os
fake = Faker()


def generate_fake_users_csv(count=10, save_dir="data"):
    users = []
    for i in range(1, count + 1):
        users.append({
            "id": i,
            "username": fake.user_name(),
            "email": fake.email()
        })

    df = pd.DataFrame(users)
    os.makedirs(save_dir, exist_ok=True)

    uploaded_path = os.path.join(save_dir, "uploaded_users.csv")
    expected_path = os.path.join(save_dir, "expected_users.csv")

    df.to_csv(uploaded_path, index=False)
    df.to_csv(expected_path, index=False)

    print(f"✅ uploaded_users.csv and expected_users.csv created in {save_dir}")
