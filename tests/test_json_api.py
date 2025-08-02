import requests
from faker import Faker

fake = Faker()


def test_create_user_with_faker():
    name = fake.first_name()
    job = fake.job()
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {"name": name, "job": job}
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 201]  # more flexible


def test_get_users_list():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    # Optional: validate fields for one user
    sample_user = users[0]
    assert "name" in sample_user
    assert "email" in sample_user
