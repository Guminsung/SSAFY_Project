from rest_framework import serializers
from .models import Recommend, Todo


class TodoSerializer(serializers.ModelSerializer):
    class RecommendSerialzerForTodoDetail(serializers.ModelSerializer):
        class Meta:
            model = Recommend
            exclude = ('todo',)

    recommend_set = RecommendSerialzerForTodoDetail(many=True)

    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
        read_only_fields = ('todo',)
