create database animals
use animals

create table roster(Name varchar(30), Species varchar(30),Age int)

INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);


update roster
set name = 'Ezri Dax'
where Name ='Jadzia Dax'

select name,age from roster
where species='Bajoran'


select*from roster