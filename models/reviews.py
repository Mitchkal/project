#!/usr/bin/python3
"""
module to store user reviews
"""

from pydantic import BaseModel
from datetime import datetime


class Review(BaseModel):
    """
    The review class
    """
    review_id: str
    user_id: str  # foreign key to User model
    product_id: str  # foreign key to Product model
    rating: int
    comment: str = ""
    dateposted: datetime = datetime.now()
