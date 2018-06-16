drop database if exists pokemon; 
create database if not exists pokemon;
use pokemon;

create table if not exists tbl_pokemon (
	id int primary key not null auto_increment,
	nom varchar(255) unique
);

create table if not exists tbl_type (
	id int primary key not null auto_increment,
    designation varchar(255) unique
);

create table if not exists tbl_caracteristique (
	desi_transformation varchar(255),
	ref_pokemon int not null,
    ref_Type1 int not null, 
    ref_Type2 int,
    hp int default 0,
    attack int default 0,
    defense int default 0,
    speed_Attack int default 0,
    speed_Defense int default 0,
    speed int default 0,
    constraint fk_caracteristique_pokemon foreign key (ref_pokemon) references tbl_pokemon(id) on delete cascade,
    constraint fk_caracteristique_type1 foreign key (ref_type1) references tbl_type(id) on delete cascade,
    constraint fk_caracteristique_type2 foreign key (ref_type2) references tbl_type(id) on delete set null
);

CREATE UNIQUE INDEX idx_caracteristique ON tbl_caracteristique (ref_pokemon, desi_transformation, ref_type1, ref_type2); 

-- DELIMITER $$

DROP PROCEDURE IF EXISTS findalltype;
-- $$
create PROCEDURE findalltype()
begin
	select id, designation 
    from tbl_type 
    order by designation;
end;
-- $$

DROP PROCEDURE IF EXISTS inserttype;
-- $$
create PROCEDURE  inserttype(in designationtype varchar(255), out msgcode int)
begin
	declare exit handler for 1062 select 900 into msgcode;-- concat('Le type ',designationtype,' existe déjà.') as msg;
    
	insert into tbl_type (designation) 
    values (trim(lcase(designationtype)));
end;
-- $$

DROP PROCEDURE IF EXISTS updatetype;
-- $$
create PROCEDURE updatetype(in olddesignationtype varchar(255), in newdesignationtype varchar(255), out msgcode int)
begin
	declare exit handler for 1062 select 900 into msgcode;-- concat('Le type ',designationtype,' existe déjà.') as msg;
    
	update tbl_type t 
    set t.designation=trim(lcase(newdesignationtype)) 
    where t.designation=trim(lcase(olddesignationtype));
end;
-- $$

DROP PROCEDURE IF EXISTS deletetype;
-- $$
create PROCEDURE deletetype(in designationtype int)
begin
	delete from tbl_type 
    where designation=trim(lcase(designationtype));
end;
-- $$



DROP PROCEDURE IF EXISTS findallpokemon;
-- $$
create PROCEDURE findallpokemon()
begin
	select id, nom 
    from tbl_pokemon 
    order by nom;
end;
-- $$

DROP PROCEDURE IF EXISTS insertpokemon;
-- $$
create PROCEDURE  insertpokemon(in nompokemon varchar(255), out msgcode int)
begin
	declare exit handler for 1062 select 900 into msgcode; -- concat('Le pokemon ',nompokemon,' existe déjà.') as msg;
    
	insert into tbl_pokemon(nom) 
    values (trim(lcase(nompokemon)));
end;
-- $$

DROP PROCEDURE IF EXISTS updatepokemon;
-- $$
create PROCEDURE  updatepokemon(in nompokemon int, in nouveaunompokemon varchar(255), out msgcode int)
begin
	declare exit handler for 1062 select 900 into msgcode; -- concat('Le pokemon ',nompokemon,' existe déjà.') as msg;
    
	update tbl_pokemon p 
    set p.nom=trim(lcase(nouveaunompokemon)) 
    where p.nom=trim(lcase(nompokemon));
end;
-- $$

DROP PROCEDURE IF EXISTS deletepokemon;
-- $$
create PROCEDURE  deletepokemon(in nompokemon int)
begin
	delete from tbl_pokemon 
    where nom=trim(lcase(nompokemon));
end;
-- $$


DROP PROCEDURE IF EXISTS findfeature;
-- $$
create PROCEDURE  findfeature(in nompokemon varchar(255)) -- , in designationtransformation varchar(255), in designationtype1 varchar(255), in designationtype2 varchar(255))
begin
	select  p.nom, c.desi_transformation, t1.designation, t2.designation, c.hp, c.attack, c.defense, c.speed_Attack, c.speed_Defense, c.speed, (c.hp+c.attack+c.defense+c.speed_Attack+c.speed_Defense+c.speed) as total
	from tbl_pokemon p 
		inner join tbl_caracteristique c on c.ref_pokemon=p.id 
			inner join tbl_type t1 on c.ref_type1=t1.id 
				inner join tbl_type t2 on c.ref_type2=t2.id 
	where p.nom=trim(lcase(nompokemon)); -- and c.desi_transformation=trim(lcase(designationtransformation)) and t1.designation=trim(lcase(designationtype1)) and t2.designation=trim(lcase(designationtype2));
end;
-- $$

DROP PROCEDURE IF EXISTS insertfeature;
-- $$
create PROCEDURE  insertfeature(in nompokemon varchar(255), in designationtransformation varchar(255), in designationtype1 varchar(255), in designationtype2 varchar(255), in paramhp int, in paramattack int, in paramdefense int, in paramspeed_Attack int, in paramspeed_Defense int, in paramspeed int, out msgcode int)
begin
	declare exit handler for 1062 select 900 into msgcode; -- concat('Les caracteristique existe déjà poour ce pokemon donner une autre designation de transformation.') as msg;
	declare exit handler for 1048 select 800 into msgcode; --  concat('Erreur references pokemon, type1 ou type2 inexistante.') as msg;
    
	insert into tbl_caracteristique (desi_transformation, ref_pokemon, ref_Type1, ref_Type2, hp, attack, defense, speed_Attack, speed_Defense, speed)
	values (trim(lcase(designationtransformation)), (select id from tbl_pokemon where nom=trim(lcase(nompokemon))), (select id from tbl_type where designation=trim(lcase(designationtype1))), (select id from tbl_type where designation=trim(lcase(designationtype2))), paramhp, paramattack, paramdefense, paramspeed_Attack, paramspeed_Defense, paramspeed);
end;-- $$

DROP PROCEDURE IF EXISTS updatefeature;
-- $$
create PROCEDURE  updatefeature(in nompokemon varchar(255), in designationtransformation varchar(255), in designationtype1 varchar(255), in designationtype2 varchar(255), in paramhp int, in paramattack int, in paramdefense int, in paramspeed_Attack int, in paramspeed_Defense int, in paramspeed int, out msgcode int)
begin
	declare exit handler for 1062 select 900 into msgcode; -- concat('Les caracteristique existe déjà poour ce pokemon donner une autre designation de transformation.') as msg;
    
	update tbl_caracteristique c
	set c.desi_transformation=trim(lcase(designationtransformation)), 
		c.hp=paramhp, 
		c.attack=paramattack, 
        c.defense=paramdefense, 
        c.speed_Attack=paramspeed_Attack, 
        c.speed_Defense=paramspeed_Defense, 
        c.speed=paramspeed
	where c.ref_pokemon=(select p.id from tbl_pokemon p where p.nom=trim(lcase(nompokemon))) 
		and c.desi_transformation=trim(lcase(designationtransformation)) 
        and c.ref_type1=(select t1.id from tbl_type t1 where t1.designation=trim(lcase(designationtype1)))
        and c.ref_type2=(select t2.id from tbl_type t2 where t2.designation=trim(lcase(designationtype2)));
end;
-- $$

DROP PROCEDURE IF EXISTS deletefeature;
-- $$
create PROCEDURE  deletefeature(in nompokemon varchar(255), in designationtransformation varchar(255), in designationtype1 varchar(255), in designationtype2 varchar(255))
begin
	delete c 
    from tbl_pokemon p 
		inner join tbl_caracteristique c on c.ref_pokemon=p.id 
			inner join tbl_type t1 on c.ref_type1=t1.id inner join tbl_type t2 on c.ref_type2=t2.id
	where p.nom=trim(lcase(nompokemon)) 
		and c.desi_transformation=trim(lcase(designationtransformation)) 
        and t1.designation=trim(lcase(designationtype1)) 
        and t2.designation=trim(lcase(designationtype2));
end;
-- $$

-- DELIMITER ;