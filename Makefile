init:
	python -m pip install -r requirements.txt

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf merge_pkg_AnSchwarzkopf.egg-info
	
unit-test:
	python -m py.test tests/test_merge.py

performance-test:
	python tests/test_performance.py