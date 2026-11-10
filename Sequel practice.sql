--question 175
SELECT 
p.firstName,
p.lastname,
a.city,
a.state
FROM Person p
LEFT JOIN Address a
ON p.personID = a.personId;


-- question 176

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    Order by salary DESC
    Limit 1 OFFSET 1
) AS SecondHighestSalary

-- Question 177
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
      SET N = N - 1;
      RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END