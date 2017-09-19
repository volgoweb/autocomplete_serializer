from rest_framework import serializers
from rest_framework.fields import ModelField
from django.db.models.query import QuerySet


class IdNameDictSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        instance_list = super(IdNameDictSerializer, self).to_representation(data)
        id_name_dict = {x['overridden_id']: x['overridden_name'] for x in instance_list}
        return id_name_dict

    @property
    def data(self):
        return super(serializers.ListSerializer, self).data


class AutoCompleteSerializer(serializers.ModelSerializer):
    overridden_id = serializers.SerializerMethodField(method_name='get_id')
    overridden_name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        list_serializer_class = IdNameDictSerializer

    def __init__(self, *args, id_field_name, name_field_name, **kwargs):
        super(AutoCompleteSerializer, self).__init__(*args, **kwargs)

    def __new__(cls, *args, id_field_name, name_field_name, **kwargs):
        try:
            queryset = args[0]
            model_cls = queryset.model
        except (IndexError, AttributeError):
            raise ValueError('You must define a queryset as a first argument.')
        cls.Meta.model = model_cls

        cls.Meta.fields = list(set([id_field_name, name_field_name, 'overridden_id', 'overridden_name']))

        self = super(AutoCompleteSerializer, cls).__new__(cls, *args,
                                                          id_field_name=id_field_name,
                                                          name_field_name=name_field_name,
                                                          **kwargs)
        self.id_field_name = id_field_name
        self.name_field_name = name_field_name
        return self

    def get_id(self, obj):
        val = getattr(obj, self.id_field_name)
        return str(val)

    def get_name(self, obj):
        val = getattr(obj, self.name_field_name)
        return str(val)
