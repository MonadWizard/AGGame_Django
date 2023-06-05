from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json
import datetime


@api_view(['GET','POST'])
def MatchCreation(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':

        data = request.data
        # if tournament_id exist then update tournament
        if 'game_id' in data:
            game_id = data['game_id']
            # print('update tournament')

        else:
            dtt = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            game_id = str(dtt)

        data = json.dumps(data)
        data = json.loads(data)
        
        data['game_id'] = game_id

        data = json.dumps(data)
        print('data:::::::::',data)
        query = f"select MatchCreation('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)

                return Response(
                    {
                        "status": "success",
                        "data": "match create success",
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
def get_team_by_specific_creator(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        # data = json.dumps(request.data)
        creator_id = request.data['creator_id']
        sport = request.data['sport']
        query = f"select get_all_Team_list_made_by_the_specific_creator('{creator_id}','{sport}');"
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
        


@api_view(['GET','POST'])
def get_all_team_list_by_game_name(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        # data = json.dumps(request.data)
        sport = request.data['sport']
        limit = request.data['limit']
        offset = request.data['offset']
        query = f"select get_all_team_list_by_game_name('{sport}','{limit}','{offset}');"
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
        



@api_view(['GET','POST'])
def team_and_player_info(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        query = f"select get_player_team_info_using_teamid('{data}');"

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
        




@api_view(['GET','POST'])
def upcomming_game_list(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)

        print('data:::::::::',data)
        query = f"select upcomming_game_list('{data}'::jsonb);"

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
        



@api_view(['GET','POST'])
def game_search(request, data):

    if request.method =='GET':
        data = data
        query = f"select Match_search('{data}');"

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



