DROP TABLE IF EXISTS comments_table;

CREATE TABLE comments_table
(
    comment_id INT AUTO_INCREMENT,
    username VARCHAR(255),
    url VARCHAR(255) NOT NULL,
    comment TEXT,
    PRIMARY KEY (comment_id)
);
