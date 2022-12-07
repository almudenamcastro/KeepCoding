/*
	Almudena Martín Castro. Práctica de SQL
*/

--------------------------
--- Create the schema ---

create schema almudena_martin_castro authorization qqcdehog;


---------------------------
--- Create the tables ----

-- currencies table --
create table almudena_martin_castro.currencies
(
	currency_id varchar(8) not null default 'EUR',
	currency_name varchar(16) not null
);

alter table almudena_martin_castro.currencies
add constraint currency_PK primary key (currency_id); 

-- brand_groups table --
create table almudena_martin_castro.brand_groups
(
	group_id integer not null,
	group_name varchar(50) not null
);

alter table almudena_martin_castro.brand_groups
add constraint groups_pk primary key (group_id);

-- car_brands table --
create table almudena_martin_castro.car_brands
(
	brand_id integer not null,
	brand_name varchar(50) not null,
	group_id integer not null
);

alter table almudena_martin_castro.car_brands
add constraint brands_pk primary key (brand_id);

alter table almudena_martin_castro.car_brands
add constraint group_fk foreign key (group_id)
references almudena_martin_castro.brand_groups;

-- car_models table --
create table almudena_martin_castro.car_models
(
	model_id integer not null,
	model_name varchar(50) not null,
	brand_id integer not null,
	description varchar(200) null
);

alter table almudena_martin_castro.car_models
add constraint models_pk primary key (model_id);

alter table almudena_martin_castro.car_models
add constraint brand_fk foreign key (brand_id)
references almudena_martin_castro.car_brands;


-- colors table --
create table almudena_martin_castro.colors
(
	color_id varchar(8) not null,
	color_name varchar(16) not null,
	description varchar(200) null
);

alter table almudena_martin_castro.colors
add constraint color_pk primary key (color_id);

-- insurance companies table --
create table almudena_martin_castro.ins_companies
(
	ins_company_id integer not null,
	ins_company_name varchar(50) not null
);

alter table almudena_martin_castro.ins_companies
add constraint ins_companies_pk primary key (ins_company_id);

-- cars table --
create table almudena_martin_castro.cars
(
	car_id integer not null,
	model_id integer not null,
	color_id varchar(8) not null,
	kilometers numeric(12,2) not null, 
	insurance_nr integer not null,
	ins_company_id integer not null,
	plate varchar(10) not null,
	purchase_dt date not null
);

alter table almudena_martin_castro.cars
add constraint cars_PK PRIMARY KEY (car_id);

alter table almudena_martin_castro.cars
add constraint model_FK FOREIGN KEY (model_id) 
references almudena_martin_castro.car_models(model_id);

alter table almudena_martin_castro.cars
add constraint ins_company_FK FOREIGN KEY (ins_company_id) 
references almudena_martin_castro.ins_companies(ins_company_id);

alter table almudena_martin_castro.cars
add constraint color_FK FOREIGN KEY (color_id) 
references almudena_martin_castro.colors(color_id);

-- car checks table --
create table almudena_martin_castro.checks
(
	check_id integer not null,
	car_id integer not null,
	kilometers numeric(12,2) not null,
	check_dt date not null,
	amount numeric(12,2) not null,
	currency_id char(8) not null,
	description varchar(200) null
);

alter table almudena_martin_castro.checks
add constraint check_pk primary key (check_id);

alter table almudena_martin_castro.checks
add constraint car_fk foreign key (car_id)
references almudena_martin_castro.cars;

alter table almudena_martin_castro.checks
add constraint currency_fk foreign key (currency_id)
references almudena_martin_castro.currencies;

-----------------------------
--- Load the data ---

-- load currencies --
insert into almudena_martin_castro.currencies (currency_id, currency_name) VALUES ('EUR', 'Euro');
insert into almudena_martin_castro.currencies (currency_id, currency_name) VALUES ('USD', 'US Dollar');
insert into almudena_martin_castro.currencies (currency_id, currency_name) VALUES ('CNY', 'Yuan Renminbi');

-- load brand_groups --
insert into almudena_martin_castro.brand_groups (group_id, group_name) VALUES ('001', 'BMW Group');
insert into almudena_martin_castro.brand_groups (group_id, group_name) VALUES ('002', 'Daimler');
insert into almudena_martin_castro.brand_groups (group_id, group_name) VALUES ('003', 'FCA');
insert into almudena_martin_castro.brand_groups (group_id, group_name) VALUES ('004', 'Ford');

-- load car_brands --
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('001', '001', 'Mini');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('002', '001', 'Rolls Royce');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('003', '001', 'BMW');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('004', '002', 'Mercedes-Benz');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('005', '002', 'Smart');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('006', '003', 'Alfa Romeo');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('007', '003', 'Chrysler');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('008', '003', 'Fiat');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('009', '003', 'Jeep');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('010', '003', 'Lancia');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('011', '003', 'Maserati');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('012', '004', 'Ford');
insert into almudena_martin_castro.car_brands (brand_id, group_id, brand_name) VALUES ('013', '004', 'Troller');


-- load car_models --
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('001', '005', 'EQ ForTwo', 'eléctrico');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('002', '001', 'Clubman', '');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('003', '003', 'iX1', '');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('004', '001', 'Cooper S ALL4', 'híbrido');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('005', '005', 'Brabus', '');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('006', '008', 'Dolcevita', '');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('007', '008', 'Panda', '');
insert into almudena_martin_castro.car_models (model_id, brand_id, model_name, description) VALUES ('008', '008', 'Cult 1.0', '');

-- load colors --
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('7006M', 'BLUE', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A101', 'GOLD', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A102', 'JAUNE', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A201', 'ORANGE NACRE', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A305', 'ROUGE FLORENTIN', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A405', 'BLANC NUAGE', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A406', 'NOIR', 'Deep black');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A504', 'BLEU OCEAN', 'Manufactured by Aixam');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A505', 'BLEU BORA', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A506', 'BLEU', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A605', 'VERT', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A702', 'GRIS METALLIC', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A706', 'GRIS TWINGO', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A707', 'GRIS', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A721', 'BLUE', '');
insert into almudena_martin_castro.colors (color_id, color_name, description) VALUES ('A741', 'GREY', '');

-- load insurance companies --
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('001', 'Mapfre');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('002', 'Allianz');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('003', 'Mutua Madrileña');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('004', 'Axa');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('005', 'Línea Directa');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('006', 'Reale');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('007', 'Generali');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('008', 'Liberty Seguros');
insert into almudena_martin_castro.ins_companies (ins_company_id, ins_company_name) VALUES ('009', 'Zurich');

-- load cars --
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('001', '005', 'A102', '47299.41', '5314', '006', 'GDO 6602', '2017-01-21');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('002', '004', '7006M', '86841.21', '5064', '003', 'CKC 8703', '2018-06-22');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('003', '002', 'A101', '69463.54', '8826', '009', 'SEI 1952', '2018-03-16');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('004', '004', 'A102', '90161.87', '2736', '006', 'WBL 1123', '2018-07-24');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('005', '007', 'A201', '88495.04', '5775', '008', 'SEG 6993', '2016-06-12');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('006', '002', 'A305', '73689.50', '3696', '006', 'ODF 8331', '2017-05-14');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('007', '001', 'A405', '21261.15', '4189', '009', 'OEU 8213', '2016-05-18');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('008', '004', 'A406', '32268.91', '9631', '008', 'AKG 8866', '2018-05-19');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('009', '005', 'A504', '89253.12', '6853', '007', 'MQZ 4274', '2016-01-18');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('010', '004', 'A505', '68672.26', '1630', '008', 'KFG 1255', '2018-04-29');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('011', '006', 'A506', '90822.43', '2881', '002', 'BMG 7322', '2016-05-12');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('012', '007', 'A605', '79149.09', '3799', '007', 'RLG 3627', '2017-02-22');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('013', '006', 'A702', '99428.04', '2272', '003', 'JCU 1533', '2017-01-27');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('014', '001', 'A706', '20048.61', '7985', '002', 'XLO 1844', '2018-09-12');
insert into almudena_martin_castro.cars (car_id, model_id, color_id, kilometers, insurance_nr, ins_company_id, plate, purchase_dt) VALUES ('015', '005', 'A707', '40958.24', '7330', '005', 'VMC 8541', '2016-05-26');

-- load checks --
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('001', '012', '4972', '2020-05-17', '271.19', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('002', '004', '9496', '2022-06-14', '62.35', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('003', '002', '5871', '2021-09-22', '264.85', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('004', '011', '7463', '2020-06-20', '499.71', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('005', '003', '4125', '2021-04-23', '313.84', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('006', '005', '9233', '2021-08-27', '99.26', 'EUR', 'Leve accidente');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('007', '004', '7697', '2021-06-16', '484.59', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('008', '009', '1667', '2021-08-17', '425.96', 'EUR', 'ITV');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('009', '003', '6047', '2022-07-11', '121.95', 'EUR', 'catástrofe total');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('010', '014', '2829', '2022-02-24', '459.30', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('011', '014', '4060', '2019-02-14', '442.57', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('012', '008', '1043', '2020-02-19', '121.16', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('013', '010', '7901', '2021-08-15', '141.22', 'EUR', 'cristal roto');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('014', '009', '1430', '2018-05-23', '193.52', 'EUR', 'ruedas');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('015', '005', '6507', '2018-07-22', '169.58', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('016', '004', '2541', '2020-07-15', '218.56', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('017', '003', '680', '2021-07-26', '284.76', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('018', '004', '8892', '2021-06-13', '405.22', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('019', '002', '8222', '2019-09-29', '203.02', 'EUR', '');
insert into almudena_martin_castro.checks (check_id, car_id, kilometers, check_dt, amount, currency_id, description) VALUES ('020', '015', '1914', '2019-08-16', '394.97', 'EUR', '');

