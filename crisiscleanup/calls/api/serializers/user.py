from rest_framework import serializers
from pprint import pprint

from crisiscleanup.calls.models import User, Language
# from .language import LanguageSerializer

# class LanguageIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Language
#         fields = ('id',)

class UserSerializer(serializers.ModelSerializer):
    read_articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    training_completed = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # languages = LanguageIdSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'willing_to_receive_calls', 'willing_to_be_call_hero', 'willing_to_be_call_center_support',
                  'willing_to_be_pin_hero', 'last_used_phone_number', 'last_used_state', 'last_used_gateway',
                  'read_articles', 'training_completed', 'name', 'languages')
        depth = 1

    # def create(self, validated_data):
    #     languages_data = validated_data.pop('languages')
    #     user = User.objects.create(**validated_data)
    #     user.save()
    #     languages = Language.objects.filter(id__in=languages_data)
    #     user.languages.add(languages)
    #     return user
    
    def update(self, instance, validated_data):
        languages_data = validated_data.pop('languages')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        # TODO: save the user's languages
        # language_ids = (lang['id'] for lang in languages_data)
        # print(language_ids)
        # languages = Language.objects.filter(id__in=language_ids)
        # instance.languages.set(languages)
        return instance
