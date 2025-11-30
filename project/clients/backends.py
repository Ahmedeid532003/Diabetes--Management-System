from django.contrib.auth.backends import ModelBackend
from .models import client
from django.contrib.auth.hashers import check_password


class CustomBackend(ModelBackend):
    def authenticate( self ,request, username , password):
        try:
            user = client.objects.get(UserName=username)
            
            print("client.UserName",client.UserName)
            print("user111",user , "----", user.UserName )
            print("user PASS",password , "----",user.Password)
            if password == user.Password:
                print("Email ",user.Email)
                print("user PASS",password , "----", user.Password )
                
                return user
        except client.DoesNotExist:
            return None
        
        
        return None
