import unittest
from server import Server
from main import Client



class TestServer(unittest.TestCase):
    """Unit tests for the server"""

    def setUp(self):
        """getting ready for tests"""
        self.server = Server()

    def test_encoding(self):
        """testing encoding"""
        self.assertEqual(
            self.server.encode(
                '"""Server side, where code is encoding all the line in one symbol'
            ),
            b"\x01\n",
        )

    def test_decoding(self):
        """testing decoding"""
        self.assertEqual(
            self.server.decode(""),
            b'"""Server side, where code is encoding all the line in one symbol\n',
        )


if __name__ == "__main__":
    unittest.main()
