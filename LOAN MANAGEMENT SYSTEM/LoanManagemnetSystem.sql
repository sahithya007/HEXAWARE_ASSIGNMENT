-- Create the database
CREATE DATABASE LoanManagementSystem;

USE LoanManagementSystem;


CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),  -- Define CustomerID as identity and primary key
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    Address VARCHAR(255),
    CreditScore INT
);

-- Create Loans table (base class for loans) with foreign key reference
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY IDENTITY(1,1),  -- Define LoanID as identity and primary key
    CustomerID INT,  -- Foreign key reference
    PrincipalAmount DECIMAL(15, 2) NOT NULL,
    InterestRate DECIMAL(5, 2) NOT NULL,
    LoanTerm INT NOT NULL,  -- Loan tenure in months
    LoanType VARCHAR(50) CHECK (LoanType IN ('HomeLoan', 'CarLoan')),
    LoanStatus VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)  -- Foreign key constraint
);

-- Create HomeLoans table with foreign key reference
CREATE TABLE HomeLoans (
    HomeLoanID INT PRIMARY KEY IDENTITY(1,1),  -- Define HomeLoanID as identity and primary key
    LoanID INT,  -- Foreign key reference
    PropertyAddress VARCHAR(255),
    PropertyValue DECIMAL(15, 2),
    FOREIGN KEY (LoanID) REFERENCES Loans(LoanID)  -- Foreign key constraint
);

-- Create CarLoans table with foreign key reference
CREATE TABLE CarLoans (
    CarLoanID INT PRIMARY KEY IDENTITY(1,1),  -- Define CarLoanID as identity and primary key
    LoanID INT,  -- Foreign key reference
    CarModel VARCHAR(100),
    CarValue DECIMAL(15, 2),
    FOREIGN KEY (LoanID) REFERENCES Loans(LoanID)  -- Foreign key constraint
);

-- Enable IDENTITY_INSERT to insert explicit CustomerID values
SET IDENTITY_INSERT Customers ON;

-- Insert data into Customers table with specific CustomerID values
INSERT INTO Customers (CustomerID, Name, Email, Phone, Address, CreditScore) VALUES
(1, 'Rahul Sharma', 'rahul.sharma@example.com', '9876543210', '1st Main, Bangalore', 720),
(2, 'Anita Desai', 'anita.desai@example.com', '8765432109', '2nd Cross, Mumbai', 680),
(3, 'Vikram Singh', 'vikram.singh@example.com', '7654321098', '3rd Street, Delhi', 750),
(4, 'Priya Iyer', 'priya.iyer@example.com', '6543210987', '4th Lane, Chennai', 800),
(5, 'Ravi Patel', 'ravi.patel@example.com', '5432109876', '5th Road, Ahmedabad', 660),
(6, 'Sunita Mehta', 'sunita.mehta@example.com', '4321098765', '6th Block, Hyderabad', 690),
(7, 'Amit Verma', 'amit.verma@example.com', '3210987654', '7th Avenue, Pune', 740),
(8, 'Neha Reddy', 'neha.reddy@example.com', '2109876543', '8th Street, Kolkata', 710),
(9, 'Karan Bansal', 'karan.bansal@example.com', '1098765432', '9th Road, Jaipur', 760),
(10, 'Simran Kaur', 'simran.kaur@example.com', '0987654321', '10th Lane, Chandigarh', 780);

-- Disable IDENTITY_INSERT after insertion
SET IDENTITY_INSERT Customers OFF;

-- Insert data into Loans table
INSERT INTO Loans (CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus) VALUES
(1, 500000, 8.5, 60, 'HomeLoan', 'Pending'),
(2, 300000, 9.0, 48, 'CarLoan', 'Approved'),
(3, 700000, 7.5, 72, 'HomeLoan', 'Pending'),
(4, 150000, 10.0, 36, 'CarLoan', 'Approved'),
(5, 250000, 9.5, 60, 'CarLoan', 'Pending'),
(6, 800000, 8.0, 120, 'HomeLoan', 'Approved'),
(7, 600000, 7.0, 84, 'HomeLoan', 'Pending'),
(8, 350000, 8.2, 72, 'CarLoan', 'Approved'),
(9, 450000, 8.8, 60, 'HomeLoan', 'Pending'),
(10, 500000, 7.9, 48, 'CarLoan', 'Approved');

-- Insert data into HomeLoans table
INSERT INTO HomeLoans (LoanID, PropertyAddress, PropertyValue) VALUES
(1, '1st Main, Bangalore', 500000),
(3, '3rd Street, Delhi', 700000),
(2, '2nd Cross, Mumbai', 300000),
(4, '4th Lane, Chennai', 800000),
(5, '5th Road, Ahmedabad', 600000),
(6, '6th Block, Hyderabad', 450000),
(7, '7th Avenue, Pune', 750000),
(8, '8th Street, Kolkata', 500000),
(9, '9th Road, Jaipur', 620000),
(10, '10th Lane, Chandigarh', 800000);

-- Insert data into CarLoans table
INSERT INTO CarLoans (LoanID, CarModel, CarValue) VALUES
(1, 'Maruti Suzuki Alto', 300000),
(2, 'Hyundai i20', 250000),
(3, 'Tata Nexon', 500000),
(4, 'Kia Seltos', 400000),
(5, 'Mahindra Thar', 550000),
(6, 'Honda City', 700000),
(7, 'Toyota Fortuner', 1200000),
(8, 'Nissan Kicks', 900000),
(9, 'Ford EcoSport', 600000),
(10, 'Skoda Rapid', 750000);