drop table if exists usedurl;
drop table if exists unusedurl;
create table usedurl( id int not null auto_increment,
		usedurl varchar(250),
		shijian datetime,
		laiyuan varchar(250),
		PRIMARY KEY(id)
		);
create table unusedurl(
		id int not null auto_increment,
		unusedurl varchar(250),
		shijian datetime,
		laiyuan varchar(250),
		PRIMARY KEY(id)
		);
