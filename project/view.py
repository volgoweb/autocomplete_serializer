from rest_framework.generics import ListAPIView

from .models import Category
from .serializers import AutoCompleteSerializer


class CategoryAutocompleteView(ListAPIView):
    queryset = Category.objects.all()

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        kwargs['context'] = self.get_serializer_context()
        return AutoCompleteSerializer(*args,
                                      id_field_name='id',
                                      name_field_name='propname',
                                      **kwargs)
