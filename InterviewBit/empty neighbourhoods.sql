select d.name from neighborhoods as d
left join users u
on u.neighborhood_id = d.id
group by d.id
having count(u.id) = 0 