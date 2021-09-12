import pytest


def test_home(client):
    """
    Test the home page
    """
    response = client.get('/')
    assert response.status_code == 200


def test_about(client):
    """
    Test the about page
    """
    response = client.get('/about')
    assert response.status_code == 200


def test_contact(client):
    """
    Test the contact page
    """
    response = client.get('/contact')
    assert response.status_code == 200
