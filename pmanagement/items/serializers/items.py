"""Items serializers."""

# Django REST Frameworks
from rest_framework import serializers

# Serializers
from pmanagement.users.serializers import UserModelSerializer

# Models
from pmanagement.items.models import Item
from pmanagement.projects.models import Membership


class ItemModelSerializer(serializers.ModelSerializer):
    """Item model serializer."""

    order_by = UserModelSerializer(read_only=True)
    order_in = serializers.StringRelatedField()

    class Meta:
        """Meta class."""

        model = Item
        fields = '__all__'
        read_only_fields = (
                    'order_by',
                    'order_in'
                    )


class CreateItemSerializer(serializers.ModelSerializer):
    """Create Item Serializer."""

    order_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        """Meta class."""

        model = Item

        exclude = (
                'order_in',
                )

    def validate(self, data):
        """ Validate
        verify  that the person who orders the item is member
        and also the same user  making the request.
        """

        if self.context['request'].user != data['order_by']:
            raise serializers.ValidationError('Items order on behalf of others are not allowed,')

        user = data['order_by']
        project = self.context['project']

        try:
            membership = Membership.objects.get(
                          user=user,
                          project=project
                          )
        except Membership.DoesNotExist:
            raise serializers.ValidationError('User is not an active member of the circle')

        self.context['membership'] = membership

        return data

    def create(self, data):
        """Create ride an update budget. """
        project = self.context['project']
        item = Item.objects.create(**data, order_in=project)

        # Project
        project.budget -= item.cost
        project.save()

        return item
