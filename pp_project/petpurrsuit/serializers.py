from rest_framework import serializers
from .models import Canine, Feline, State, Feline, Shelter

class CanineSerializer(serializers.ModelSerializer):
    
    shelter = serializers.StringRelatedField(
        
        many=False,
        read_only=True
        )

    class Meta:
       model = Canine
       fields = ('id', 'dogName', 'breed', 'age', 'photo_url', 'userCanine', 'user', 'shelter')

class FelineSerializer(serializers.ModelSerializer):
    shelter = serializers.StringRelatedField(
        many=False,
        read_only=True
    )

    class Meta:
       model = Feline
       fields = ('id', 'catName', 'breed', 'age', 'photo_url', 'userFeline', 'user', 'shelter')
    
class ShelterSerializer(serializers.ModelSerializer):
    state = serializers.HyperlinkedRelatedField(
        view_name='StateDetail',
        many=False,
        read_only=True
    )
    canines = CanineSerializer(
        # view_name='CanineDetail',
        many=True,
        read_only=True
    )
    felines = FelineSerializer(
        # view_name='FelineDetail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Shelter
       fields = ('id', 'shelterName', 'website', 'state', 'canines', 'felines')

class StateSerializer(serializers.ModelSerializer):
    shelters = ShelterSerializer(
        # view_name='ShelterDetail',
        many=True,
        read_only=True,
    )

    class Meta:
       model = State
       fields = ('id','stateName', 'shelters')