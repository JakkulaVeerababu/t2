import requests

BASE_URL = 'http://127.0.0.1:8000/api/auth'

def test_registration():
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword123',
        'first_name': 'Test',
        'last_name': 'User',
        'profile': {
            'role': 'operator'
        }
    }
    try:
        response = requests.post(f'{BASE_URL}/register/', json=data)
        if response.status_code == 201:
            print("Registration Successful")
            return True
        elif response.status_code == 400 and 'username' in response.json() and 'already exists' in str(response.json()['username']):
             print("User already exists")
             return True
        else:
            print(f"Registration Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Registration Error: {e}")
        return False

def test_login():
    data = {
        'username': 'testuser',
        'password': 'testpassword123'
    }
    try:
        response = requests.post(f'{BASE_URL}/login/', json=data)
        if response.status_code == 200:
            token = response.json().get('access')
            print("Login Successful, Token received")
            return token
        else:
            print(f"Login Failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Login Error: {e}")
        return None

def test_profile(token):
    headers = {'Authorization': f'Bearer {token}'}
    try:
        response = requests.get(f'{BASE_URL}/profile/', headers=headers)
        if response.status_code == 200:
            print("Profile Retrieval Successful")
            print(response.json())
            return True
        else:
            print(f"Profile Retrieval Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Profile Error: {e}")
        return False

if __name__ == '__main__':
    if test_registration():
        token = test_login()
        if token:
            test_profile(token)
