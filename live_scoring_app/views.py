from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import json






@api_view(['GET','POST'])
def start_match(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        match_id = request.data['match_id']
        tournament_id = request.data['tournament_id']
        # print("data::::::::::::",data)
        query = f"select create_dynamic_table_for_tournament_single_match_start('{match_id}','{tournament_id}');"
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
def live_score_input(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        data = json.dumps(request.data)
        # print("data::::::::::::",data)
        query = f"select input_live_Score('{data}');"
        # print("query::::::::::::",query)

        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                # row = cursor.fetchall()
                # row = cursor.fetchone()
                # row = json.loads(row[0])
                return Response(
                    {
                        "status": "success",
                        "data": "input completely complete",
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
            

