#!/bin/bash
export PYTHONCACHEPREFIX=./build

SRC=src/main.py
TEST_SRC=src/tests.py
DRIVE_ID=0ANtwa3WJVNrUUk9PVA 
FOLDER_ID_1=1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A 
FOLDER_ID_2=1IluQF5LFvOshpHJNTl4IIF30EEIS2akm


LIBS_COMMON=google-auth-oauthlib google-auth-httplib2 oauth2client
LIBS_DEBIAN=googleapi $(LIBS_COMMON)
LIBS_PIP=google-api-python-client $(LIBS_COMMON)


.PHONY: tests

set-up-debian:
	sudo apt install python
	sudo apt install $(addprefix python3-,$(LIBS_DEBIAN))
set-up-pip:
	@echo "This only works if you already have python and pip installed"
	pip install $(LIBS_PIP)

single:
	python3  $(SRC) validate -d $(DRIVE_ID) -f $(FOLDER_ID_1) --lifetime 30 -p 1231231  
tests:
	python3 $(TEST_SRC) 	
sample:
	python3  $(SRC) validate -d $(DRIVE_ID) -f $(FOLDER_ID_1) --lifetime 30 -p 1231231  
	python3  $(SRC) validate -d $(DRIVE_ID) -f $(FOLDER_ID_2) --lifetime 30 -p 231231231 

