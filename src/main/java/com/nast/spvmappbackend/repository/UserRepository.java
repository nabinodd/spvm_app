package com.nast.spvmappbackend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.nast.spvmappbackend.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User,Integer>{

}
