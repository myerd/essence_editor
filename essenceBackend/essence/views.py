from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from essence.serializers import *
from rest_framework.decorators import api_view

#Views for CARD
@api_view(['GET', 'POST', 'DELETE'])
def card_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            cards = cards.filter(title__contains=title)

        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)

    elif request.method == 'POST':
        card_data = JSONParser().parse(request)
        card_serializer = CardSerializer(data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse(card_serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        count = Card.objects.all().delete()
        return JsonResponse({'message': '{} Cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, pk):
    try:
        card = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return JsonResponse({'message': 'The Card does no exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        card_serializer = CardSerializer(card)
        return JsonResponse(card_serializer.data)

    elif request.method == 'PUT':
        card_data = JSONParser().parse(request)
        card_serializer = CardSerializer(card, data=card_data)
        if card_serializer.is_valid():
            card_serializer.save()
            return JsonResponse(card_serializer.data)
        return JsonResponse(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        card.delete()
        return JsonResponse({'message': 'Card was deleted succesfully!'}, status= status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def card_list_completed(request):
    cards = Card.objects.filter(completed=True)

    if request.method == 'GET':
        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)


#Views for Team:
@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except:
        return JsonResponse({'message': 'The Team does no exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        team_serializer = TeamSerializer(team)
        return JsonResponse(team_serializer.data)

    elif request.method == 'PUT':
        team_data = JSONParser().parse(request)
        team_serializer = TeamSerializer(team, data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return JsonResponse({'message': 'Team was deleted succesfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def team_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        teams_serializer = TeamSerializer(teams, many=True)
        return JsonResponse(teams_serializer.data, safe=False)

    elif request.method == 'POST':
        team_data = JSONParser().parse(request)
        team_serializer = TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)
