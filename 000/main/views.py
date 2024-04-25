from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpRequest,JsonResponse,FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
import random

from .models import Person, Keys



class CreateToken(APIView):
    def post(self,request):
        user = request.data['user']
        user = Person.objects.get(jshr=user)
        tkn = ''
        for i in range(144):
            token = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5,' '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '/', '|', '№', ';', ':', '?', '<', '>', '.', ','])
            tkn+=token

        new_key = Keys.objects.create(
            token = tkn,
            user = user
        )

        name_lst = ''
        for i in range(15):
            name = random.choice(['1','2','3','4','5','6','7','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
            name_lst+=name

        new_key.save()
        a = open(f'{name_lst}.psw','w')
        a.write(tkn)
        a.close()
        f = open(f'{name_lst}.psw','rb')
        return FileResponse(f)
    
class CheckKey(APIView):
    def post(self,request):
        uploaded_file = request.FILES['fayl']
        f = fayl_malumotlari = uploaded_file.read()
        key = request.data['jshr']
        try:
            prs = Person.objects.get(jshr=key)
            ky = Keys.objects.get(user=prs)
            return Response({"Status":True})
        except:
            return Response({"Status":False})

