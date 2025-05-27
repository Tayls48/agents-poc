from pydantic import BaseModel, Field
from typing import Optional, List

class inheritance_risk_output(BaseModel):
    estate_value: float
    estate_value_description: str
    inheritance_tax: float
    inheritance_tax_description: str
    estate_tax: float
    estate_tax_description: str
    capital_gains_tax: float
    capital_gains_tax_description: str

