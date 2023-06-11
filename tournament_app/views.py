from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json
from django.conf import settings
import datetime

from .utils import image_decoder

@api_view(['GET','POST'])
def TournamentCreation(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        
        data = request.data
        # if tournament_id exist then update tournament
        if 'tournament_id' in data:
            tournament_id = data['tournament_id']
            # print('update tournament')

        else:
            dtt = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            tournament_id = str(dtt)
            # print('create tournament')
        
        if 'tournament_logo' in data:
            base64_image = data['tournament_logo']
            image_extension = data['tournament_photopath_extension']
            tournament_logo_path = '/tournament_logo/' + str(tournament_id) + '/'
            image_url = image_decoder(base64_image, image_extension,tournament_id, tournament_logo_path)
            data = json.dumps(data)
            data = json.loads(data)
            del data['tournament_photopath_extension']
            data['tournament_logo'] = image_url

        data = json.dumps(data)
        data = json.loads(data)
        data['tournament_id'] = tournament_id
        # data['tournament_logo'] = image_url
        data = json.dumps(data)

        query = f"select Create_Tournament('{data}');"
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
def get_tournament_details(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        tournament_id = request.data['tournament_id']
        sport = request.data['sport']
        query = f"select get_tournament_details('{tournament_id}','{sport}');"
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
def get_tournament_info(request, user_id, limit, offset):

    if request.method =='GET':
        user_id = user_id
        limit = limit
        offset = offset

        query = f"select get_tournament_details_basedOn_tournament_owner_id('{user_id}',{limit},{offset});"

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
def tournament_schedule(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)

        query = f"select tournament_schedule('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)

                return Response(
                    {
                        "status": "success",
                        "data": "sheduled create success",
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
def tournament_schedule_update(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)

        query = f"select tournament_schedule_update('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)

                return Response(
                    {
                        "status": "success",
                        "data": "sheduled create success",
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
def get_tournament_shedule(request, tournament_id):
    if request.method =='GET':
        tournament_id = tournament_id
        query = f"select get_tournament_shedule_data('{tournament_id}');"
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
def upcomming_tournament_list(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)

        query = f"select upcomming_tournament_list('{data}'::jsonb);"
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
def tournament_update(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)

        query = f"select Tournament_Update('{data}');"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                
                return Response(
                    {
                        "status": "success",
                        "data": "tournament update success",
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
def tournament_search(request, data):

    if request.method =='GET':
        data = data
        query = f"select tournament_search('{data}');"

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
def tournament_team_search(request, data):

    if request.method =='GET':
        data = data
        query = f"select tournament_team_search('{data}');"

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
def tournament_start(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)

        query = f"select score_start_match_tournament('{data}'::jsonb);"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                
                return Response(
                    {
                        "status": "success",
                        "data": "tournament started successfull",
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
        









