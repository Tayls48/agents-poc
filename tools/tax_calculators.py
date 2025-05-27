from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class TaxRates:
    """Tax rates for different jurisdictions"""
    INHERITANCE_TAX_RATES = {
        "United Kingdom": 0.40,  # 40% for UK
        "United States": 0.40,   # 40% for US
        "Canada": 0.00,         # No inheritance tax in Canada
        "Australia": 0.00       # No inheritance tax in Australia
    }
    
    ESTATE_TAX_RATES = {
        "United Kingdom": 0.40,  # 40% for UK
        "United States": 0.40,   # 40% for US
        "Canada": 0.00,         # No estate tax in Canada
        "Australia": 0.00       # No estate tax in Australia
    }
    
    CAPITAL_GAINS_RATES = {
        "United Kingdom": 0.20,  # 20% for UK
        "United States": 0.15,   # 15% for US
        "Canada": 0.15,         # 15% for Canada
        "Australia": 0.15       # 15% for Australia
    }

class TaxCalculator:
    def __init__(self, user_data: Dict[str, Any]):
        """
        Initialize the tax calculator with user data.
        
        Args:
            user_data (Dict[str, Any]): User data including location and estate information
        """
        self.user_data = user_data
        self.estate = user_data.get('estate', {})
        self.user_country = user_data['user_location']['country']
        self.parents_country = user_data['parents_location']['country']
        
    def calculate_capital_gains(self) -> tuple[float, str]:
        """
        Calculate capital gains tax on assets.
        
        Returns:
            tuple[float, str]: (tax_amount, description)
        """
        total_gains = 0
        gains_breakdown = []
        
        for asset_name, asset in self.estate.get('assets', {}).items():
            gain = asset['value'] - asset['purchase_price']
            if gain > 0:
                total_gains += gain
                gains_breakdown.append(f"{asset_name}: ${gain:,.2f}")
        
        rate = TaxRates.CAPITAL_GAINS_RATES.get(self.parents_country, 0.15)
        tax_amount = total_gains * rate
        
        description = (
            f"Capital gains tax of {rate*100}% on ${total_gains:,.2f} "
            f"in {self.parents_country}. Breakdown: {', '.join(gains_breakdown)}"
        )
        
        return tax_amount, description
        
    def calculate_inheritance_tax(self) -> tuple[float, str]:
        """
        Calculate inheritance tax based on user's location.
        
        Returns:
            tuple[float, str]: (tax_amount, description)
        """
        rate = TaxRates.INHERITANCE_TAX_RATES.get(self.user_country, 0.00)
        tax_amount = self.estate.get('total_value', 0) * rate
        
        description = (
            f"Inheritance tax of {rate*100}% based on {self.user_country} rates. "
            f"Total estate value: ${self.estate.get('total_value', 0):,.2f}"
        )
        
        return tax_amount, description
        
    def calculate_estate_tax(self) -> tuple[float, str]:
        """
        Calculate estate tax based on parents' location.
        
        Returns:
            tuple[float, str]: (tax_amount, description)
        """
        rate = TaxRates.ESTATE_TAX_RATES.get(self.parents_country, 0.00)
        tax_amount = self.estate.get('total_value', 0) * rate
        
        description = (
            f"Estate tax of {rate*100}% based on {self.parents_country} rates. "
            f"Total estate value: ${self.estate.get('total_value', 0):,.2f}"
        )
        
        return tax_amount, description
        
    def calculate_total_tax_burden(self) -> Dict[str, Any]:
        """
        Calculate all applicable taxes and return a complete analysis.
        
        Returns:
            Dict[str, Any]: Complete tax analysis
        """
        capital_gains_tax, capital_gains_desc = self.calculate_capital_gains()
        inheritance_tax, inheritance_desc = self.calculate_inheritance_tax()
        estate_tax, estate_desc = self.calculate_estate_tax()
        
        total_tax = capital_gains_tax + inheritance_tax + estate_tax
        total_value = self.estate.get('total_value', 0)
        effective_tax_rate = (total_tax / total_value) if total_value > 0 else 0
        
        return {
            "estate_value": total_value,
            "estate_value_description": f"Total value of all assets in {self.parents_country}",
            "inheritance_tax": inheritance_tax,
            "inheritance_tax_description": inheritance_desc,
            "estate_tax": estate_tax,
            "estate_tax_description": estate_desc,
            "capital_gains_tax": capital_gains_tax,
            "capital_gains_tax_description": capital_gains_desc,
            "total_tax_burden": total_tax,
            "effective_tax_rate": effective_tax_rate
        } 