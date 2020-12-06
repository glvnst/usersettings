.PHONY: advise package publish clean

advise:
	@echo "This Makefile is for developers, not users."
	@echo "To build/install usersettings, see docs/INSTALL.txt"

package:
	python ./setup.py sdist bdist_wheel

publish: clean package
# prod:
#   TWINE_REPOSITORY_URL="https://upload.pypi.org/legacy/"
	TWINE_REPOSITORY_URL="$${TWINE_REPOSITORY_URL:-https://test.pypi.org/legacy/}" \
	  python3 -m twine upload --username '__token__' dist/*

clean:
	python ./setup.py clean
	rm -rf usersettings.egg-info dist build __pycache__


