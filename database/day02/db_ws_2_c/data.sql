SELECT "BillingCountry", sum("Total") sumTotal
FROM invoices
GROUP BY "BillingCountry";

SELECT strftime('%Y', "InvoiceDate") year, sum("Total") total_sum
FROM invoices
GROUP BY year;

SELECT "BillingState", SUM("Total") AS TotalSales
FROM invoices
WHERE "BillingCountry" = 'USA' AND "InvoiceDate" > '2010-01-01'
GROUP BY "BillingState";

SELECT "BillingCountry", max("Total") MaxOrderAmount
FROM invoices
WHERE "BillingCountry" = 'Germany' OR "BillingCountry" = 'France'
GROUP BY "BillingCountry";
