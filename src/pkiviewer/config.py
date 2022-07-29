from typing import cast, Any

import tomli

from pkiviewer.context import _config  # type: ignore
from pkiviewer.types import Configuration, ConfigSection, Visibility

default_theme: dict[str, str] = {
    "default": "white",
    "error": "red",
    "warning": "yellow",
    "info": "green",
    "key": "blue",
    "value": "white",
    "extension_critical": "yellow",
}


VisibilityMapping = {
    "normal": Visibility.NORMAL,
    "hidden": Visibility.HIDDEN,
    "lowlight": Visibility.LOWLIGHT,
    "highlight": Visibility.HIGHLIGHT,
}


default_x509_element_visibility: dict[str, str] = {
    ".Header": "normal",
    ".Header.Filename": "normal",
    ".Signature": "normal",
    ".Signature.Algorithm": "normal",
    ".Signature.Value": "normal",
    ".Data": "normal",
    ".Data.Version": "normal",
    ".Data.SerialNumber": "normal",
    ".Data.Issuer": "normal",
    ".Data.Fingerprint": "normal",
    ".Data.Validity": "normal",
    ".Data.Validity.Before": "normal",
    ".Data.Validity.After": "normal",
    ".Data.Subject": "normal",
    ".Data.Subject.Name": "normal",
    ".Data.Subject.PublicKey": "normal",
    ".Data.Subject.PublicKey.Algorithm": "normal",
    ".Data.Extensions": "normal",
    ".Data.Extension.Critical": "normal",
    ".Data.Extension.Value": "normal",
    ".Data.Extension.AuthorityKeyIdentifier": "normal",
    ".Data.Extension.AuthorityKeyIdentifier.Value": "normal",
    ".Data.Extension.SubjectKeyIdentifier": "normal",
    ".Data.Extension.SubjectKeyIdentifier.Value": "normal",
    ".Data.Extension.KeyUsage": "normal",
    ".Data.Extension.KeyUsage.Value": "normal",
    ".Data.Extension.CertificatePolicies": "normal",
    ".Data.Extension.CertificatePolicies.Value": "normal",
    ".Data.Extension.SubjectAlternativeName": "normal",
    ".Data.Extension.SubjectAlternativeName.Value": "normal",
    ".Data.Extension.IssuerAlternativeName": "normal",
    ".Data.Extension.IssuerAlternativeName.Value": "normal",
    ".Data.Extension.BasicConstraints": "normal",
    ".Data.Extension.BasicConstraints.Value": "normal",
    ".Data.Extension.NameConstraints": "normal",
    ".Data.Extension.NameConstraints.Value": "normal",
    ".Data.Extension.ExtendedKeyUsage": "normal",
    ".Data.Extension.ExtendedKeyUsage.Value": "normal",
    ".Data.Extension.CRLDistributionPoints": "normal",
    ".Data.Extension.CRLDistributionPoints.Value": "normal",
    ".Data.Extension.InhibitAnyPolicy": "normal",
    ".Data.Extension.InhibitAnyPolicy.Value": "normal",
    ".Data.Extension.AuthorityInformationAccess": "normal",
    ".Data.Extension.AuthorityInformationAccess.Value": "normal",
    ".Data.Extension.SubjectInformationAccess": "normal",
    ".Data.Extension.SubjectInformationAccess.Value": "normal",
    ".Data.Extension.CertificateSCTs": "normal",
    ".Data.Extension.CertificateSCTs.Value": "normal",
    ".Data.Extension.PreCertificateSCTs": "normal",
    ".Data.Extension.PreCertificateSCTs.Value": "normal",
    ".P12.Certificate": "normal",
    ".P12.AdditionalCertificates": "normal",
    # ".P12.PrivateKey": "normal",
}


_base_configuration: Configuration = {
    "theme": default_theme,
    "visibility": default_x509_element_visibility,
    "output": {"svg": "", "html": "", "options": {"width": "100"}},
}


config_file = "pkiviewer.toml"


def config_from_file(filename: str) -> Configuration:
    config_file_config = {}
    try:
        with open(filename, "rb") as fp:
            config_file_config = tomli.load(fp)
    except FileNotFoundError:
        pass

    return cast(Configuration, config_file_config)


value_types = (int, float, str)


class MergeError(Exception):
    ...


def merge(base: ConfigSection, file: ConfigSection) -> ConfigSection:
    if len(file) == 0:
        return base

    result = base.copy()
    for key, value in file.items():
        if key in result:
            if isinstance(result[key], value_types):
                if isinstance(value, value_types):
                    result[key] = value
                else:
                    raise MergeError()
            elif isinstance(result[key], list):
                if isinstance(value, value_types):
                    result[key].append(value)
                elif isinstance(value, list):
                    result[key].extend(value)
                elif isinstance(value, dict):
                    raise MergeError()
            elif isinstance(result[key], dict):
                if isinstance(value, value_types):
                    raise MergeError()
                elif isinstance(value, list):
                    raise MergeError()
                elif isinstance(value, dict):
                    result[key] = merge(result[key], cast(ConfigSection, value))
        else:
            result[key] = value

    return result


def config_load(filename: str = config_file) -> Configuration:
    config: Configuration = _base_configuration.copy()
    _file: Configuration = config_from_file(filename)
    if len(_file) > 0:
        for section in config.keys():
            if section in _file:
                config[section] = merge(config[section], _file[section])  # type: ignore

    config["visibility"] = {
        key: VisibilityMapping[value] for key, value in config["visibility"].items()
    }

    _config.set(config)
    return config


def has_key(key_path: str, config: Configuration):
    section = config
    elems = list(reversed(key_path.split(".")))
    try:
        while elem := elems.pop():
            if not isinstance(section, dict) and len(elems) == 0:
                return False
            if not elem in section:
                return False

            section: Any = section[elem]
    except IndexError:
        return True
