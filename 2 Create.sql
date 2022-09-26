-- Задание №1
-- CREATE

create table if not exists Genres (
	id SERIAL primary key,
	name VARCHAR(40) unique not null
	);

create table if not exists Catalogue ( 
	id SERIAL primary key,
	name VARCHAR(40) not null,
	year INTEGER between(1900 and 2050) not null
	);

create table if not exists Albums (
	id SERIAL primary key,
	name VARCHAR(40) not null,
	year INTEGER between(1900 and 2050) not null,
	catalogue_id INTEGER references catalogue(id)
	);

create table if not exists Composers (
	id SERIAL primary key,
	name VARCHAR(40) not null
	);

create table if not exists Composer_Genre ( 
	id SERIAL primary key,
	composer_id INTEGER references Composers (id),
	genre_id INTEGER references Genres (id)
	);

create table if not exists Tracks (
	id SERIAL primary key,
	name VARCHAR(40) not null,
	duration INTEGER between (10 and 6000) not null,
	album_id INTEGER references Albums(id),
	);

create table if not exists Album_Composer ( 
	id SERIAL primary key,
	album_id INTEGER references Albums (id),
	composer_id INTEGER references Composers (id)
	);

create table if not exists tracks_catalogue (
	id SERIAL primary key,
	catalogue_id INTEGER references catalogue (id),
	track_id INTEGER references Tracks (id)
	);


-- ALTER
alter table tracks 
	drop column catalogue_id;