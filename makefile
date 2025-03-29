#!/bin/bash
VIRTUAL_DIR=env
PY=$(VIRTUAL_DIR)/bin/python3
PIP=$(VIRTUAL_DIR)/bin/pip

MODULE=src
TEST_SRC=src/tests.py
DRIVE_ID=0ANtwa3WJVNrUUk9PVA 
FOLDER_ID_1=1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A 
FOLDER_ID_2=1IluQF5LFvOshpHJNTl4IIF30EEIS2akm


LIBS=google-auth-oauthlib google-auth-httplib2 oauth2client google-api-python-client 


.PHONY: tests

RUN=$(PY) -m $(MODULE)


set-up-deb:
	@echo "Installing python"
	sudo apt install python3
	@echo "Installing python virtual enviroment"
	sudo apt install python3.11-venv
	@echo "Creating a virtual enviroment called "$(VIRTUAL_DIR)""
	$(PY) -m venv $(VIRTUAL_DIR)	
	@echo "Installing the 3rd party libraries"
	$(PIP) install $(LIBS)
	@echo "Done"
set-up-win:	
	$(PY) -m venv $(VIRTUAL_DIR)	
	@echo "Installing the 3rd party libraries"
	$(PIP) install $(LIBS)
	@echo "Done"
config:
	$(RUN) config DRIVE_ID=$(DRIVE_ID) 

single:
	$(RUN) validate -d $(DRIVE_ID) -f $(FOLDER_ID_1) --lifetime 30 -p 1231231  

tests:
	$(PY) $(TEST_SRC) 	

sample:
	$(RUN) validate -d $(DRIVE_ID) -f $(FOLDER_ID_1) --lifetime 30 -p 1231231  
	$(RUN) validate -d $(DRIVE_ID) -f $(FOLDER_ID_2) --lifetime 30 -p 231231231 

