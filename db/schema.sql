CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    profession VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE income (
    income_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    date DATE,
    amount FLOAT,
    source VARCHAR(100)
);

CREATE TABLE transactions (
    trans_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    date DATE,
    category VARCHAR(50),
    amount FLOAT,
    payment_mode VARCHAR(50)
);

CREATE TABLE credit_usage (
    usage_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    date DATE,
    credit_used FLOAT,
    credit_limit FLOAT
);
