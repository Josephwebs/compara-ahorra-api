	
create table producto (
	id BIGSERIAL,
	name VARCHAR(90),
	price INTEGER,
	compare_at_price INTEGER,
	image VARCHAR(200),
	PRIMARY KEY (id)
);

insert into producto (name, price, compare_at_price, image) values('example-t-shirt',10990, 2599, 'https://burst.shopifycdn.com/photos/green-t-shirt.jpg?width=5000'); 
insert into producto (name, price, compare_at_price, image) values('example-t-shirt',11990, 22599, 'https://burst.shopifycdn.com/photos/green-t-shirt.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-t-shirt',12990, 22599, 'https://burst.shopifycdn.com/photos/green-t-shirt.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-hat',13990, 22599, 'https://burst.shopifycdn.com/photos/kids-beanie.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-pants',14990, 22599, 'https://burst.shopifycdn.com/photos/distressed-kids-jeans.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-pants',15990, 22599, 'https://burst.shopifycdn.com/photos/distressed-kids-jeans.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-t-shirt',16990, 22599, 'https://burst.shopifycdn.com/photos/green-t-shirt.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-pants',17990, 22599, 'https://burst.shopifycdn.com/photos/distressed-kids-jeans.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-t-shirt',18990, 22599, 'https://burst.shopifycdn.com/photos/green-t-shirt.jpg?width=5000');
insert into producto (name, price, compare_at_price, image) values('example-pants',19990, 22599, 'https://burst.shopifycdn.com/photos/distressed-kids-jeans.jpg?width=5000');

select * from producto;