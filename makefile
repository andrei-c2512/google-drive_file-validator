#!/bin/bash

# general variables
VIRTUAL_DIR=env
PY=$(VIRTUAL_DIR)/bin/python3
PIP=$(VIRTUAL_DIR)/bin/pip

.PHONY: tests
# 

LIBS=google-auth-oauthlib google-auth-httplib2 oauth2client google-api-python-client 

# set-up related rules
set-up-deb:
	@echo "Installing python"
	sudo apt install python3
	@echo "Installing python virtual enviroment"
	sudo apt install python3.11-venv
	@echo "Creating a virtual enviroment called "$(VIRTUAL_DIR)""
	python3 -m venv $(VIRTUAL_DIR)	
	@echo "Installing the 3rd party libraries"
	$(PIP) install $(LIBS)
	@echo "Done"
set-up-win:	
	py -m venv $(VIRTUAL_DIR)	
	@echo "Installing the 3rd party libraries"
	$(PIP) install $(LIBS)
	@echo "Done"
# set-up end

DRIVE_ID=0ANtwa3WJVNrUUk9PVA 
# 0ANtwa3WJVNrUUk9PVA 
FOLDER_ID_1=1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A 
FOLDER_ID_2=1IluQF5LFvOshpHJNTl4IIF30EEIS2akm
SRC=src/main.py
RUN=$(PY) $(SRC)

# Running rules for quick tests and testing itself
config:
	$(RUN) config --list DRIVE_ID=$(DRIVE_ID) DATE_PATTERN=YYYY-MM-DD

single:
	$(RUN) validate -d $(DRIVE_ID) -f $(FOLDER_ID_1) --lifetime 30 -p YYYY-MM-DD

tests:
	$(PY) -m unittest tests/test_file_filter.py

sample:
	$(RUN) validate -d $(DRIVE_ID) -f $(FOLDER_ID_1) --lifetime 30 -p 1231231  
	$(RUN) validate -d $(DRIVE_ID) -f $(FOLDER_ID_2) --lifetime 30 -p 231231231 
# testing end

TREE_IGNORE=$(VIRTUAL_DIR)|__pycache__

# Utility rules
dep-list:
	$(PIP) freeze && $(PIP) list > requirements.txt

## this is for the tree command I have on linux
tree:
	tree -I "$(TREE_IGNORE)"
diff:
	@git status
	@git diff --stat
# utility end



