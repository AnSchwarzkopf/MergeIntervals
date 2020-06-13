build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf merge_pkg_AnSchwarzkopf.egg-info
	
unit-test:
	python3 -m py.test tests/test_merge.py

performance-test:
	python3 tests/test_performance.py