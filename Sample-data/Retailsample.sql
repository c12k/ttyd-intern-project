select extract (month from invoicedate) as mth,
stockcode, count(stockcode), sum(unitprice*quantity) as total
from txn 
group by invoicedate, stockcode
order by mth, total desc
limit 5;