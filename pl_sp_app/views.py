from django.shortcuts import render
from . import graph
from django.http import JsonResponse


def home(request):
    player1 = request.GET["player1"]
    player2 = request.GET["player2"]
    data_array = graph.ret_data(player1, player2)
    #return render(request, 'index.html', { 'data_array':data_array.to_html()})
    return JsonResponse(data_array.to_json(), safe=False)




