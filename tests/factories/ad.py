import factory

from ads.models import Ad
from tests.factories.category import CategoryFactory
from tests.factories.user import UserFactory


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Test123456"
    price = 1234

    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)