import unittest

from wagzai import nlp


class TestNLP(unittest.TestCase):
    def test_process_query_dog(self):
        self.assertEqual(
            nlp.process_query("Tell me about dogs"),
            "Dogs are loyal and friendly. They need regular exercise and a balanced diet.",
        )

    def test_process_query_cat(self):
        self.assertEqual(
            nlp.process_query("Tell me about cats"),
            "Cats are independent and curious. They need a clean litter box and regular vet checkups.",
        )


if __name__ == "__main__":
    unittest.main()
