from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from api.utils import number_to_english

def landing_page(request):
    return render(request, 'landing_page.html')

@api_view(['GET', 'POST'])
def num_to_english(request):
    if request.method == 'GET':
        number = request.query_params.get('number')
    elif request.method == 'POST':
        data = request.data
        number = data.get('number')
    else:
        return Response({'status': 'error', 'message': 'Invalid HTTP method'}, status=400)

    if not number:
        return Response({'status': 'error', 'message': 'Number parameter is missing'}, status=400)

    try:
        number = int(number)
        num_in_english = number_to_english(number)
        return Response({'status': 'ok', 'num_in_english': num_in_english})
    except ValueError:
        return Response({'status': 'error', 'message': 'Invalid number format'}, status=400)
