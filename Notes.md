# Signed Certificate Timestamps

See
[How CT fits into the wider Web PKI ecosystem](https://certificate.transparency.dev/howctworks/)
for details on how this works.

Signed certificate timestamps and pre-certificate timestamps are created by the log

Pre-certificate issuer = Transparency Log

- Server sends certificate request
- CA service creates pre-certificate
- CA service sends pre-certificate to log
- log service adds pre-certificate to log
- log service adds pre-certificate timestamp to certificate before returning it to the CA
- CA sends certificate with pre-certificate info attached to Server OR
- CA sends final certificate to log service

Log service has a CA that all certificates added to the log need to be signed by

pre-certificate signed certificate timestamps are created before sending certificate back to CA

When the certificate returns to the CA with the pre-certificate signed certificate timestamps the CA can sned the final certificate to the log service and the 'certificate signed certificate timestamps' are added to the certificate before sending on to the server.
