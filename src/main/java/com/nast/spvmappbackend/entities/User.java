package com.nast.spvmappbackend.entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="user")
public class User {
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private int id;
	
	@Column(name="name")
	private String name;
	
	@Column(name="serial_num")
	private String serial_num;
	
	/*public User(String name, String serial_num, int curr_count) {
		super();
		this.name = name;
		this.serial_num = serial_num;
		this.curr_count = curr_count;
	}*/

	public int getCurr_count() {
		return curr_count;
	}

	public void setCurr_count(int curr_count) {
		this.curr_count = curr_count;
	}

	@Column(name="curr_count")
	private int curr_count;

	



	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSerial_num() {
		return serial_num;
	}

	public void setSerial_num(String serial_num) {
		this.serial_num = serial_num;
	}

	

}
