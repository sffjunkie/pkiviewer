import pytest
from cryptography.x509 import load_pem_x509_certificate

bad_naming_constraints = """-----BEGIN CERTIFICATE-----
MIICyTCCAbGgAwIBAgIBAjANBgkqhkiG9w0BAQsFADARMQ8wDQYDVQQDDAZSb290
IDIwHhcNMjEwNjAyMTMwMzExWhcNMjEwNzAyMTMwMzExWjAPMQ0wCwYDVQQDDARS
b290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvfhnjWl5hnF1ecJv
kq21AWOfHhPsQT/5juFA/v/goAFatKr40+k7Jy3qQ79FRLBf2l4yMun8K7ZPMFfV
q7q3SliOmLqRq0Uf1Eyh8KdQTWc5QIhNttlDaP8EMDuoTJK2NIUTenV/y5errWNJ
l1a8l+kbI6PuKTyziAi524Hja7BH4nQ5rk2vb3nc4vlRAYZtke2MMeHSxZhvkZj/
UtAfAu2Ql9auc6sfViGuaBc4sShS2F7rmQnJmmf0+qW6y9VoYV68HC7EsO22UDXd
aYhY2To9al04rdL0rDDw018Z8VbcW6lwPOkgfbpQDl9fvuFFfxb/2t7soRsAcuKr
+gbWmQIDAQABoy4wLDAPBgNVHRMBAf8EBTADAQH/MBkGA1UdHgQSMBCgDDAKgQgu
Zm9vLmNvbaEAMA0GCSqGSIb3DQEBCwUAA4IBAQCA9aWhpHdUM/9yx0HRgkW5M8IS
zc83Fzbhv3/32s8H2gplxq+XqfIIdoOosgnaEi01ynPncG6IWqj4hfOuoyoorZA3
cmubAjkHrTu8VaMgZL43SwvyWda7atpCOo7rGdz+LL9hH/jcwhLtEqoB+Tdj6wOp
1O14ndCLi0XXoBezsCpmGtjF7aIunsu6yxJN7b/nTcKh/XSAxjpsa6GlNXTbfJyL
BAUiksQ1KTiW8LyF9IRjckpkf1RH9pqBD8vVeunEpXOUPGOfseL5AAXbvYI6iN70
aCxKkiRwqX7ZK0lL9Oh+hhaVqqdPnGxb+O3ZX/88FvKvWiicnftMx56lzv4H
-----END CERTIFICATE-----
"""


def test_bad_naming_constraints_no_error_when_loading():
    load_pem_x509_certificate(bad_naming_constraints.encode("ascii"))


def test_bad_naming_constraints_error_when_accessing():
    cert = load_pem_x509_certificate(bad_naming_constraints.encode("ascii"))

    with pytest.raises(ValueError):
        for _ext in cert.extensions:
            ...
