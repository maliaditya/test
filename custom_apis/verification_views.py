from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from authapp.models import User
import base64
import os
from twilio.rest import Client

account_sid = 'AC9f3176c894b3ba79073dba0146d8b6e3'
auth_token = 'bd258c6dfd08593efc33d4c6080173da'
client = Client(account_sid, auth_token)


class generateKey:
    permission_classes = []
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class SendOtp(APIView):
    permission_classes = []
    @staticmethod
    def get(request, phone):
        try:
            Mobile = User.objects.get(phone=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            message = {
                'message': 'Phone Number does exist please enter registered phone number'
            }
            return Response(data = message, status=400)

        Mobile.counter += 1
        Mobile.save()
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key) 

        message = client.messages \
                        .create(
                            body=f''''
                            You have recived this otp on request for password reset
                            Please click on the link below and enter the otp

                            Your one time password is:{OTP.at(Mobile.counter)}

                            http://127.0.0.1:8000/api/otp/
                                   ''',
                            from_='+19388883481',
                            to=f'+91{Mobile}'
                        )
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration
        
    @staticmethod
    def post(request, phone):
        try:
            Mobile = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call
        print("phone the iasnlkadnnjskdbhabxk maksndajs")
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorized", status=200)
        return Response("OTP is wrong", status=400)



