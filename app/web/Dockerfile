FROM httpd:2.4-alpine

# Website
COPY index.html /usr/local/apache2/htdocs/index.html

# Our minimal config snippet (do NOT replace httpd.conf)
COPY mw.conf /usr/local/apache2/conf/extra/mw.conf

# Include the snippet
RUN echo "Include conf/extra/mw.conf" >> /usr/local/apache2/conf/httpd.conf