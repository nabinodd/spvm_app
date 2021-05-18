package com.nast.spvmappbackend.services;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.nast.spvmappbackend.entities.User;
import com.nast.spvmappbackend.repository.UserRepository;

@Service("userService")
public class UserServiceImpl implements UserService{
	@Autowired
	private UserRepository userRepository;

	@Override
	public Iterable<User> findAll() {
		
		return userRepository.findAll();
				
	}

	@Override
	public User findById(int id) {
		// TODO Auto-generated method stub
		return userRepository.findById(id).get();
	}

	@Override
	public User save(User user) {
		User newUser=new User();
		newUser.setName(user.getName());
		newUser.setSerial_num(user.getSerial_num());
		newUser.setCurr_count(user.getCurr_count());
		return newUser;
	}

	@Override
	public void delete(int id) {
		userRepository.deleteById(id);
		
	}

}
