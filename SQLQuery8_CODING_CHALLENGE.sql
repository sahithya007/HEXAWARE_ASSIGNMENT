CREATE DATABASE CarRentalSystem;
USE CarRentalSystem;

CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    dailyRate DECIMAL(10, 2),
    status VARCHAR(20) CHECK (status IN ('available', 'notAvailable')),
    passengerCapacity INT,
    engineCapacity INT
);

CREATE TABLE Customer (
    customerID INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    phoneNumber VARCHAR(15)
);

CREATE TABLE Lease (
    leaseID INT PRIMARY KEY,
    vehicleID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    type VARCHAR(20) CHECK (type IN ('Daily', 'Monthly')),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE Payment (
    paymentID INT PRIMARY KEY,
    leaseID INT,
    paymentDate DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);


INSERT INTO Vehicle (vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
VALUES
(1, 'Toyota', 'Camry', 2022, 50.00, 'available', 4, 1450),
(2, 'Honda', 'Civic', 2023, 45.00, 'available', 7, 1500),
(3, 'Ford', 'Focus', 2022, 48.00, 'notAvailable', 4, 1400),
(4, 'Nissan', 'Altima', 2023, 52.00, 'available', 7, 1200),
(5, 'Chevrolet', 'Malibu', 2022, 47.00, 'available', 4, 1800),
(6, 'Hyundai', 'Sonata', 2023, 49.00, 'notAvailable', 7, 1400),
(7, 'BMW', '3 Series', 2023, 60.00, 'available', 7, 2499),
(8, 'Mercedes', 'C-Class', 2022, 58.00, 'available', 8, 2599),
(9, 'Audi', 'A4', 2022, 55.00, 'notAvailable', 4, 2500),
(10, 'Lexus', 'ES', 2023, 54.00, 'available', 4, 2500);

INSERT INTO Customer (customerID, firstName, lastName, email, phoneNumber)
VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '555-555-5555'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '555-123-4567'),
(3, 'Robert', 'Johnson', 'robert@example.com', '555-789-1234'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '555-456-7890'),
(5, 'David', 'Lee', 'david@example.com', '555-987-6543'),
(6, 'Laura', 'Hall', 'laura@example.com', '555-234-5678'),
(7, 'Michael', 'Davis', 'michael@example.com', '555-876-5432'),
(8, 'Emma', 'Wilson', 'emma@example.com', '555-432-1098'),
(9, 'William', 'Taylor', 'william@example.com', '555-321-6547'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '555-765-4321');

INSERT INTO Lease (leaseID, vehicleID, customerID, startDate, endDate, type)
VALUES
(1, 1, 1, '2023-01-01', '2023-01-05', 'Daily'),
(2, 2, 2, '2023-02-15', '2023-02-28', 'Monthly'),
(3, 3, 3, '2023-03-10', '2023-03-15', 'Daily'),
(4, 4, 4, '2023-04-20', '2023-04-30', 'Monthly'),
(5, 5, 5, '2023-05-05', '2023-05-10', 'Daily'),
(6, 4, 3, '2023-06-15', '2023-06-30', 'Monthly'),
(7, 7, 7, '2023-07-01', '2023-07-10', 'Daily'),
(8, 8, 8, '2023-08-12', '2023-08-15', 'Monthly'),
(9, 3, 3, '2023-09-07', '2023-09-10', 'Daily'),
(10, 10, 10, '2023-10-10', '2023-10-31', 'Monthly');

INSERT INTO Payment (paymentID, leaseID, paymentDate, amount)
VALUES
(1, 1, '2023-01-03', 200.00),
(2, 2, '2023-02-20', 1000.00),
(3, 3, '2023-03-12', 75.00),
(4, 4, '2023-04-25', 900.00),
(5, 5, '2023-05-07', 60.00),
(6, 6, '2023-06-18', 1200.00),
(7, 7, '2023-07-03', 40.00),
(8, 8, '2023-08-14', 1100.00),
(9, 9, '2023-09-09', 80.00),
(10, 10, '2023-10-25', 1500.00);


-- tasks questions
UPDATE Vehicle
SET dailyRate = 68
WHERE make = 'Mercedes' AND model = 'C-Class';

SELECT * from vehicle

DELETE FROM Payment WHERE leaseID IN (SELECT leaseID FROM Lease WHERE customerID = 1);
DELETE FROM Lease WHERE customerID = 1;
DELETE FROM Customer WHERE customerID = 1;


EXEC sp_rename 'Payment.paymentDate', 'transactionDate', 'COLUMN';

select * from payment;

SELECT * FROM Customer WHERE email = 'olivia@example.com';


SELECT * FROM Lease WHERE customerID = 3 AND endDate >= GETDATE();

SELECT P.* 
FROM Payment P
JOIN Lease L ON P.leaseID = L.leaseID
JOIN Customer C ON L.customerID = C.customerID
WHERE C.phoneNumber = '555-765-4321';

SELECT AVG(dailyRate) AS AvgDailyRate
FROM Vehicle
WHERE status = 'available';

SELECT TOP 1 * 
FROM Vehicle 
ORDER BY dailyRate DESC;

SELECT V.*
FROM Vehicle V
JOIN Lease L ON V.vehicleID = L.vehicleID
WHERE L.customerID = 3;

SELECT TOP 1 *
FROM Lease
ORDER BY endDate DESC;

SELECT * 
FROM Lease 
WHERE customerID = 5
AND CAST(endDate AS DATE) > CAST(GETDATE() AS DATE);



SELECT * FROM Payment
WHERE YEAR(transactionDate) = 2023;

SELECT * FROM Customer C
WHERE C.customerID NOT IN (SELECT L.customerID FROM Lease L
                           JOIN Payment P ON L.leaseID = P.leaseID);



SELECT V.vehicleID, V.make, V.model, V.year, V.dailyRate, V.status, V.passengerCapacity, V.engineCapacity, 
       SUM(P.amount) AS totalPayments
FROM Vehicle V
JOIN Lease L ON V.vehicleID = L.vehicleID
JOIN Payment P ON L.leaseID = P.leaseID
GROUP BY V.vehicleID, V.make, V.model, V.year, V.dailyRate, V.status, V.passengerCapacity, V.engineCapacity;

SELECT C.customerID, C.firstName, C.lastName, SUM(P.amount) AS totalPayments
FROM Customer C
JOIN Lease L ON C.customerID = L.customerID
JOIN Payment P ON L.leaseID = P.leaseID
GROUP BY C.customerID, C.firstName, C.lastName;

SELECT L.leaseID, V.*
FROM Lease L
JOIN Vehicle V ON L.vehicleID = V.vehicleID;

SELECT C.*, V.*, L.*
FROM Lease L
JOIN Customer C ON L.customerID = C.customerID
JOIN Vehicle V ON L.vehicleID = V.vehicleID
WHERE L.endDate >= GETDATE();

SELECT TOP 1 C.customerID, C.firstName, C.lastName, SUM(P.amount) AS totalSpent
FROM Customer C
JOIN Lease L ON C.customerID = L.customerID
JOIN Payment P ON L.leaseID = P.leaseID
GROUP BY C.customerID, C.firstName, C.lastName
ORDER BY totalSpent DESC;

SELECT V.vehicleID, V.make, V.model, V.year, V.dailyRate, V.status, V.passengerCapacity, V.engineCapacity, 
       L.leaseID, L.customerID, L.startDate, L.endDate, L.type AS leaseType
FROM Vehicle V
LEFT JOIN Lease L ON V.vehicleID = L.vehicleID AND L.endDate >= GETDATE();

-- Get the current date

-- Declare the customer ID you are interested in
-- Declare the customer ID and current date
DECLARE @CustomerID INT = 3; -- Replace with the specific customerID you want to query
DECLARE @CurrentDate DATE = CAST(SYSDATETIME() AS DATE);

-- Retrieve active leases for the specific customer
SELECT C.customerID, C.firstName, C.lastName, C.email, C.phoneNumber,
       V.vehicleID, V.make, V.model, V.year, V.dailyRate, V.status,
       L.leaseID, L.startDate, L.endDate, L.type AS leaseType
FROM Lease L
JOIN Customer C ON L.customerID = C.customerID
JOIN Vehicle V ON L.vehicleID = V.vehicleID
WHERE C.customerID = @CustomerID
AND L.endDate >= @CurrentDate;


-- Update end dates to future dates for testing
UPDATE Lease
SET endDate = DATEADD(MONTH, 6, GETDATE()) -- Adds 6 months to the current date
WHERE endDate < GETDATE(); -- Ensures only past end dates are updated

-- Define the customer ID you want to query
DECLARE @CustomerID INT = 3; -- Replace with the specific customerID you want

-- Get the current date
DECLARE @CurrentDate DATE = CAST(GETDATE() AS DATE);

-- Query to retrieve active leases for the specified customer
SELECT C.customerID, C.firstName, C.lastName, C.email, C.phoneNumber,
       V.vehicleID, V.make, V.model, V.year, V.dailyRate, V.status,
       L.leaseID, L.startDate, L.endDate, L.type AS leaseType
FROM Lease L
JOIN Customer C ON L.customerID = C.customerID
JOIN Vehicle V ON L.vehicleID = V.vehicleID
WHERE C.customerID = @CustomerID
AND L.endDate >= @CurrentDate;

-- Define the current date
DECLARE @CurrentDate DATE = CAST(GETDATE() AS DATE);

-- Retrieve details of active leases with customer and car information
SELECT 
    C.customerID, 
    C.firstName, 
    C.lastName, 
    C.email, 
    C.phoneNumber,
    V.vehicleID, 
    V.make, 
    V.model, 
    V.year, 
    V.dailyRate, 
    V.status,
    L.leaseID, 
    L.startDate, 
    L.endDate, 
    L.type AS leaseType
FROM Lease L
JOIN Customer C ON L.customerID = C.customerID
JOIN Vehicle V ON L.vehicleID = V.vehicleID
WHERE L.endDate >= @CurrentDate;
