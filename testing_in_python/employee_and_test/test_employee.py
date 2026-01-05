import unittest
import employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # this method runs once before all tests
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        # this method runs once after all tests
        print("tearDownClass")

    def setUp(self):
        # this method runs before each test
        print("setUp")
        self.emp1 = employee.Employee("John", "Doe", 50000)
        self.emp2 = employee.Employee("Jane", "Smith", 60000)

    def tearDown(self):
        # this method runs after each test
        print("tearDown")
        pass

    def test_email(self):
        self.assertEqual(self.emp1.email, "john.doe@company.com")
        self.assertEqual(self.emp2.email, "jane.smith@company.com")
        self.assertNotEqual(self.emp1.email, "john_doe@company.com")

    def test_full_name(self):
        self.assertEqual(self.emp1.full_name, "John Doe")
        self.assertEqual(self.emp2.full_name, "Jane Smith")
        self.assertNotEqual(self.emp1.full_name, "JohnD")

    def test_give_raise_default(self):
        self.emp1.give_raise()
        self.emp2.give_raise()
        self.assertEqual(self.emp1.salary, 52500)
        self.assertEqual(self.emp2.salary, 63000)
        self.assertNotEqual(self.emp1.salary, 52000)
        self.assertNotEqual(self.emp2.salary, 62000)

    def test_give_raise_custom(self):
        self.emp1.give_raise(7000)
        self.emp2.give_raise(8000)
        self.assertEqual(self.emp1.salary, 57000)
        self.assertEqual(self.emp2.salary, 68000)
        self.assertNotEqual(self.emp1.salary, 56000)
        self.assertNotEqual(self.emp2.salary, 67000)

    def test_promote(self):
        self.emp1.promote("Senior Developer", 10000)
        self.emp2.promote("Lead Developer", 12000)
        self.assertEqual(self.emp1.position, "Senior Developer")
        self.assertEqual(self.emp2.position, "Lead Developer")
        self.assertEqual(self.emp1.salary, 60000)
        self.assertEqual(self.emp2.salary, 72000)
        self.assertNotEqual(self.emp1.position, "Developer")
        self.assertNotEqual(self.emp2.position, "Developer")
        self.assertNotEqual(self.emp1.salary, 59000)
        self.assertNotEqual(self.emp2.salary, 71000)


if __name__ == "__main__":
    unittest.main()
