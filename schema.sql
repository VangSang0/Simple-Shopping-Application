CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO products (name, price) VALUES
    ('Beginning PC' , 849.99),
    ('Mid-Tier PC' , 1199.99),
    ('High-End PC' , 1599.99),

    ('Kevins Tool-Kit' : 7.99),
    ('Larrys Tool-Kit' , 35.99),
    ('Fanttik Tool Set' , 67.99),

    ('Keychron K2' , 74.99),
    ('Razor Mouse' , 21.99),
    ('Classic mousepad' , 14.99);