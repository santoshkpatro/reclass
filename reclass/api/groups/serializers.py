from rest_framework import serializers
from reclass.models.enrollment import Enrollment
from reclass.models.group import Group
from reclass.models.user import User


class GroupListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'code',
            'group_type'
        ]


class GroupOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']


class GroupDetailSerializer(serializers.ModelSerializer):
    owner = GroupOwnerSerializer(read_only=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'description',
            'group_type',
            'owner'
        ]

    
class GroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name',
            'description',
            'group_type'
        ]


class GroupEnrolledUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'avatar',
            'first_name',
            'last_name'
        ]


class GroupEnrollmentSerializer(serializers.ModelSerializer):
    user = GroupEnrolledUserSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'is_active',
            'user',
        ]