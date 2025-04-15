import pytest
from API_test.utils.schemas import User, UserCreate, UserListResponse, UserResponse
from API_test.utils.data_generator import generate_user_data, generate_email

@pytest.mark.api
class TestUsersAPI:
    def test_list_users(self, session):
        """Test GET /users - List all users"""
        page = 2
        # Use a URL completa concatenando corretamente
        response = session.get(f"{session.base_url}users?page={page}")
        
        assert response.status_code == 200
        
        users = UserListResponse(**response.json())
        
        assert users.page == page
        assert len(users.data) > 0
        assert isinstance(users.data[0], User)

    def test_get_single_user(self, session):
        """Test GET /users/{id} - Get single user"""
        user_id = 2
        # Use a URL completa concatenando corretamente
        response = session.get(f"{session.base_url}users/{user_id}")
        
        assert response.status_code == 200
        
        user_response = UserResponse(**response.json())
        assert user_response.data.id == user_id
        assert "@" in user_response.data.email