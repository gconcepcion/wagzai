import logging
import os
import unittest

from flask import Flask, jsonify, session, url_for
from flask_login import current_user, login_user, logout_user
from flask_migrate import Migrate

from wagzai.app import create_app
from wagzai.extensions import db, login_manager
from wagzai.forms import LoginForm, RegistrationForm
from wagzai.models import User

logging.basicConfig(level=logging.DEBUG)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["WAGZAI_DB_TEST_NAME"] = "test_database"
        self.client = self.app.test_client()

        #        db.init_app(app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # db.session.remove()
            # db.drop_all()
            db.session.rollback()

    #   db.drop_all()

    def test_home_page(self):
        with self.app.app_context():
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        logging.info("test_login")
        with self.app.app_context():
            # db.session.rollback()  # Ensure no existing user session before testing
            response = self.client.get("/login")  # Test the login page initially
            assert (
                b"Login" in response.data
            )  # Make sure we see "Login" on the initial request

            # Perform login with valid credentials
            response = self.client.post(
                "/login",
                data={"email": "test@example.com", "password": "test"},
                follow_redirects=True,
            )
            self.assertIn(
                b"Im", response.data
            )  # Ensure we see the success flash message

        #   self.assertTrue(self.client.get('logaoege_in'))  # Ensure session contains 'logged_in' flag

        #  logging.info(response)
        # assert b'ImOut' in response.data  # Check that we are redirected to the correct page after login (assuming you have a '/welcome' route)

    def test_invalid_login(self):
        response = self.client.post(
            "/login", data={"email": "test@example.com", "password": "wrong_password"}
        )

        self.assertNotIn(
            b"Login unsuccessful. Please check your email and password.", response.data
        )


if __name__ == "__main__":
    unittest.main()
