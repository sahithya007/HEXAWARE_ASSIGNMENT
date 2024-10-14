CREATE DATABASE Finance_Mgmt;
USE Finance_Mgmt;
CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE ExpenseCategories (
    category_id INT PRIMARY KEY IDENTITY,
    category_name VARCHAR(50) NOT NULL
);

CREATE TABLE Expenses (
    expense_id INT PRIMARY KEY IDENTITY,
    user_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    category_id INT,
    date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES ExpenseCategories(category_id)
);

INSERT INTO ExpenseCategories (category_name)
VALUES ('Food'), ('Transportation'), ('Utilities'),('Investments');

INSERT INTO ExpenseCategories (category_name)
VALUES 
('Entertainment'),
('Healthcare'),
('Insurance'),
('Education'),
('Clothing'),
('Groceries'),
('Dining Out'),
('Subscriptions'),
('Travel'),
('Home Maintenance'),
('Personal Care'),
('Gifts'),
('Charity'),
('Pet Care'),
('Savings'),
('Debt Payments'),
('Fitness'),
('Electronics'),
('Rent'),
('Taxes');

select * from Users;

select * from Expenses;

select * from ExpenseCategories;
