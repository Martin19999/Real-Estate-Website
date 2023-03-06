DROP TABLE IF EXISTS houses;

CREATE TABLE houses
(
    house_id INT,
    username VARCHAR(20) NOT NULL,
    name VARCHAR(255),
    qty INT,
    PRIMARY KEY (house_id,username)
);
