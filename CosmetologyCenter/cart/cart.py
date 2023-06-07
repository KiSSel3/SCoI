from django.conf import settings
from services.models import Issue
from decimal import Decimal
class Cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, issue, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        issue_id = str(issue.id)
        if issue_id not in self.cart:
            self.cart[issue_id] = {'quantity': 0,
                                  'price': str(issue.price)}
        if update_quantity:
            self.cart[issue_id]['quantity'] = quantity
        else:
            self.cart[issue_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, book):
        """
        Удаление товара из корзины.
        """
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        issue_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        issues = Issue.objects.filter(id__in=issue_ids)
        for issue in issues:
            self.cart[str(issue.id)]['issue'] = issue

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True