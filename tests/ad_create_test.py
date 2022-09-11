import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):

    expected_response = {
        "id": user.id,
        "image": None,
        "name": "Test123456",
        "price": 1234,
        "author": user.username,
        "category": category.name,
        "is_published": False,
        "description": "Test description"
    }

    data = {
        "author_id": user.id,
        "name": "Test123456",
        "price": 1234,
        "description": "Test description",
        "is_published": False,
        "category_id": category.id
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response

