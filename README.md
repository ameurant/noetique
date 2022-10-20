# Site Noétique de Marc Halévy

Plone 6 Classic Product for http://www.noetique.eu web site.


## Development installation

    git clone https://github.com/ameurant/noetique.git
    cd noetique
    python3.9 -m venv .
    ./bin/pip install -r https://dist.plone.org/release/6.0.0b3/requirements.txt
    ./bin/buildout -c development.cfg


## Start instance

    ./bin/instance fg
    open http://localhost:8080

## Theme development

    npm install
    npm run watch

## Build theme

    npm run build
