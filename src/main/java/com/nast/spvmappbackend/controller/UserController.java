package com.nast.spvmappbackend.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.nast.spvmappbackend.entities.User;
import com.nast.spvmappbackend.exception.ResourceNotFoundException;
import com.nast.spvmappbackend.repository.UserRepository;
import com.nast.spvmappbackend.services.UserServiceImpl;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
@RequestMapping("/api/v1/")
public class UserController {
	
	@Autowired
	private UserRepository userRepository;
	
	
	//get all users:
	@GetMapping("/users")
	public List<User> getAllUsers(){
		
		return userRepository.findAll();
		//return (List<User>) userService.findAll();// userRepository.findAll();
	
	}
	
	//get user by Id rest api
		@GetMapping("/users/{id}")
		public ResponseEntity<User> getUserById(@PathVariable int id){
			User user=userRepository.findById(id)
					.orElseThrow(()->new com.nast.spvmappbackend.exception.ResourceNotFoundException("User do not exist for id:"+id));
			return ResponseEntity.ok(user);
		}
		
		// create user rest api
		@PostMapping("/users")
		public User createUser(@RequestBody User user) {
			System.out.println("going to save in db..");
			return userRepository.save(user);
		}
		
		//update user rest api
		@PutMapping("/users/{id}")
		public ResponseEntity<User> updateUser(@PathVariable Integer id,@RequestBody User updateUserDetails){
			//User user1=userService.findById(3);
			User user=userRepository.findById(id)
					.orElseThrow(()->new ResourceNotFoundException("User do not exist for id:"+id));
			user.setName(updateUserDetails.getName());
			user.setSerial_num(updateUserDetails.getSerial_num());
			user.setCurr_count(updateUserDetails.getCurr_count());
			User updatedUser=userRepository.save(user);
			return ResponseEntity.ok(updatedUser);
		}
		
		//delete employee rest api
		@DeleteMapping("/users/{id}")
		public ResponseEntity<Map<String,Boolean>> deleteUser(@PathVariable Integer id){
			User user=userRepository.findById(id)
					.orElseThrow(()->new ResourceNotFoundException("User do not exist for id:"+id));
			userRepository.delete(user);
			Map<String,Boolean> response=new HashMap<>();
			response.put("deleted", Boolean.TRUE);
			return ResponseEntity.ok(response);
		}

}