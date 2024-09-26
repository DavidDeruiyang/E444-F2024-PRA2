Flasky
======

this repo is a clone of: https://github.com/miguelgrinberg/flasky 

This repository contains the source code examples for the second edition of my O'Reilly book [Flask Web Development](http://www.flaskbook.com).

The commits and tags in this repository were carefully created to match the sequence in which concepts are presented in the book. Please read the section titled "How to Work with the Example Code" in the book's preface for instructions.

For Readers of the First Edition of the Book
--------------------------------------------

The code examples for the first edition of the book were moved to a different repository: [https://github.com/miguelgrinberg/flasky-first-edition](https://github.com/miguelgrinberg/flasky-first-edition).



Activity 1 
run cmd: [$ flask --app hello.py run]

Activity 2
build and run container:
[$ docker build -t flasky .]
[$docker run -d -p 5000:5000 --name flasky_running flasky]
[$docker ps -a]
[$docker logs flasky_running]
[$docker stop flasky_running]

go into container:
[$docker exec -it flasky_running /bin/bash]