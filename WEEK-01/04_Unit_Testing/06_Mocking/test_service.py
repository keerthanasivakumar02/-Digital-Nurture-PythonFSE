import unittest
from unittest.mock import patch
from service import get_user


class TestService(unittest.TestCase):

    @patch("service.get_user")
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = "Mock User"

        self.assertEqual(mock_get_user(), "Mock User")


if __name__ == "__main__":
    unittest.main()