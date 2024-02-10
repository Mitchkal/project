#!/usr/bin/python3
"""
module payment
"""

from pydantic import BaseModel
from datetime import datetime


class Payment(BaseModel):
    """
    class definition to store payment information
    """
    payment_id: str
    user_id: str
    payment_method: str
    amount_paid: float
    date_paid: datetime = datetime.now()
