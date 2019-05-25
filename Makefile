.PHONY: ui_files

ui_files:
	scripts/build_ui_files.sh

install:
	sudo apt-get install bluetooth libbluetooth-dev
	pip install -r requirements.txt
	@echo "installation complete"
