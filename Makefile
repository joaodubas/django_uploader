CMD_BASE=python manage.py

SET_TEST=pandora.settings.test

SET_LOCAL=pandora.settings.local
PORT_LOCAL=8061
ADDR_LOCAL=0.0.0.0

test:
	@cd ./pandora; \
	$(CMD_BASE) test --verbosity=2 --settings=$(SET_TEST)

coverage:
	@cd ./pandora; \
	$(CMD_BASE) test \
		--verbosity=2 \
		--with-coverage \
		--cover-package=$(pack) \
		--settings=$(SET_TEST)

run:
	@cd ./pandora; \
	$(CMD_BASE) $(cmd) --settings=$(SET_LOCAL)

runserver:
	@cd ./pandora; \
	$(CMD_BASE) runserver $(ADDR_LOCAL):$(PORT_LOCAL) --settings=$(SET_LOCAL)

shell:
	@cd ./pandora; \
	$(CMD_BASE) shell --settings=$(SET_LOCAL)

start:
	@./bin/gunicorn start

stop:
	@./bin/gunicorn stop

restart:
	@./bin/gunicorn restart

.PHONY: test coverage run runserver shell start stop restart

