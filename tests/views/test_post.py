import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_views(cliente):
    url = reverse('home')
    response = cliente.get(url)
    assert response.status_code == 200
