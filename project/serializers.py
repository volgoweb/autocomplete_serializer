from rest_framework import serializers
from rest_framework.fields import ModelField


class IdNameDictSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        instance_list = super(IdNameDictSerializer, self).to_representation(data)
        id_name_dict = {x['id']: x['name'] for x in instance_list}
        return id_name_dict

    @property
    def data(self):
        return super(serializers.ListSerializer, self).data


class AutoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = IdNameDictSerializer

    def __init__(self, *args, model_cls, id_field_name, name_field_name, **kwargs):
        super(AutoCompleteSerializer, self).__init__(*args, **kwargs)

    def __new__(cls, *args, model_cls, id_field_name, name_field_name, **kwargs):
        cls.Meta.model = model_cls
        cls.Meta.fields = list(set([id_field_name, name_field_name, 'id', 'name']))
        id_field = model_cls()._meta.get_field(id_field_name)
        name_field = model_cls()._meta.get_field(name_field_name)
        cls._declared_fields['id'] = ModelField(model_field=id_field)
        cls._declared_fields['name'] = ModelField(model_field=name_field)

        self = super(AutoCompleteSerializer, cls).__new__(cls, *args,
                                                          model_cls=model_cls,
                                                          id_field_name=id_field_name,
                                                          name_field_name=name_field_name,
                                                          **kwargs)
        return self
