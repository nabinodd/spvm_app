package com.nast.spvmappbackend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.nast.spvmappbackend.entities.User;

import com.nast.spvmappbackend.services.UserService;


@SpringBootApplication
public class SpvmappbackendApplication {

	
	@Autowired
	private UserService userService;
	
	public static void main(String[] args) {
		SpringApplication.run(SpvmappbackendApplication.class, args);
	}

	/*@Override
	public void run(String... args) throws Exception {
		// TODO Auto-generated method stub
		//System.out.println("Test");
		Demo4();
		
	}*/
	
	public void Demo1(){
		for(User user:userService.findAll()){
			System.out.println("##############");
			System.out.println("Id : " +user.getId());
			System.out.println("Name : "+user.getName());
			System.out.println("Serial Number : "+user.getSerial_num());
			System.out.println("Current Count : "+user.getCurr_count());
			
		}
		
				
	}
	
	public void Demo2(){
		User user1=userService.findById(3);
		System.out.println("##############");
		System.out.println("Id : " +user1.getId());
		System.out.println("Name : "+user1.getName());
		System.out.println("Serial Number : "+user1.getSerial_num());
		System.out.println("Current Count : "+user1.getCurr_count());
	}

	public void Demo3(){
		System.out.println("deleting id:"+5);
		System.out.println("before delete");
		Demo1();
		userService.delete(8);
		System.out.println("after delete");
		Demo1();
		
	}
	
	public void Demo4(){
		User user=new User();
		user.setName("sabin dangi");
		user.setSerial_num("82609");
		user.setCurr_count(4);
		user.setId(5);
		
		user=userService.save(user);
		
		System.out.println("done");
		System.out.println("user id = "+user.getId());
	}

	
	public void Demo5(){
		User user=userService.findById(6);
		System.out.println("##############");
		System.out.println("Id : " +user.getId());
		System.out.println("Name : "+user.getName());
		System.out.println("Serial Number : "+user.getSerial_num());
		System.out.println("Current Count : "+user.getCurr_count());
		System.out.println("##############");
		user.setName("sabin dangi");
		user.setSerial_num("82609");
		user.setCurr_count(4);
		
		userService.save(user);
		
		System.out.println("done");
		
	}
}
