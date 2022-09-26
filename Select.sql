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

select genre_id , count (distinct composer_id) from composer_genre
	group by genre_id


select a.name, year, count(t.name) from albums a 
left join tracks t on t.album_id = a.id
group by a.name, year
having year in('2019', '2020')
order by a.name;


select a.name, AVG(duration) from albums a 
join tracks t on t.album_id = a.id
group by a.name
order by avg desc;


select composer_id, album_id, year from album_composer ac 
join albums a on ac.id = a.id
group by composer_id, album_id, year 
having year not in ('2020')
order by composer_id;


select co.name, ca.name from composers co
join album_composer ac on co.id = ac.composer_id 
join albums a on ac.album_id = a.id
join catalogue ca on a.catalogue_id = ca.id
 where co.name in ('Tapok');





