CMD_BASE=python manage.py
ROOT_PATH=./uploader

SET_TEST=uploader.settings.test

SET_LOCAL=uploader.settings.local
PORT_LOCAL=8031
ADDR_LOCAL=0.0.0.0

test:
	@cd $(ROOT_PATH); \
	$(CMD_BASE) test --verbosity=2 --settings=$(SET_TEST)

coverage:
	@cd $(ROOT_PATH); \
	$(CMD_BASE) test \
		--verbosity=2 \
		--with-coverage \
		--cover-package=$(pack) \
		--settings=$(SET_TEST)

run:
	@cd $(ROOT_PATH); \
	$(CMD_BASE) $(cmd) --settings=$(SET_LOCAL)

runserver:
	@cd $(ROOT_PATH); \
	$(CMD_BASE) runserver $(ADDR_LOCAL):$(PORT_LOCAL) --settings=$(SET_LOCAL)

shell:
	@cd $(ROOT_PATH); \
	$(CMD_BASE) shell --settings=$(SET_LOCAL)

start:
	@./bin/gunicorn start

stop:
	@./bin/gunicorn stop

restart:
	@./bin/gunicorn restart

.PHONY: test coverage run runserver shell start stop restart

