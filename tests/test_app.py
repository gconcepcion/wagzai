import logging as log
import os
import sys
import unittest

from wagzai.wagz import app

# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestApp(unittest.TestCase):
    def setUp(self):
        self.wzapp = app.test_client()

    def test_home(self):
        result = self.wzapp.get("/")
        self.assertEqual(result.status_code, 200)

    def test_chat(self):
        result = self.wzapp.post("/chat", data={"message": "Tell me about dogs"})
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Dogs are loyal and friendly.", result.data)


if __name__ == "__main__":
    unittest.main()
