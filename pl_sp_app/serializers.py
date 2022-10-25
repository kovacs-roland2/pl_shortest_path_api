from rest_framework import serializers
from . import graph

class PathSerializer(serializers.Serializer):
    data_array = graph.ret_data('Frank Lampard', 'Peter Duffield')
