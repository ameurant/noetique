# Site Noétique de Marc Halévy

Plone 6.1 Classic Product for http://www.noetique.eu web site.

## Production installation

    git clone https://github.com/ameurant/noetique.git noetique6
    cd noetique6
    python3.12 -m venv .
    ./bin/pip install -r https://dist.plone.org/release/6.1.2/requirements.txt
    ./bin/buildout

## Development installation

    git clone https://github.com/ameurant/noetique.git
    cd noetique
    make install
    make start
    open http://localhost:1920


## Theme development

    npm install
    npm run watch

## Build theme

    npm run build
