from rest_framework import serializers

from recipes.serializers import RecipeSerializer
from users.serializers import UserSerializer
from ..models import BookmarkCollection


class BookmarkCollectionSerializer(serializers.ModelSerializer):

    # bookmarked_recipe = BookmarkSerializer(many=True, required=False)
    # Circling Import Issue -> model에서 'blank=True' 설정하고
    #   별도의 Nested Serializer를 위처럼 정의하지 않음으로 자동으로
    #   required=False가 설정되도록 함.

    user = UserSerializer(read_only=True)

    class Meta:
        model = BookmarkCollection
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        bookmarked_recipe_list = []
        for i in instance.bookmark_set.all():
            bookmarked_recipe_list.append(i.recipe)

        # 방법 1) informal way
        # serializer = RecipeSerializer(bookmarked_recipe_list, many=True)
        # serializer._context = self.context

        # 아래코드로는 AttributeError: can't set attribute 발생
        # _context, context 차이?
        # serializer.context = self.context

        # 방법 2) formal way
        # context = self.context
        # serializer = RecipeSerializer(bookmarked_recipe_list, many=True, context=context)

        # * iOS 요청으로 일단 auth_user_like_state, auth_user_bookmark_state를
        # null로 표시되도록 임시 변경
        serializer = RecipeSerializer(bookmarked_recipe_list, many=True)

        ret['bookmarked_recipe'] = serializer.data
        return ret
