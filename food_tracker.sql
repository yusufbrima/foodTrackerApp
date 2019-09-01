CREATE TABLE log_date(
 id INTEGER PRIMARY KEY autoincrement,
 entry_date DATE NOT NULL
);


CREATE TABLE food(
 id INTEGER PRIMARY KEY autoincrement,
 name TEXT  NOT NULL,
 protein INTEGER NOT NULL,
 carbohydrates INTEGER NOT NULL,
 fat INTEGER NOT NULL,
 calories INTEGER  NOT NULL
);

CREATE TABLE food_date(
 food_id INTEGER NOT NULL,
 log_date_id INTEGER NOT NULL,
 PRIMARY KEY(food_id,log_date_id)
);


SELECT f.name AS name, 
f.protein AS protein,
f.carbohydrates AS carbohydrates,
f.fat AS fat,
f.calories AS calories
FROM food AS f jOIN  food_date  ON  food_date.log_date_id =  log_date.id;



SELECT * FROM log_date 
JOIN food_date ON food_date.log_date_id =  log_date.id 
JOIN food on food.id =  food_date.food_id WHERE log_date.entry_date=?;


SELECT food.name, food.protein, food.carbohydrates,food.fat,food.calories FROM log_date 
JOIN food_date ON food_date.log_date_id =  log_date.id
JOIN food on food.id =  food_date.food_id 


--Version 0.1

SELECT name,sum(protein),sum(carbohydrates),sum(fat),sum(calories), log_date.entry_date FROM food_date 
JOIN log_date ON food_date.log_date_id=log_date.id
JOIN food ON food.id =  food_date.food_id GROUP BY log_date.id;


--Version 0.2

SELECT log_date.entry_date, SUM(food.protein) AS total_protein,
 SUM(food.carbohydrates) AS total_carbohydrates,SUM(food.fat) AS total_fat,SUM(food.calories) AS total_calories 
 FROM log_date JOIN food_date ON food_date.log_date_id =  log_date.id 
 JOIN food on food.id =  food_date.food_id GROUP BY log_date.id;



query = "SELECT log_date.entry_date, SUM(food.protein) AS total_protein,SUM(food.carbohydrates) AS total_carbohydrates,SUM(food.fat) AS total_fat,SUM(food.calories) AS total_calories FROM log_date JOIN food_date ON food_date.log_date_id =  log_date.id JOIN food on food.id =  food_date.food_id GROUP BY log_date.id"