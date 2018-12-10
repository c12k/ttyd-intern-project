DROP DATABASE IF EXISTS retail;
CREATE DATABASE retail;

DROP TABLE IF EXISTS txn;
CREATE TABLE txn(
  id serial primary key,
  InvoiceNo text,
  StockCode text,
  Description text,
  Quantity numeric,
  InvoiceDate date,
  UnitPrice numeric,
  CustomerID numeric,
  Country text);
  
COPY txn(InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) 
FROM '/Users/cmc/Code/ttyd-intern-project/Sample-data/OnlineRetail.csv' 
DELIMITER ',' CSV HEADER;