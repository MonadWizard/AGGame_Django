from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def demo(request):
    if request.method =='GET':
        return Response('get data')

    elif request.method == 'POST':
        return Response('post data',status=status.HTTP_201_CREATED)
        