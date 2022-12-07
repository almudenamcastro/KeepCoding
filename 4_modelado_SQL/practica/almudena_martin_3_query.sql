/*
	Almudena Martín Castro. Práctica de SQL
*/

--- Query ---

select cb.brand_name, cm.model_name, c.plate, c2.color_name, bg.group_name, c.purchase_dt, c.kilometers, c.insurance_nr, ic.ins_company_name
from almudena_martin_castro.cars c 
	left join almudena_martin_castro.car_models cm on c.model_id = cm.model_id 
	left join almudena_martin_castro.car_brands cb on cm.brand_id = cb.brand_id 
	left join almudena_martin_castro.brand_groups bg on cb.group_id = bg.group_id 
	left join almudena_martin_castro.colors c2 on c.color_id =c2.color_id 
	left join almudena_martin_castro.ins_companies ic on c.ins_company_id =ic.ins_company_id 