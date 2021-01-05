from django.shortcuts import render
from authapp.models import (
    WorkerDetails, JobDetails, User, Categories
    )
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recruiters_requests(request,recruiter_id):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details where category_1 = '{category}' OR category_2 = '{category}' OR category_3 = '{category}' ")
    #cursor.execute(f'select job_description, job_title, worker_id,amount from authapp_recruitersrequests r , authapp_jobdetails j where r.recruiter ={recruiter_id} and j.recruiter_id = r.recruiter')
    cursor.execute(f'select job_description, job_title, worker_id ,amount from authapp_jobdetails ,authapp_recruitersrequests where authapp_recruitersrequests.job_detail_id = authapp_jobdetails.id  and authapp_recruitersrequests.recruiter = {recruiter_id}')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
        cursor.execute(f'select first_name, address from authapp_user  where id = {data[2]}')
        row1 = cursor.fetchall()
        for info in row1:

            content = {
            'job_title': data[1],
            'job_description': data[0],
            'amount': data[3],
            'woker_name': info[0],
            'woker_address': info[1],
            }
        payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wokers_requests(request,worker_id):
    cursor=connection.cursor()
    cursor.execute(f'select job_description, job_title, recruiter_id  from authapp_jobdetails ,authapp_workersrequests where authapp_workersrequests.job_detail_id = authapp_jobdetails.id  and worker_id = {worker_id}')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
        u_id = data[2] 
        cursor.execute(f'select first_name, address from authapp_user where id = {u_id}')
        row = cursor.fetchall()
        for info in row:
            content = {
                'job_title': data[1],
                'job_description': data[0],
                'recruiter_id': data[2],
                'recruiter_name':info[0],
                'address':info[1],

                }  
        
        
        
        payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)


