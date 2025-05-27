import unittest
from tax_calculators import TaxCalculator
from users import users

class TestTaxCalculations(unittest.TestCase):
    def setUp(self):
        """Set up test cases with different user scenarios"""
        self.uk_user = users["user1"]  # UK resident inheriting from Canada
        self.canada_user = users["user2"]  # Canadian resident inheriting from Canada
        
    def test_uk_user_tax_calculations(self):
        """Test tax calculations for UK resident inheriting from Canada"""
        calculator = TaxCalculator(self.uk_user)
        tax_analysis = calculator.calculate_total_tax_burden()
        
        # UK resident should pay inheritance tax
        self.assertGreater(tax_analysis["inheritance_tax"], 0)
        
        # Canadian estate should have no estate tax
        self.assertEqual(tax_analysis["estate_tax"], 0)
        
        # Should have capital gains tax
        self.assertGreater(tax_analysis["capital_gains_tax"], 0)
        
        # Total tax burden should be significant
        self.assertGreater(tax_analysis["total_tax_burden"], 0)
        
    def test_canada_user_tax_calculations(self):
        """Test tax calculations for Canadian resident inheriting from Canada"""
        calculator = TaxCalculator(self.canada_user)
        tax_analysis = calculator.calculate_total_tax_burden()
        
        # Canadian resident should not pay inheritance tax
        self.assertEqual(tax_analysis["inheritance_tax"], 0)
        
        # Canadian estate should have no estate tax
        self.assertEqual(tax_analysis["estate_tax"], 0)
        
        # Should have capital gains tax
        self.assertGreater(tax_analysis["capital_gains_tax"], 0)
        
        # Total tax burden should be lower than UK user
        self.assertLess(tax_analysis["total_tax_burden"], 
                       TaxCalculator(self.uk_user).calculate_total_tax_burden()["total_tax_burden"])

if __name__ == '__main__':
    unittest.main() 