-- insert Genres

insert into genres (name) values
	('Rock'),
	('Metal'),
	('Funk'),
	('Punk'),
	('Hard-Rock');

-- Insert Catalogue

insert into catalogue  (name, year) values
	('Rock 1', 2021),
	('Rock 2', 2022),
	('Rock 3', 2019),
	('Rock 4', 2014),
	('Rock 5', 2010),
	('Rock 6', 2018),
	('Rock 7', 2005),
	('Rock 8', 2014);


-- Insert Album

insert into albums  (name, year, catalogue_id) values
	('Album 1', 2017, 1),
	('Album 2', 2014, 2),
	('Album 3', 2019, 2),
	('Album 4', 2020, 3),
	('Album 5', 2021, 4),
	('Album 6', 1998, 4),
	('Album 7', 2010, 7),
	('Album 8', 2008, 1);


-- Insert Tracks

insert into tracks  (name, duration, album_id, catalogue_id) values
	('track 1', 125, 1, 2),
	('track 2', 140, 1, 2),
	('track 3', 60, 2, 3),
	('track 4', 88, 2, 4),
	('track 5', 200, 2, 1),
	('track 6', 195, 2, 3),
	('track 7', 300, 3, 5),
	('track 8', 150, 3, 7),
	('track 9', 128, 4, 7),
	('track 10', 130, 4, 4),
	('track 11', 130, 5, 4),
	('track 12', 40, 6, 7),
	('track 13', 15, 6, 4),
	('track 14', 88, 7, 5),
	('track 15', 99, 8, 6);


-- Insert Composers

insert into composers (name) values
	('Rammstein'),
	('Oomph'),
	('Tapok'),
	('Sum41'),
	('Linkin Park'),
	('Slipknot'),
	('Limp Bizkit'),
	('Skillet');


-- insert composer_genre
insert into composer_genre (composer_id, genre_id) values
	('1', 1),
	('1', 5),
	('2', 1),
	('2', 3),
	('3', 5),
	('4', 1),
	('4', 2),
	('5', 3),
	('6', 5),
	('7', 4),
	('8', 5);
	
insert into album_composer (composer_id, album_id) values
	('1', 1),
	('1', 2),
	('2', 2),
	('2', 3),
	('3', 6),
	('4', 1),
	('4', 2),
	('5', 3),
	('6', 5),
	('7', 7),
	('8', 8);