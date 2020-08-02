create database data;
	use data;
	create table employee(
		employee_id int not null auto_increment,
		username varchar(255),
        password varchar(255),
        primary key(employee_id)
        );
	insert into employee (username, password) values('Admin', '1234567890');
	create table user(
		user_id int not null auto_increment,
	    handlename varchar(255),
	    password   varchar(255),
	    primary key(user_id)
	    );	
	create table indentor(
       indent_id int not null auto_increment,
       indent_date date,
       email
       handlename varchar(255),
       Designation varchar(255),
       indent_approving varchar(255),
       Budget_type varchar(255),
       estimated_cost int,
       expected_delivery_period date,
       order_status varchar(255) DEFAULT "Not Placed",
       placing_date date,
       checkres 
       primary key(indent_id)
       );
	create table main_cat(
        mainitem_id int not null auto_increment,
        item_name varchar(255),
        brand varchar(255),
        quantity int,
        warrenty_period varchar(255),
        primary key(mainitem_id)
		);
	create table sub_cat(
		subitem_id int not null auto_increment,
		item_specification varchar(255),
		primary key(subitem_id)
		);
	create table approves(
        indent_id int not null,
        checkres boolean DEFAULT false,
        primary key(indent_id)
		);
)
create table vendor(
        vendor_id int not null auto_increment,
        vendor_name varchar(255),
        indent_id int,
        primary key(vendor_id)
        );
create table purchase_types(
        indent_id int not null,
        direct_purchase varchar(255),
        local_purchase varchar(255),
        gem varchar(255),
        primary key(indent_id)
		);
CREATE TRIGGER place_order
       AFTER UPDATE ON indentor 
       FOR EACH ROW
       SET NEW.order_status="placed";

CREATE TRIGGER approves
       BEFORE UPDATE ON indentor
       FOR EACH ROW
       SET NEW.checkres=true;
		);
CREATE TRIGGER place_order1
      BEFORE UPDATE ON indentor
       FOR EACH ROW 
       SET NEW.order_date=curdate();