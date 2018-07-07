-- Projects DB Exercises Solutions
--1
SELECT project.name FROM project
  JOIN project_uses_tech ON project.id = project_uses_tech.project_id
  JOIN tech ON project_uses_tech.tech_id = tech.id
  WHERE tech.name = 'Java';
  --No records found
--2
SELECT tech.name FROM project
  JOIN project_uses_tech ON project.id = project_uses_tech.project_id
  JOIN tech ON project_uses_tech.tech_id = tech.id
  WHERE project.name = 'Personal Website';
  --HTML/CSS

--3
SELECT * FROM tech 
  LEFT JOIN project_uses_tech ON tech.id = project_uses_tech.tech_id
  WHERE project_uses_tech.tech_id IS NULL;
--Ruby/JavaScript/Java
--4
SELECT project.name, COUNT(tech.id) FROM tech
  LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id
  JOIN project ON project_uses_tech.project_id = project.id
  GROUP BY project.name;
--5
SELECT * FROM project 
  LEFT JOIN project_uses_tech ON project.id = project_uses_tech.project_id
  WHERE project_uses_tech.project_id  NULL;
--Whiteboard Exercise
--6
SELECT tech.name, COUNT(tech.id) FROM tech
  LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id
  JOIN project ON project_uses_tech.project_id = project.id
  GROUP BY tech.name;
--7
SELECT project.name, tech.name FROM tech
  LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id
  JOIN project ON project_uses_tech.project_id = project.id;
--8
SELECT DISTINCT(tech.name) FROM tech
  LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id
  JOIN project ON project_uses_tech.project_id = project.id;
--9
SELECT DISTINCT(tech.name) FROM tech
  LEFT OUTER JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id
  WHERE project_uses_tech.tech_id IS NULL;
--10
SELECT DISTINCT(project.name) FROM project
  JOIN project_uses_tech ON project.id = project_uses_tech.project_id;
--11
SELECT DISTINCT(project.name) FROM project
  LEFT JOIN project_uses_tech ON project.id = project_uses_tech.project_id
  WHERE project_uses_tech.project_id IS NULL;
--12
SELECT name, COUNT(project_uses_tech.tech_id) FROM project
  LEFT JOIN project_uses_tech ON project.id = project_uses_tech.project_id
  GROUP BY project.name
  ORDER BY COUNT(project_uses_tech.tech_id) DESC;
--13
SELECT name, COUNT(project_uses_tech.project_id) FROM tech
  LEFT JOIN project_uses_tech ON tech.id = project_uses_tech.tech_id
  GROUP BY tech.name
  ORDER BY COUNT(project_uses_tech.project_id) DESC;
--14
SELECT AVG(count) FROM (
  SELECT name, COUNT(project_uses_tech.tech_id) FROM project
    LEFT JOIN project_uses_tech ON project.id = project_uses_tech.project_id
    GROUP BY project.name
    ORDER BY COUNT(project_uses_tech.tech_id) DESC
   )
AS acount;