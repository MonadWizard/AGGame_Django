from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json


@api_view(['GET','POST'])
def team_shedule(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        # print("data::::::::::::",data)
        query = f"select team_schedule('{data}');"
        # print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
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
            




@api_view(['GET','POST'])
def get_team_basic_data(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        # print("data::::::::::::",data)
        query = f"select get_team_basic_data('{data}');"
        print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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
            


@api_view(['GET','POST'])
def get_team_stats(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        # print("data::::::::::::",data)
        query = f"select get_team_stats('{data}');"
        print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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
            





@api_view(['GET','POST'])
def team_player_list(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        # print("data::::::::::::",data)
        query = f"select team_player_list('{data}');"
        print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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
            





@api_view(['GET','POST'])
def get_team_stats(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        # print("data::::::::::::",data)
        query = f"select get_team_stats('{data}');"
        # print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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
            




@api_view(['GET','POST'])
def upsert_team(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        # print("data::::::::::::",data)
        query = f"select upsert_team('{data}');"
        print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                # row = cursor.fetchone()
                # row = json.loads(row[0])
                return Response(
                    {
                        "status": "success",
                        "data": "update completely complete",
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
            





@api_view(['GET','POST'])
def update_player_info_in_team(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        # print("data::::::::::::",data)
        query = f"select upsert_team('{data}');"
        print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                # row = cursor.fetchone()
                # row = json.loads(row[0])
                return Response(
                    {
                        "status": "success",
                        "data": "update completely complete",
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
            




@api_view(['GET','POST'])
def team_player_list(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        # print("data::::::::::::",data)
        query = f"select team_player_list('{data}');"
        # print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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
        



@api_view(['GET','POST'])
def get_team_info(request, user_id, limit, offset):

    if request.method =='GET':
        user_id = user_id
        limit = limit
        offset = offset

        query = f"select get_team_info('{user_id}',{limit},{offset});"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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
def name_Search(request, user_name):

    if request.method =='GET':
        user_name = user_name
        
        query = f"select name_Search('{user_name}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                row = cursor.fetchone()
                row = json.loads(row[0])
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




