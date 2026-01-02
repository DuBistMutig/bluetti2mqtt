ARG BUILD_FROM
FROM $BUILD_FROM

# Copy data for add-on
COPY rootfs /

COPY bluetti_mqtt /tmp/bluetti_mqtt
RUN apk add --update --no-cache \
		bluez \
	&& pip install /tmp/bluetti_mqtt \
	&& rm -rf /tmp/bluetti_mqtt \
	&& rm -rf /var/cache/apk/* /lib/apk/db/* \
	&& chmod a+x /run.sh

CMD [ "/run.sh" ]
