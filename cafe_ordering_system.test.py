import unittest
import cafe_ordering_system

class TestCafeOrderingSystem(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_main_with_special_characters(self):
        with unittest.mock.patch('builtins.input') as mock_input, \
            unittest.mock.patch('builtins.print') as mock_print, \
            unittest.mock.patch('cafe_ordering_system.write_to_file') as mock_write_to_file:
            mock_input.side_effect = ["!@#$%^&*", "", "1", "Coffee"]
            cafe_ordering_system.main()
            mock_write_to_file.assert_called_once_with("!@#$%^&*", "", 15.00)
            mock_print.assert_any_call("Total Bill: R15.00")

    def test_discount_savings_display(self):
        with unittest.mock.patch('builtins.input') as mock_input, \
             unittest.mock.patch('builtins.print') as mock_print, \
             unittest.mock.patch('cafe_ordering_system.write_to_file') as mock_write_to_file:
            mock_input.side_effect = ["John", "Doe", "3", "Pizza Slice", "Burger", "Coffee"]
            cafe_ordering_system.main()
            expected_savings = 9.00  # (35 + 40 + 15) * 0.10
            mock_print.assert_any_call(f"Discount applied! You saved R{expected_savings:.2f}")
            mock_print.assert_any_call("Total Bill: R81.00")
            mock_write_to_file.assert_called_once_with("John", "Doe", 81.00)
            
                
if __name__ == '__main__':
    unittest.main()
