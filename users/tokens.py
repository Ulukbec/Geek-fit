from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

User = get_user_model()


def create_jwt_pair_for_user(user: User) -> dict:
    refresh = RefreshToken.for_user(user)
    access = AccessToken.for_user(user)
    tokens = {"access": str(access), "refresh": str(refresh)}

    return tokens