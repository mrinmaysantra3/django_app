from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Player
from .serializers import PlayerSerializer

@api_view(["GET"])
def getData(request):
    Players=Player.objects.all()
    serializer = PlayerSerializer(Players,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addPlayer(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

