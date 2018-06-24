from django.contrib.auth import get_user_model
from django.db.models import Count
from django_filters import FilterSet, Filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework import generics, permissions
from utils.permission.custom_permission import IsProductMakerOrReadOnly

from ..serializers.recipe import RecipeSerializer
from ..models import Recipe, Sandwich

User = get_user_model()

__all__ = (
    'RecipeListCreateView',
    'RecipeRetrieveUpdateDestroyView',
)


class ListFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        self.lookup_expr = 'in'
        values_text = value.split(',')
        values = []
        for value in values_text:
            obj = Sandwich.objects.get(name=value)
            values.append(obj.id)
        return super().filter(qs, values)


class RecipeFilter(FilterSet):
    sandwich = ListFilter()

    class Meta:
        model = Recipe
        fields = (
            'sandwich',
        )


class RecipeListCreateView(generics.ListCreateAPIView):
    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    # filter_fields = ('sandwich',)
    # DjangoFilterBackends에 multiple id를 사용하기 위해
    # filter_class와 ListFilter를 활용하여 Custom
    filter_class = RecipeFilter

    ordering_fields = ('id', 'like_count', 'bookmark_count',)
    ordering = ('-like_bookmark_count', '-bookmark_count', '-like_count',)
    search_fields = ('name__name',)

    def get_queryset(self):
        queryset = Recipe.objects.annotate(
            like_count=Count('liker', distinct=True),
            bookmark_count=Count('bookmarker', distinct=True),
            like_bookmark_count=Count('liker', distinct=True) +
                            Count('bookmarker', distinct=True),
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(inventor=self.request.user)


class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsProductMakerOrReadOnly,
    )