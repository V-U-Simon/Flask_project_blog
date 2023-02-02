
# from flask import url_for
# from app import db
# from app.models import Article


# def test_list(client, articles: db.Query):
#     article = articles.first()
    
#     response = client.get(url_for('article.list'))
#     assert response.status_code == 200
#     assert article.title in response.text


# # def test_detail(client, article:Article):
# #     response = client.get(url_for('article.detail', id=article.id))
# #     assert response.status_code == 200
# #     assert article.title in response.text




    
    
#     # assert client.get(url_for('main.main_page')).status_code == 302
#     # assert client.get('/').status_code == 302
#     # response = client.get(url_for('article.list'))
#     # assert response.status_code == 200
#     # assert 'article list' in response.text



# # def test_user_pages(client):
# #     """
# #     GIVEN a Flask application
# #     WHEN the '/' page is requested (GET)
# #     THEN check the response is valid
# #     """
    
# #     response = client.get
#     # assert response.status_code == 302
#     # assert client.get(url_for('myview')).status_code == 200    
    
#     # response = test_client.get('/articles')
#     # response = test_client.get('/')
#     # # response = client.get(url_for('main.index'))
#     # assert response.status_code == 200

#     # response = test_client.get(url_for('article.article_detail'))
#     # assert response.status_code == 200
#     # response = test_client.get(url_for('article.detail'))
#     # assert response.status_code == 200
    
    
# # def test_valid_login_logout(test_client, init_database):
# #     """
# #     GIVEN a Flask application
# #     WHEN the '/login' page is posted to (POST)
# #     THEN check the response is valid
# #     """
# #     response = test_client.post('/login',
# #                                 data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
# #                                 follow_redirects=True)
# #     assert response.status_code == 200
# #     assert b"Thanks for logging in, patkennedy79@gmail.com!" in response.data
# #     assert b"Welcome patkennedy79@gmail.com!" in response.data
# #     assert b"Flask User Management" in response.data
# #     assert b"Logout" in response.data
# #     assert b"Login" not in response.data
# #     assert b"Register" not in response.data
 
# #     """
# #     GIVEN a Flask application
# #     WHEN the '/logout' page is requested (GET)
# #     THEN check the response is valid
# #     """
# #     response = test_client.get('/logout', follow_redirects=True)
# #     assert response.status_code == 200
# #     assert b"Goodbye!" in response.data
# #     assert b"Flask User Management" in response.data
# #     assert b"Logout" not in response.data
# #     assert b"Login" in response.data
# #     assert b"Register" in response.data
