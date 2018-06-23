from django.db import models


class Vegetables(models.Model):
    """
    Product와 Many-to-many relationship으로 연결된 vegetables
    """

    VEGETABLE_LESS = 'LE'
    VEGETABLE_NORMAL = 'NO'
    VEGETABLE_MORE = 'MO'

    VEGETABLE_QUANTITY_CHOICES = (
        (VEGETABLE_LESS, 'LESS'),
        (VEGETABLE_NORMAL, 'NORMAL'),
        (VEGETABLE_MORE, 'MORE'),
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='100자까지 vegetable의 이름을 저장합니다.',
    )

    quantity = models.CharField(
        max_length=2,
        choices=VEGETABLE_QUANTITY_CHOICES,
        default='NO'
    )

    class Meta:
        verbose_name_plural = '선택한 vegetables'

    def __str__(self):
        return f'{self.pk}_{self.name}'
