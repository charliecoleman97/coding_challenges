"""
Employee class tests.
"""

import unittest
from employee import Employee

NAME:str = "Kevin"
EMPLOYEE_ID: int = 12345

class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute payout method of the Employee class"""

    def setUp(self):
        """Set up the test fixtures"""
        self.kevin = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_a_float(self):
        """Whether payout returns a float"""
        self.assertIsInstance(self.kevin.compute_payout(), float)

    def test_employee_payout_no_commission_no_hours(self):
        """Tests whether payout is computed correctly with no comission and no hours"""
        self.assertAlmostEqual(self.kevin.compute_payout(), 1000.0)

    def test_employee_payout_no_comission(self):
        """Tests whether employee payout is calculated correctly in case of no comission and 10 hours worked"""
        self.kevin.hours_worked = 10.0
        self.assertAlmostEqual(self.kevin.compute_payout(), 2000.0)

    def test_employee_payout_with_comission(self):
        """Whether payout is correctly computed in case of 10 contracts landed and 10 hours worked"""
        self.kevin.hours_worked = 10.0
        self.kevin.contracts_landed = 10
        self.assertAlmostEqual(self.kevin.compute_payout(), 3000.0)

    def test_employee_payout_comission_disabled(self):
        """Whether payout is correctly computed in case of 10 contracts landed and 10 hours worked, 
        but comission is diabled """
        self.kevin.hours_worked = 10.0
        self.kevin.contracts_landed = 10
        self.kevin.has_commission = False
        self.assertAlmostEqual(self.kevin.compute_payout(), 2000.0)



if __name__ == "__main__":
    unittest.main()