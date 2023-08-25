select n.name
from neighborhoods as n
left join users as u
on n.id = u.neighborhood_id
where u.id is null

--This also works
-- select d.name from neighborhoods as d
-- left join users u
-- on u.neighborhood_id = d.id
-- group by d.id
-- having count(u.id) = 0 
