from .database import get_db_connection
from .models import UserCreate, ProductCreate, OrderCreate

# User CRUD operations
def create_user(user: UserCreate):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO users (username, email, password_hash, first_name, last_name)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (user.username, user.email, user.password, user.first_name, user.last_name))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
        finally:
            connection.close()

def get_users():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT user_id, username, email, first_name, last_name, created_at FROM users")
            users = cursor.fetchall()
            return users
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []
        finally:
            connection.close()

def get_user(user_id: int):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT user_id, username, email, first_name, last_name, created_at FROM users WHERE user_id = %s", (user_id,))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        finally:
            connection.close()

def update_user(user_id: int, user_data: dict):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            set_clause = ", ".join([f"{key} = %s" for key in user_data.keys()])
            values = list(user_data.values())
            values.append(user_id)
            
            query = f"UPDATE users SET {set_clause} WHERE user_id = %s"
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            connection.close()

def delete_user(user_id: int):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            connection.close()

# Product CRUD operations
def create_product(product: ProductCreate):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO products (name, description, price, stock_quantity, category_id)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (product.name, product.description, product.price, product.stock_quantity, product.category_id))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating product: {e}")
            return None
        finally:
            connection.close()

def get_products():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products WHERE is_active = TRUE")
            products = cursor.fetchall()
            return products
        except Exception as e:
            print(f"Error fetching products: {e}")
            return []
        finally:
            connection.close()

def get_product(product_id: int):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products WHERE product_id = %s AND is_active = TRUE", (product_id,))
            product = cursor.fetchone()
            return product
        except Exception as e:
            print(f"Error fetching product: {e}")
            return None
        finally:
            connection.close()

def update_product(product_id: int, product_data: dict):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            set_clause = ", ".join([f"{key} = %s" for key in product_data.keys()])
            values = list(product_data.values())
            values.append(product_id)
            
            query = f"UPDATE products SET {set_clause} WHERE product_id = %s"
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating product: {e}")
            return False
        finally:
            connection.close()

def delete_product(product_id: int):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE products SET is_active = FALSE WHERE product_id = %s", (product_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False
        finally:
            connection.close()

# Order CRUD operations
def create_order(order: OrderCreate):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO orders (user_id, total_amount, shipping_address, billing_address)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (order.user_id, order.total_amount, order.shipping_address, order.billing_address))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating order: {e}")
            return None
        finally:
            connection.close()

def get_orders():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
            return orders
        except Exception as e:
            print(f"Error fetching orders: {e}")
            return []
        finally:
            connection.close()

def get_order(order_id: int):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))
            order = cursor.fetchone()
            return order
        except Exception as e:
            print(f"Error fetching order: {e}")
            return None
        finally:
            connection.close()