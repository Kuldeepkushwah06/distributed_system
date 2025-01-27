from django.core.exceptions import ValidationError
import threading
import logging
from concurrent.futures import ThreadPoolExecutor
from .models import User, Product, Order

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataValidator:
    @staticmethod
    def validate_data(model_class, data):
        instance = model_class(**data)
        try:
            instance.clean()
            # Add email validation for User model
            if model_class.__name__ == 'User':
                existing_user = User.objects.filter(email=data['email']).first()
                if existing_user:
                    return False, f"Email {data['email']} already exists"
            return True, None
        except ValidationError as e:
            return False, str(e)

class DatabaseInserter:
    def __init__(self):
        self.users_data = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
            {"id": 4, "name": "David", "email": "david@example.com"},
            {"id": 5, "name": "Eve", "email": "eve@example.com"},
            {"id": 6, "name": "Frank", "email": "frank@example.com"},
            {"id": 7, "name": "Grace", "email": "grace@example.com"},
            {"id": 8, "name": "Alice", "email": "alice@example.com"},
            {"id": 9, "name": "Henry", "email": "henry@example.com"},
            {"id": 10, "name": "", "email": "jane@example.com"},
        ]

        self.products_data = [
            {"id": 1, "name": "Laptop", "price": 1000.00},
            {"id": 2, "name": "Smartphone", "price": 700.00},
            {"id": 3, "name": "Headphones", "price": 150.00},
            {"id": 4, "name": "Monitor", "price": 300.00},
            {"id": 5, "name": "Keyboard", "price": 50.00},
            {"id": 6, "name": "Mouse", "price": 30.00},
            {"id": 7, "name": "Laptop", "price": 1000.00},
            {"id": 8, "name": "Smartwatch", "price": 250.00},
            {"id": 9, "name": "Gaming Chair", "price": 500.00},
            {"id": 10, "name": "Earbuds", "price": -50.00},
        ]

        self.orders_data = [
            {"id": 1, "user_id": 1, "product_id": 1, "quantity": 2},
            {"id": 2, "user_id": 2, "product_id": 2, "quantity": 1},
            {"id": 3, "user_id": 3, "product_id": 3, "quantity": 5},
            {"id": 4, "user_id": 4, "product_id": 4, "quantity": 1},
            {"id": 5, "user_id": 5, "product_id": 5, "quantity": 3},
            {"id": 6, "user_id": 6, "product_id": 6, "quantity": 4},
            {"id": 7, "user_id": 7, "product_id": 7, "quantity": 2},
            {"id": 8, "user_id": 8, "product_id": 8, "quantity": 0},
            {"id": 9, "user_id": 9, "product_id": 1, "quantity": -1},
            {"id": 10, "user_id": 10, "product_id": 11, "quantity": 2},
        ]

    def insert_record(self, model_class, data):
        record_id = data.get('id')
        is_valid, error = DataValidator.validate_data(model_class, data)
        
        if is_valid:
            try:
                model_class.objects.create(**data)
                logger.info(f"Successfully inserted {model_class.__name__} record {record_id}")
                return True, None
            except Exception as e:
                logger.error(f"Error inserting {model_class.__name__} record {record_id}: {str(e)}")
                return False, str(e)
        else:
            logger.error(f"Validation failed for {model_class.__name__} record {record_id}: {error}")
            return False, error

    def run_concurrent_insertions(self):
        with ThreadPoolExecutor(max_workers=30) as executor:
            user_futures = [executor.submit(self.insert_record, User, data) for data in self.users_data]
            product_futures = [executor.submit(self.insert_record, Product, data) for data in self.products_data]
            order_futures = [executor.submit(self.insert_record, Order, data) for data in self.orders_data]

            results = {
                'users': [future.result() for future in user_futures],
                'products': [future.result() for future in product_futures],
                'orders': [future.result() for future in order_futures]
            }

        return results