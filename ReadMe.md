# PKI Viewer

Displays information in the terminal from the following PKI file types

- Certificates
- PKCS#12 files
- Certificate Signing Request (Coming Soon™)
- Certificate Revocation List (Coming Soon™)

Also Coming Soon™ is Certificate Transparency information.

## Features

1. Files can be in either PEM or DER formats

1. If a URL is passed a certificate will be downloaded automatically

1. The certificate information can be output to the terminal, an SVG file or an HTML file.

1. The information that is displayed can be configured (either hidden, displayed dim or highlighted)

1. The colors can be configured

1. Uses [rich](https://rich.readthedocs.io/en/latest/) for the
   fancy output/SVG & HTML generation and
   [cryptography](https://cryptography.io/en/latest/) for the low level parsing.

1. It stcks fairly closely to the output from the `openssl` binary

DER format certificates should have the extension '.cer' and PKCS#12 '.p12'

## PKCS#12 Files

If the PKCS#12 file is encrypted you will be prompted to enter the passsword

## Usage

Output certificate information to the terminal

```
pkiviewer testcert.pem   OR   pkiviewer https://bbc.com
```

For example

```
pkiviewer https://bbc.com
```

produces the following output

```
Certificate: https://bbc.com
    Data:
        Version: 1 (0x0)
        Serial Number:
            3e:55:35:3c:c9:9b:cb:59:6e:be:fc:64
        Signature Algorithm: RSA with SHA256
        Issuer: C = BE, O = GlobalSign nv-sa, CN = GlobalSign RSA OV SSL CA 2018
        Validity:
            Not Before: Mar 04 13:51:12 2022 UTC
            Not After:  Apr 05 13:51:11 2023 UTC
        Subject:
            C = GB, ST = London, L = London, O = BRITISH BROADCASTING CORPORATION, CN = www.bbc.com
        Subject Public Key Info:
            Public Key Algorithm: RSA
                RSA Public-Key (2048 bit)
                Modulus:
                    c1:91:f9:55:15:2b:77:96:e3:a5:62:2b:1c:4b:2e:8f:e3:c9:f9:76:bd:91:d4:96:
                    28:7e:2e:b4:a9:6a:62:71:50:74:8e:d9:ef:5d:8d:ab:fc:d9:b8:1a:f8:30:01:82:
                    30:45:15:32:e0:f8:64:53:5d:c2:92:0b:44:29:81:5b:b0:83:bf:df:c5:b4:56:e3:
                    7b:af:54:cf:4c:1f:6c:46:ca:b7:21:ae:bc:f5:48:93:ff:ef:f0:37:7c:16:b3:92:
                    c1:be:36:54:78:e0:06:86:64:c1:74:4d:39:c7:79:2d:1f:e4:99:bd:fc:1b:5e:29:
                    bc:c4:ce:8c:aa:76:81:e0:c6:30:08:ea:21:e1:b9:81:1e:08:ea:7d:31:f3:3f:b3:
                    77:98:71:53:00:45:a6:97:a3:54:f5:25:87:eb:81:97:86:45:ef:47:3d:3e:a4:14:
                    2c:06:9d:18:a2:4e:26:5c:bd:b8:c5:a6:53:5d:65:7b:e9:02:52:77:26:10:b5:44:
                    e1:e0:79:a2:ef:29:d3:1b:37:46:27:67:ef:bb:5e:78:58:05:94:5b:3d:82:d8:4d:
                    d8:28:32:b9:e8:e2:5e:65:58:f8:fc:b0:79:f8:fc:23:4f:6a:33:ff:b8:60:96:9a:
                    bc:9b:8c:46:24:8d:fc:5d:13:19:32:ac:ff:a4:f8:91
                Exponent 65537 (0x10001)
                Fingerprint (SHA256):
                    66:dd:b2:a9:e1:f4:52:2f:3b:06:e3:de:6a:76:b3:f0:18:b8:3a:e5:54:7e:71:15:
                    83:68:5c:d7:6a:3d:17:84
        X509v3 Extensions:
            Authority Key Identifier:
                keyIdentifier:
                    f8:ef:7f:f2:cd:78:67:a8:de:6f:8f:24:8d:88:f1:87:03:02:b3:eb
            Subject Key Identifier:
                7c:48:b3:b1:0d:48:93:a2:d2:f0:ac:f4:f6:13:ef:75:94:cf:80:97
            Key Usage: critical
                Digital Signature, Key Encipherment
            Certificate Policies:
                Policy:
                    GlobalSign Certificate Policy
                    https://www.globalsign.com/en/repository
                Policy:
                    CA/Browser Forum organization-validated
            Subject Alternative Name:
                DNS:www.bbc.com, DNS:www.bbc.co.uk, DNS:bbc.co.uk, DNS:bbcrussian.com,
                DNS:*.bbc.com, DNS:*.bbcrussian.com, DNS:bbc.com
            Basic Constraints:
                cA:FALSE
            Extended Key Usage:
                TLS Web Server Authentication, TLS Web Client Authentication
            CRL Distribution Points:
                Full Name:
                    URI:http://crl.globalsign.com/gsrsaovsslca2018.crl
            Authority Information Access:
                CA Issuers - URI:http://secure.globalsign.com/cacert/gsrsaovsslca2018.crt
                OCSP - URI:http://ocsp.globalsign.com/gsrsaovsslca2018
            CT Precertificate SCTs:
                Signed Certificate Timestamp:
                    Version: 1 (0x0)
                    Log ID:
                        e8:3e:d0:da:3e:f5:06:35:32:e7:57:28:bc:89:6b:c9:
                        03:d3:cb:d1:11:6b:ec:eb:69:e1:77:7d:6d:06:bd:6e
                    Timestamp: Mar 04 13:51:14 2022 UTC
                Signed Certificate Timestamp:
                    Version: 1 (0x0)
                    Log ID:
                        6f:53:76:ac:31:f0:31:19:d8:99:00:a4:51:15:ff:77:
                        15:1c:11:d9:02:c1:00:29:06:8d:b2:08:9a:37:d9:13
                    Timestamp: Mar 04 13:51:13 2022 UTC
                Signed Certificate Timestamp:
                    Version: 1 (0x0)
                    Log ID:
                        55:81:d4:c2:16:90:36:01:4a:ea:0b:9b:57:3c:53:f0:
                        c0:e4:38:78:70:25:08:17:2f:a3:aa:1d:07:13:d3:0c
                    Timestamp: Mar 04 13:51:13 2022 UTC
    Signature: RSA with SHA256
        14:40:09:bd:42:2d:bc:29:4d:da:58:55:87:05:dc:8b:1e:1c:e9:1a:77:c4:cb:b2:
        35:fd:b1:3b:ee:5c:97:ef:c9:b0:bb:c4:3a:9c:88:81:ff:e9:02:9e:91:9e:0e:85:
        5d:32:4e:d5:7f:1c:cd:7b:bc:0b:7b:00:c6:07:3e:b2:c0:0a:eb:9d:f1:a5:28:cf:
        eb:9f:12:d0:da:75:6e:f3:da:74:36:e5:6c:8a:75:41:13:4b:2b:ed:83:24:d1:d1:
        e6:6d:85:60:86:22:b2:c7:ff:61:0d:0d:91:1c:b9:ff:18:00:ed:16:09:5d:74:dd:
        cb:bd:85:ca:5a:46:38:f6:86:07:74:21:24:dd:be:5b:6f:43:e8:64:79:70:65:c7:
        79:0f:44:b2:08:6f:a6:1e:73:4e:9a:e2:6f:0a:5c:ae:99:bf:f9:b3:ef:b2:f4:e6:
        bb:1d:52:92:fd:03:14:00:24:47:0c:00:bb:3b:33:f4:2f:d9:1c:00:fc:e2:57:8d:
        a4:bf:2f:bf:5d:94:c2:ab:48:3e:24:00:39:1f:68:29:f2:e1:ba:24:9f:96:9c:24:
        d1:82:5d:49:70:9a:5f:56:1a:2d:14:c2:6b:02:ab:9f:f1:6b:87:c2:e9:2e:46:c1:
        7a:08:95:94:7c:b4:3a:07:c1:c7:fe:0b:df:c3:48:68
```

Output the certificate to an SVG file

```
pkiviewer --save-svg=cert.svg testcert.pem
```

Output the certificate to an HTML file

```bash
$ pkiviewer --save-html=cert.html testcert.pem
```

For SVG and HTML output the number of columns to output can be set with the `--width` option

## Display Configuration

`pkiviewer` looks for a `pkiviewer.toml` in the current directory. See
`pkiviewer.toml.sample` for all the options.

This file can configure what information is output and the colors.

### Colors

The default colors are

```toml
[theme]
default = "white"
error = "red"
warning = "yellow"
info = "green"
key = "blue"
value = "white"
extension_critical = "yellow"
```

### Information Visibility

The following items control what is output.

```toml
[visibility]
".Header" = "normal"                                           # Header text depending on the file type
".Header.Filename" = "normal"                                  # The filename
".Data" = "normal"                                             # The Data block visibility
".Data.Version" = "normal"                                     # Certiificate version
".Data.SerialNumber" = "normal"                                # Certificate serial number
".Data.Issuer" = "normal"                                      # The name of the org that issued the certificate
".Data.Fingerprint" = "normal"                                 # Fingerprint of the certificate
".Data.Validity" = "normal"                                    # The Validity block
".Data.Validity.Before" = "normal"                             # Date and time from which the certificate is valid
".Data.Validity.After" = "normal"                              # Date and time after which the certificate is invalid
".Data.Subject" = "normal"                                     # Visibility of the certificate subject block
".Data.Subject.Name" = "normal"                                # The subject's name
".Data.Subject.PublicKey" = "normal"                           # The public key
".Data.Subject.PublicKey.Algorithm" = "normal"                 # The public key algorithm

".Data.Extensions" = "normal"                                  # Visibility for all extensions
".Data.Extension.Critical" = "normal"                          # Whether the extension is critical
".Data.Extension.Value" = "normal"                             # Visibility of the value for all extensions

# Individual extension information
".Data.Extension.AuthorityKeyIdentifier" = "normal"
".Data.Extension.AuthorityKeyIdentifier.Value" = "normal"
".Data.Extension.SubjectKeyIdentifier" = "normal"
".Data.Extension.SubjectKeyIdentifier.Value" = "normal"
".Data.Extension.KeyUsage" = "normal"
".Data.Extension.KeyUsage.Value" = "normal"
".Data.Extension.CertificatePolicies" = "normal"
".Data.Extension.CertificatePolicies.Value" = "normal"
".Data.Extension.SubjectAlternativeName" = "normal"
".Data.Extension.SubjectAlternativeName.Value" = "normal"
".Data.Extension.IssuerAlternativeName" = "normal"
".Data.Extension.IssuerAlternativeName.Value" = "normal"
".Data.Extension.BasicConstraints" = "normal"
".Data.Extension.BasicConstraints.Value" = "normal"
".Data.Extension.NameConstraints" = "normal"
".Data.Extension.NameConstraints.Value" = "normal"
".Data.Extension.ExtendedKeyUsage" = "normal"
".Data.Extension.ExtendedKeyUsage.Value" = "normal"
".Data.Extension.CRLDistributionPoints" = "normal"
".Data.Extension.CRLDistributionPoints.Value" = "normal"
".Data.Extension.InhibitAnyPolicy" = "normal"
".Data.Extension.InhibitAnyPolicy.Value" = "normal"
".Data.Extension.AuthorityInformationAccess" = "normal"
".Data.Extension.AuthorityInformationAccess.Value" = "normal"
".Data.Extension.SubjectInformationAccess" = "normal"
".Data.Extension.SubjectInformationAccess.Value" = "normal"
".Data.Extension.CertificateSCTs" = "normal"
".Data.Extension.CertificateSCTs.Value" = "normal"
".Data.Extension.PreCertificateSCTs" = "normal"
".Data.Extension.PreCertificateSCTs.Value" = "normal"

# Signature Information
".Signature" = "normal"                                        # The signature block (alogrithm + value)
".Signature.Algorithm" = "normal"                              # The signature algorithm
".Signature.Value" = "normal"                                  # The signature value
```
