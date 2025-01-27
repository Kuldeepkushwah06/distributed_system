class DatabaseRouter:
    """
    Router to control all database operations on models for different databases.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'main':
            if model._meta.model_name == 'user':
                return 'default'
            if model._meta.model_name == 'order':
                return 'orders'
            if model._meta.model_name == 'product':
                return 'products'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'main':
            if model._meta.model_name == 'user':
                return 'default'
            if model._meta.model_name == 'order':
                return 'orders'
            if model._meta.model_name == 'product':
                return 'products'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'main':
            if model_name == 'user':
                return db == 'default'
            if model_name == 'order':
                return db == 'orders'
            if model_name == 'product':
                return db == 'products'
        return None