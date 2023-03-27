from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json


@api_view(['GET','POST'])
def TournamentCreation(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        query = f"select TournamentCreation('{data}');"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchone()
                # row = json.loads(row[0])
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
        



