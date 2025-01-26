import threading
from django.core.management.base import BaseCommand
from data_models.models import UserModel, ProductModel, OrderModel

class Command(BaseCommand):
    help = 'Simulate concurrent database insertions'

    def handle(self, *args, **options):
        # Create tables first
        UserModel.create_table()
        ProductModel.create_table()
        OrderModel.create_table()

        # User data
        users_data = [
            (1, 'Alice', 'alice@example.com'),
            (2, 'Bob', 'bob@example.com'),
            (3, 'Charlie', 'charlie@example.com'),
            (4, 'David', 'david@example.com'),
            (5, 'Eve', 'eve@example.com'),
            (6, 'Frank', 'frank@example.com'),
            (7, 'Grace', 'grace@example.com'),
            (8, 'Alice', 'alice@example.com'),
            (9, 'Henry', 'henry@example.com'),
            (10, '', 'jane@example.com')
        ]

        # Product data
        products_data = [
            (1, 'Laptop', 1000.00),
            (2, 'Smartphone', 700.00),
            (3, 'Headphones', 150.00),
            (4, 'Monitor', 300.00),
            (5, 'Keyboard', 50.00),
            (6, 'Mouse', 30.00),
            (7, 'Laptop', 1000.00),
            (8, 'Smartwatch', 250.00),
            (9, 'Gaming Chair', 500.00),
            (10, 'Earbuds', -50.00)
        ]

        # Order data
        orders_data = [
            (1, 1, 1, 2),
            (2, 2, 2, 1),
            (3, 3, 3, 5),
            (4, 4, 4, 1),
            (5, 5, 5, 3),
            (6, 6, 6, 4),
            (7, 7, 7, 2),
            (8, 8, 8, 0),
            (9, 9, 1, -1),
            (10, 10, 11, 2)
        ]

        # Threads for Users
        user_threads = []
        for user_data in users_data:
            user = UserModel(*user_data)
            thread = threading.Thread(target=user.insert)
            thread.start()
            user_threads.append(thread)

        # Threads for Products
        product_threads = []
        for product_data in products_data:
            product = ProductModel(*product_data)
            thread = threading.Thread(target=product.insert)
            thread.start()
            product_threads.append(thread)

        # Threads for Orders
        order_threads = []
        for order_data in orders_data:
            order = OrderModel(*order_data)
            thread = threading.Thread(target=order.insert)
            thread.start()
            order_threads.append(thread)

        # Wait for all threads to complete
        for thread in user_threads + product_threads + order_threads:
            thread.join()

        self.stdout.write(self.style.SUCCESS('Concurrent insertions completed'))