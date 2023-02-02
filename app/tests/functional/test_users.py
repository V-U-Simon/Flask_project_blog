from flask import url_for
import pytest
# from app import db, login
from app.models import User


def test_list_users(client, users):
    """
    GIVEN sequence of users: Simple, Staff, Author users
    WHEN get the list users page (GET)
    THEN check that all users can take access
    """
    for user in users:
        response = client.get(url_for("user.list"))
        assert response.status_code == 200
        assert user.username in response.text


def test_profile_users(client, users, set_user_as_auth, set_user_as_logut):
    """
    GIVEN sequence of users: Simple, Staff, Author users
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    for user in users:
        
        set_user_as_auth(user)
        response = client.get(url_for("user.profile", id=user.id))
        assert response.status_code == 200
        assert user.username in response.text
        
        set_user_as_logut()
        response = client.get(url_for("user.profile", id=user.id))
        assert response.status_code == 302
        

pytest.mark.xfail(strict=True)
def test_login_and_logout(client, users: list[User], set_user_as_logut):
    """
    GIVEN sequence of users: Simple, Staff, Author users
    WHEN user try to get to the page of login (GET) then login (POST) and logout (POST)
    THEN check the response is valid
    """
    for user in users:     
        # todo: why user is authenticated and is't anonymous?
        set_user_as_logut()
        response = client.get(url_for("user.logout"))
        assert user.is_authenticated == False
        assert user.is_anonymous == True


        response = client.get(url_for("user.login", id=user.id))
        print(response.location)
        assert response.status_code == 200
        assert 'Username' in response.text
        assert 'Password' in response.text
        assert 'Remember Me' in response.text 

        response = client.post(
            url_for("user.login", id=user.id),
            data=dict(username=user.username, password="passwd"),
            follow_redirects=True,
        )
        assert response.status_code == 200 
        assert user.username in response.text
        assert response.request.path == url_for("user.profile", id=user.id)
        assert user.is_authenticated == True
        assert user.is_anonymous == False

        set_user_as_logut()
        response = client.get(url_for("user.logout"))
       
        
pytest.mark.skip()
def test_update_user(client, users: list[User], set_user_as_auth, set_user_as_logut):
    pass
    # todo
    # for user in users:
        
    #     set_user_as_auth(user)
    #     response = client.post(
    #         url_for("user.update", id=user.id),
    #         data=dict(username=user.username, password="passwd"),
    #         follow_redirects=True,
    #     )
        
        
    #     response = client.get(url_for("user.profile", id=user.id))
    #     assert response.status_code == 200
    #     assert user.username in response.text
        
    #     set_user_as_logut()
    #     response = client.get(url_for("user.profile", id=user.id))
    #     assert response.status_code == 302


