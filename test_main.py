'''
Tests for jwt flask app.
'''
import main
import os
import json
import pytest

SECRET = 'patience'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjM0NDk0MzEsIm5iZiI6MTY2MjIzOTgzMSwiZW1haWwiOiJoZW5yeWNvZGUxMHhAZ21haWwuY29tIn0.c0bCu1PHV2YKA0AUhI6KcOtft0BM09UiGmMo1_GvG5s'
EMAIL = 'henrycode10x@gmail.com'
PASSWORD = 'rabbiIstheGreatest'


@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client


def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth',
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
    # assert False
