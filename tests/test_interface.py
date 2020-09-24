
import random
from unittest.main import main
import requests
import time

import unittest

class TestInteface(unittest.TestCase):
    
    def test_interface(self):

        secret = random.randint(0, 10000)    
        requests.post(f'http://myserver:9999/{secret}')
        time.sleep(1)
        r = requests.get(f'http://myclient:9998/')
        self.assertEqual(secret, int(r.content))
        
    def test_failure(self):

        raise Exception()
    

if __name__ == "__main__":
    test = TestInteface()
    test.test_interface()
