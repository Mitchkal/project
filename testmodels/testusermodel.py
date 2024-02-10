from models import user
"""
model to test user model
"""

user_data = {
        'uid': 'id_example'
        'email': 'user@example.com'
        'full_name': 'John Doe'
        'profile_picture_url': 'https://example.com/profilepicture.jpg',
        }

user_instance = User(**user_data)

print(user_instance.email)
print(user_instance.full_name)
