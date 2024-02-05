"""
module user model 
uses pydantic for dtat validation and modelling
"""

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    """
    User model
    """

    uid: str
    email: str
    full_name: Optional[str]
    profile_picture_url: Optional[str]

