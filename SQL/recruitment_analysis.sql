-- 1. View all data
SELECT * FROM cleaned_recruitment;

-- 2. Average Time to Hire by Source
SELECT 
  Source, 
  ROUND(AVG(Time_to_Hire), 2) AS avg_days 
FROM cleaned_recruitment 
GROUP BY Source;

-- 3. Top Recruiter Performance (Hired only)
SELECT 
  Recruiter_Name, 
  COUNT(*) AS hires 
FROM cleaned_recruitment 
WHERE Status='Hired' 
GROUP BY Recruiter_Name
ORDER BY hires DESC;