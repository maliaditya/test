from django.shortcuts import render
from authapp.models import WorkerDetails, JobDetails, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
import requests
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_workers_responses(request , worker_id ):
    cursor = connection.cursor()
    cursor.execute(f'select job_detail_id, recruiter from authapp_recruitersrequests where worker_id = {worker_id}')
    row1 = cursor.fetchall()
    print(row1)
    content= {}
    payload=[]
    for a in row1:
        job_id = a[0]
        recruiter_id = a[1]
        cursor.execute(f'select status_name from authapp_jobdetails j, authapp_statusmaster s where j.id = {job_id} and j.status = s.id')
        row2 = cursor.fetchall()
        st_info = row2[0]
        

        cursor.execute(f'select first_name, phone from authapp_user where id = {recruiter_id}')
        row3 = cursor.fetchall()


        for st in row2:
            for result in row3:
                content = {
                    'recruiter_name' : result[0],
                    'status': st[0],
                    'contact_no': result[1]        
                }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_recruiters_responses(request , recruiter_id ):
    cursor = connection.cursor()
    cursor.execute(f'select job_detail_id, worker_id from authapp_workersrequests where recruiter = {recruiter_id}')
    row1 = cursor.fetchall()
    print(row1)
    content= {}
    payload=[]
    for a in row1:
        job_id = a[0]
        worker_id = a[1]
        cursor.execute(f'select status_name from authapp_jobdetails j, authapp_statusmaster s where j.id = {job_id} and j.status = s.id')
        row2 = cursor.fetchall()
        st_info = row2[0]
        

        cursor.execute(f'select first_name, phone from authapp_user where id = {worker_id}')
        row3 = cursor.fetchall()


        for st in row2:
            for result in row3:
                content = {
                    'worker_name' : result[0],
                    'status': st[0],
                    'contact_no': result[1]        
                }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)


