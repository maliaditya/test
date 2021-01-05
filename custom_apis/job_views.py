from django.shortcuts import render
from authapp.models import WorkerDetails, JobDetails, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json
# from authapp impo

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_job(request , user ):
    cursor = connection.cursor()
    cursor.execute(f'select category_1 , category_2 ,category_3  from authapp_workerdetails where authapp_workerdetails.user_id = {user}')
    row = cursor.fetchall()
    cursor.execute('select first_name ,job_title from authapp_user INNER JOIN authapp_jobdetails ON authapp_user.id  = authapp_jobdetails.recruiter_id')
    row1 = cursor.fetchall()
    content = {}
    payload = []
    for res in row:
        for res1 in row1:
           if res[0] == res1[1] or res[1] == res1[1] or res[2] == res1[1]:
               content = {
                          'recruiter_name' : res1[0],
                          'category_1': res1[1],
                         }
               payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_recruiter_job(request , recruiterid):
    cursor = connection.cursor()
    cursor.execute(f'select first_name,address , job_Description  from authapp_user INNER JOIN authapp_jobdetails on authapp_user.id = authapp_jobdetails.recruiter_id where authapp_jobdetails.recruiter_id = {recruiterid}')
    row = cursor.fetchall()
    content = {}
    payload = []
    for result in row:
        content = {
                       'name' : result[0],
                       'address' : result[1],
                       'job_Description' : result[2],
                       
                       }
        payload.append(content)
    return Response(data = payload , status = status.HTTP_200_OK)
