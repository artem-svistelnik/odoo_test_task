ifeq (cmd, $(firstword $(MAKECMDGOALS)))
  runargs := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
  $(eval $(runargs):;@true)
  ifeq ($(runargs),)
	runargs := odoo bash
  endif
endif

build:
	docker build . -t odoo-app -f odoo/Dockerfile

run:
	docker compose up

restart:
	docker compose stop && docker compose up -d

stop:
	docker compose stop

cmd:
	docker compose run $(runargs)
