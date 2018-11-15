[![Coverage Status](https://coveralls.io/repos/github/OnyiegoAyub/SENDIT-API/badge.svg?branch=api)](https://coveralls.io/github/OnyiegoAyub/SENDIT-API?branch=api)
[![Build Status](https://travis-ci.org/OnyiegoAyub/SENDIT-API.svg?branch=Bg-bug-fixes-161984113)](https://travis-ci.org/OnyiegoAyub/SENDIT-API)

# BUILD A PRODUCT: SendIT

## Project Overview

API  endpoints for SendIt, a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

## Getting started

   git clone https://github.com/OnyiegoAyub/SendIt-API-CH2
   
   Set up a virtual environment on SendIt-API-CH2 using commamnd: sudo apt install virtualenv
   
   ctivate the virtual environment with source env/bin/activate
   
   Install flask, flask_resful and pytest with sudo apt install flask, sudo apt install flask_restful and sudo apt      install pytest
   
   Use the command pytest to run the tests
   
   To run the application:
   
     -Export flask with the command FLASK_APP=run.py
     
     -Export development environment using command FLASK_ENV=development
     
     -Then Run using the command flask run
      
Test the following endpoints on Postman

## ENDPOINTS

Create a parcel order localhost:5000/api/v1/parcels

Fetch all parcel orders: localhost:5000/api/v1/parcel

Fetch a specific parcel order localhost:5000/api/v1/parcels/101

Cancel the specific parcel order localhost:5000/api/v1/parcels/101/cancel

Fetch all parcel orders by a specific user localhost:5000/api/v1/users/1/parcels

Fetch a specific user localhost:5000/api/v1/users/1

Fetch all users localhost:5000/api/v1/users 
  
## Prerequisites

  Git
  
  Make required installations
  
  Postman

install postman from https://www.getpostman.com/apps

install git from https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/

Output of terminal

git clone https://github.com/OnyiegoAyub/SendIt-API-CH2.git

## Author
  Ayub Onyiego
