17.04.21 ������� commit.
������� ��!
���� commit ��������� �������. � ���������� ���������� ��������� � �������� �������� �����.
�����!

MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.yandex.ru')
MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
FLASKY_MAIL_SENDER = 'Flasky Admin <k######.##@u####.ru>'

� FLASKY_MAIL_SENDER � ������� <> ������ ����������� ����� ����, ��� ���������� ������ (��� �������������� �� �����).
set FLASKY_ADMIN=l*******@yandex.ru - ������� ����� ������� ����, ��� ����� �������� �����.
���� � ������ ������ ���� ������ � ����� � ������.

����� �������� ���������� � ��������� ���������� ������:
(venv) C:\Users\������\PycharmProjects\pythonProject>set FLASK_APP=flasky.py

(venv) C:\Users\������\PycharmProjects\pythonProject>set FLASK_DEBUG=1

(venv) C:\Users\������\PycharmProjects\pythonProject>set MAIL_USE_TLS=1

(venv) C:\Users\������\PycharmProjects\pythonProject>set MAIL_USERNAME=k######.##@u####.ru

(venv) C:\Users\������\PycharmProjects\pythonProject>set MAIL_PASSWORD=...

(venv) C:\Users\������\PycharmProjects\pythonProject>set FLASKY_ADMIN=l*******@yandex.ru

(venv) C:\Users\������\PycharmProjects\pythonProject>flask run

13.04.21 ������� commit.
���������� ����������� (���������� Hello, Stranger!), ������ ��������.
�� ����� �� ������������ (yandex.ru), � ��� ������� Submit ���������� ���������.
� ������� ���� � ����� views.py � ��� ����� ����� (#...). � ���� ������� ��� �� �������� �����.
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
� ������� ���� ���� ������ app.config � send_email ����� Unresolved reference. � ������� ��� ����� ������� import
(� � �����, �� ��������������), �� ��� ��� ���� ����, ��� ����� ���� �� �������� �����������. ��� � ��� �� ���������.
 
06.04.21 ������ commit.
�������������� ���������� �� ����� �� ����� 7, �� ���������� � ��������� ��������� (��������� ��������� ������).
������ ����� ��� ����� ����������� � ��������� ������.
��� ������� ������� ���������� ����������:
- ������� ��� ����� �� ������� commit.
����� ������� �� ������������.

06.04.21 ����� commit.
�� ���������� ���������� �������� �� �����.
��� ������� ������� ���������� ����������:
- ������� ��� ����� �� ������ commit;
- ���������� ���������� flask-mail
P.s. ������ googlemail.com �������� ������������ yandex.ru

04.04.21 �������� commit.
�������� �������� � ������ ������ Flask-SQLAlchemy.
��� ������� ������� ���������� ����������:
- ������� ��� ����� �� ��������� commit;
- ���������� ���������� flask-sqlalchemy;
- ���������� ���������� flask-migrate.
P.s. ��� ������� flask shell �����:
(venv) $ set FLASK_APP=main.py
(venv) $ flask shell

22.03.21 ������ commit.
��� ������� ������� ���������� ����������:
- ������� ��� ����� � ����� �� �������� commit;
- ���������� ���������� flask-wtf.
�������, � �������� � ������� �� ������ commit, �������� ����c��������� � ��� ������, 
��� ��� ��������� ���������� ���������� � ������� ������������.
� ������ commit ���������� ��������� � ������ �����������: ������������ ���������� ������, 
� ������ ��������� � ������������.

��� ����� ������ commit.
��� ������� ������� ���������� ����������:
- ������� ��� ����� � ����� �� ������� commit; 
- ���������� ���������� flask-bootstrap;
- ���������� ���������� flask-moment.
P.s. ����� ������������ http://127.0.0.1:5000/user/<name>, ��������, http://127.0.0.1:5000/user/Eleferij