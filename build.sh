#!/bin/sh -e
# Build the components of the Pax application

case $1 in
    help)
        cat <<EOF

EOF
        ;;
    up)
        cd src
        docker-compose up
        ;;
    down|stop)
        cd src
        docker-compose $1
        ;;
    test)
        cd src/backend
        python manage.py test
        ;;
    all)
        docker build -t pax:latest src/backend/.
        docker build -t pax-gui:latest src/webserver/.
        ;;
esac
