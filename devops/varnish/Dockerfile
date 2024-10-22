# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Brian Davis <info@pimaker.org>" \
      org.label-schema.name="plone-pimaker-site-varnish" \
      org.label-schema.description="Plone PiMaker Site Varnish image." \
      org.label-schema.vendor="Brian Davis"

COPY etc/varnish.vcl /etc/varnish/default.vcl
