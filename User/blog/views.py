from django.shortcuts import render
import json , jwt
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime , timedelta
from .models import User




def encode_auth_token( user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        print(1)
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=120),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        print(jwt.encode(
            payload,
            '@qljsvhy@64=a$@6&1ehxr)j7cih-$f(yl(y9zlprz922k62d1',
            algorithm='HS256'
        ))
        return jwt.encode(
            payload,
            '@qljsvhy@64=a$@6&1ehxr)j7cih-$f(yl(y9zlprz922k62d1',
            algorithm='HS256'
        )
    except Exception as e:
        print(e)
        return e
def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, '@qljsvhy@64=a$@6&1ehxr)j7cih-$f(yl(y9zlprz922k62d1')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
