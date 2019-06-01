ui_files:
	sudo `which python` build.py ui_files
	@echo "SIGNALUM >>> generated py code from ui"

dependencies:
	sudo apt-get install bluetooth libbluetooth-dev
	@echo "SIGNALUM >>> install python dependencies"
	pip install -r requirements/linux.txt

dev:
	# build ui files
	make ui_files
	sudo `which python` build.py run

uninstall:
	pip uninstall -r requirements/linux.txt
	@echo "SIGNALUM >>> uninstallation complete"
