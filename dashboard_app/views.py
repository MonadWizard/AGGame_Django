from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json


@api_view(['GET','POST'])
def Dashboard_information(request, team_id):

    if request.method =='GET':
        team_id = team_id
        
        query = f"select Dashboard_information('{team_id}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
                return Response(
                    {
                        "status": "success",
                        "data": row,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                err_msg = str(e)
                return Response(
                    {
                        "status": "fail",
                        "message": err_msg,
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )


    elif request.method == 'POST':
        return Response('post data')



@api_view(['GET','POST'])
def dash_game(request, team_id):

    if request.method =='GET':
        team_id = team_id
        
        query = f"select Match_Dashboard_information('{team_id}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
                return Response(
                    {
                        "status": "success",
                        "data": row,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                err_msg = str(e)
                return Response(
                    {
                        "status": "fail",
                        "message": err_msg,
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )


    elif request.method == 'POST':
        return Response('post data')



@api_view(['GET','POST'])
def dash_tournament(request, team_id):

    if request.method =='GET':
        team_id = team_id
        
        query = f"select Tournament_Dashboard_Information('{team_id}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                try:
                    row = cursor.fetchone()
                    row = json.loads(row[0])
                except:
                    row = cursor.fetchall()
                return Response(
                    {
                        "status": "success",
                        "data": row,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                err_msg = str(e)
                return Response(
                    {
                        "status": "fail",
                        "message": err_msg,
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )


    elif request.method == 'POST':
        return Response('post data')

