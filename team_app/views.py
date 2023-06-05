from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json
import datetime

from tournament_app.utils import image_decoder




@api_view(['GET','POST'])
def team_shedule(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        query = f"select Get_Tournament_Match_Schedule_based_on_team_id('{data}');"

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
def get_team_basic_data(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        query = f"select get_team_basic_data('{data}');"

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
def get_team_stats(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        query = f"select get_team_stats('{data}');"

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
def team_player_list(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        query = f"select team_player_list('{data}');"

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
def get_team_stats(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = request.data['team_id']
        query = f"select get_team_stats('{data}');"

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
def upsert_team(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':

        data = request.data
        # if tournament_id exist then update tournament
        if 'team_id' in data:
            team_id = data['team_id']
            # print('update tournament')

        else:
            dtt = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            team_id = str(dtt)
            # print('create tournament')
        
        if 'team_logo' in data:
            base64_image = data['team_logo']
            image_extension = data['team_photopath_extension']
            team_logo_path = '/team_logo/' + str(team_id) + '/'
            image_url = image_decoder(base64_image, image_extension,team_id, team_logo_path)
            data = json.dumps(data)
            data = json.loads(data)
            del data['team_photopath_extension']
            data['team_logo'] = image_url

        data = json.dumps(data)
        data = json.loads(data)
        data['team_id'] = team_id
        # data['tournament_logo'] = image_url
        data = json.dumps(data)

        query = f"select Upsert_team_basic_info('{data}');"

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
def update_player_info_in_team(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        query = f"select update_Player_in_team_info('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
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
        query = f"select team_player_list('{data}');"

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()

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
def get_team_info(request, user_id, limit, offset):

    if request.method =='GET':
        user_id = user_id
        limit = limit
        offset = offset

        query = f"select get_Team_details_based_on_team_Creator_id('{user_id}',{limit},{offset});"

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
def name_Search(request, user_name):

    if request.method =='GET':
        user_name = user_name
        
        query = f"select search_userfullname_unsernickname('{user_name}');"

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




