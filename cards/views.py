from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cards.models import Card
from cards.serializers import CardsSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['GET', 'POST', 'DELETE'])
def cards_list(request):

    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardsSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def cards_detail(request, pk):
    try: 
        card = Card.objects.get(pk=pk) 
    except Card.DoesNotExist: 
        return JsonResponse({'message': 'The card does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        cards_serializer = CardsSerializer(card)
        return JsonResponse(cards_serializer.data)
    
    elif request.method == 'PUT': 
        cards_data = JSONParser().parse(request) 
        cards_serializer = CardsSerializer(card, data=cards_data) 
        if cards_serializer.is_valid(): 
            cards_serializer.save() 
            return JsonResponse(cards_serializer.data) 
        return JsonResponse(cards_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        card.delete() 
        return JsonResponse({'message': 'Card was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)