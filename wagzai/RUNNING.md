<img src="assets/images/wagzai.webp" width="400" height="400" ="center"/>

Wagzai
=====

This is a simple Flask application for managing tasks.

Requirements
------------

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-WTF
* SQLite

Getting Started
---------------

1. Clone the repository:
```bash
$ git clone https://github.com/gconcepcion/wagzai.git
$ cd wagzai
```
2. Create a virtual environment and activate it:
```
$ python3 -m venv venv
$ source venv/bin/activate # On Windows, use "venv\Scripts\activate"
```
3. Install the dependencies:
```
(myapp) $ pip install -r requirements.txt
```
4. Run the application:
```
(myapp) $ flask run
```
5. Open your browser and go to `http://localhost:5000`.

6. Log in with the following credentials:

   * Username: user@example.com
   * Password: password

7. To create a new user, register from the login page.

Testing
-------

To run tests, use the following command:
```
(myapp) $ pytest
```
Contributing
------------

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
-------

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
