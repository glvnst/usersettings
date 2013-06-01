.PHONY: advise package publish check clean

advise:
	@echo "This Makefile is for developers, not users."
	@echo "To build/install usersettings, see docs/INSTALL.txt"

package:
	python ./setup.py sdist bdist_egg
	cheesecake_index -v -p dist/usersettings-*.tar.gz

publish:
	python ./setup.py register sdist bdist_egg upload

check:
	cheesecake_index -v --name=usersettings

clean:
	python ./setup.py clean
	rm -rf usersettings.egg-info dist build


