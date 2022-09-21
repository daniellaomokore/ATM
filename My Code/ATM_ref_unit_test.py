from unittest import mock
from unittest import TestCase, main
from ATM_ref import accountAccess, withdrawMoney


class test_successful_account_access(TestCase):            #it MUST start with test

    def test_correctPin(self):
        expected = True
        result = accountAccess(pin=1234)
        self.assert(expected, result)

class test_failed_account_access(TestCase):

    def test_pin2(self):
        expected = False
        result = accountAccess(pin=124)
        self.assertEqual(expected, result)

    def test_pin3(self):
        expected = False
        result = accountAccess(pin=1542)
        self.assertEqual(expected, result)


class test_successfully_withdraw(TestCase):

    def test_withdraw_50(self):
        expected = True
        result = withdrawMoney(50)
        self.assertEqual(expected, result)

    def test_withdraw_100(self):
        expected = True
        result = withdrawMoney(100)
        self.assertEqual(expected, result)


class test_unsuccessfully_withdraw(TestCase):

    def test_withdraw_111(self):
        expected = False
        result = withdrawMoney(111)
        self.assertEqual(expected, result)

    def test_withdraw_2000(self):
        expected = False
        result = withdrawMoney(2000)
        self.assertEqual(expected, result)
        
        
        
if __name__ == '__main__':
    main()




