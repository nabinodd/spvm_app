package com.nast.spvmappbackend.services;

import com.nast.spvmappbackend.entities.User;

public interface UserService {
	
	public Iterable<User> findAll(); 
	
	public User findById(int id);
	
	public User save(User user);
	
	public void delete(int id);

}
