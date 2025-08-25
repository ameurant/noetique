.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install development environment
install: .venv/bin/buildout
	.venv/bin/buildout -c development.cfg

.PHONY: start  # Start Zope instance
start:
	bin/instance fg

.PHONY: clean  # Clean development environment
clean:
	rm -rf .venv bin develop-eggs eggs include lib parts .installed.cfg pyvenv.cfg

.venv/bin/buildout:
	uv venv
	uv pip install -r https://dist.plone.org/release/6.1.2/requirements.txt
