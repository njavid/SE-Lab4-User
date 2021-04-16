from django.shortcuts import render
import json , jwt
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime , timedelta
from .models import User




@csrf_exempt
def register(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        user = User.objects.filter(username=received_json_data["username"])
        if len(user)!= 0:
            return HttpResponse(status=400, content="username exists!")
        print(received_json_data["password"])
        user = User(
            username = received_json_data["username"],
            password = received_json_data["password"],
            email = received_json_data["email"],
            mobile = received_json_data["mobile"],
        )
        user.save()


        print(request)
        return HttpResponse("created successfully",status= 201)
    else:
        return HttpResponse(status=401,content="method not allowed!")

def login(request):
    if request.method != 'GET':
        return HttpResponse(status=401, content="method not allowed!")
    received_json_data = json.loads(request.body)
    print(received_json_data["username"])
    user = User.objects.filter(username=received_json_data["username"])
    if len(user) == 0:
        return HttpResponse(status=401, content="username or password is incorrect!")
    user = user[0]
    print(123)
    if user.password == received_json_data["password"]:
        auth_token = encode_auth_token(user.id)
        response_data = {'token': auth_token.decode()}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)

    else:
        return HttpResponse(status=401,content="username or password is incorrect!")

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
