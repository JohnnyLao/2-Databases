-- HW3

select name, year from albums
where year = 2017;

select name, duration from tracks
order by duration desc
limit 1;

select name, duration from tracks
where duration >= 210;

select name, year from catalogue
where year between 2018 and 2020;

select name from composers
where name not like ('% %');

select name from tracks
where name like ('%2');


-- HW 4

select c.name, count (composer_id) from composer_genre co
	join composers c on co.composer_id = c.id
	group by c.name
	order by count desc;


select a.name, year, count(t.name) from albums a 
	left join tracks t on t.album_id = a.id
	group by a.name, year
	having year in('2019', '2020')
	order by a.name;


select a.name, AVG(duration) from albums a 
	join tracks t on t.album_id = a.id
	group by a.name
	order by avg desc;


select c.name, a.name, a.year from album_composer ac 
	join composers c on ac.composer_id = c.id
	join albums a on ac.id = a.id
	group by c.name, a.name, a.year
	having year not in ('2020');


select co.name, c.name from composers co
	join album_composer ac on co.id = ac.composer_id 
	join albums a on ac.album_id = a.id
	join tracks t on t.album_id = a.id
	join tracks_catalogue tc on t.album_id = tc.catalogue_id 
	join catalogue c on tc.catalogue_id = c.id
	where co.name in ('Tapok')
	limit 1;


select a.name, c.name, count(cg.genre_id) from albums a 
	join album_composer ac on a.id = ac.album_id 
	join composers c on ac.id = c.id
	join composer_genre cg on c.id = cg.composer_id 
	group by a.name, c.name
	having count(cg.genre_id) >= 2;


select t.name from tracks t 
	full join tracks_catalogue tc on t.id = tc.track_id 
	full join catalogue c on tc.catalogue_id = c.id 
	where c.name is null;

select c.name, t.name, min(t.duration) from tracks t 
	join albums a on t.album_id = a.id
	join album_composer ac on a.id = ac.composer_id 
	join composers c on ac.id = c.id
	group by c.name, t.name
	order by min(duration)
	limit 3;
	
select a.name, count(table2.name) from albums a 	
	full join 
	(select al.name, t.name, count(distinct al.name) from albums al 
	join tracks t on t.album_id = al.id
	group by al.name, t.name) 
	table2 on a.name = table2.name;
;





