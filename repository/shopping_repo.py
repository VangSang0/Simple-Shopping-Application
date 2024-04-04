from repository.db import get_pool
from psycopg.rows import dict_row


def get_all_products():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                                SELECT 
                                    * 
                                FROM 
                                    products
                            ''')
            return cursor.fetchall()

def get_product(product_name):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            Select
                                name,
                                price
                            FROM
                                products
                            WHERE
                                name = %s
                            
                            ''', [product_name])
            return cursor.fetchone()