from pkiviewer.model.p12 import PKCS12KeyAndCertificateInfo

from pkiviewer.view.theme import Visibility
from pkiviewer.view.console import print_key_oneline
from pkiviewer.view.display.certificate import certificate_display
from pkiviewer.view.visibility import get_element_visibility, Visibility


def p12_display(
    p12_info: PKCS12KeyAndCertificateInfo,
) -> None:
    print_key_oneline("PKCS#12:")

    visibility = get_element_visibility(".P12.Certificate")
    cert = p12_info.get("certificate", None)
    if visibility != Visibility.HIDDEN and cert is not None:
        certificate_display(cert, indent=1)

    visibility = get_element_visibility(".P12.AdditionalCertificates")
    additional_certs = p12_info.get("additional_certs", None)
    if visibility != Visibility.HIDDEN and additional_certs is not None:
        print_key_oneline("Additional Certificates:", indent=1)
        for cert in additional_certs:
            certificate_display(cert, indent=2)

    visibility = get_element_visibility(".P12.PrivateKey")

    # TODO: Private Keys
    # private_key = p12_info.get("private_key", None)
    # if visibility != Visibility.HIDDEN and private_key is not None:
    #     print_key_oneline("Private Key:", indent=1)
