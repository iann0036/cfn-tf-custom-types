# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    CustomOriginServer: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    OwnershipVerification: Optional[Sequence["_OwnershipVerificationDefinition"]]
    OwnershipVerificationHttp: Optional[Sequence["_OwnershipVerificationHttpDefinition"]]
    Status: Optional[str]
    ZoneId: Optional[str]
    Ssl: Optional[Sequence["_SslDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomOriginServer=json_data.get("CustomOriginServer"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            OwnershipVerification=deserialize_list(json_data.get("OwnershipVerification"), OwnershipVerificationDefinition),
            OwnershipVerificationHttp=deserialize_list(json_data.get("OwnershipVerificationHttp"), OwnershipVerificationHttpDefinition),
            Status=json_data.get("Status"),
            ZoneId=json_data.get("ZoneId"),
            Ssl=deserialize_list(json_data.get("Ssl"), SslDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OwnershipVerificationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnershipVerificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnershipVerificationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnershipVerificationDefinition = OwnershipVerificationDefinition


@dataclass
class OwnershipVerificationHttpDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnershipVerificationHttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnershipVerificationHttpDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnershipVerificationHttpDefinition = OwnershipVerificationHttpDefinition


@dataclass
class SslDefinition(BaseModel):
    CertificateAuthority: Optional[str]
    CnameName: Optional[str]
    CnameTarget: Optional[str]
    CustomCertificate: Optional[str]
    CustomKey: Optional[str]
    Method: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    Wildcard: Optional[bool]
    Settings: Optional[Sequence["_SettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthority=json_data.get("CertificateAuthority"),
            CnameName=json_data.get("CnameName"),
            CnameTarget=json_data.get("CnameTarget"),
            CustomCertificate=json_data.get("CustomCertificate"),
            CustomKey=json_data.get("CustomKey"),
            Method=json_data.get("Method"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Wildcard=json_data.get("Wildcard"),
            Settings=deserialize_list(json_data.get("Settings"), SettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslDefinition = SslDefinition


@dataclass
class SettingsDefinition(BaseModel):
    Ciphers: Optional[Sequence[str]]
    Http2: Optional[str]
    MinTlsVersion: Optional[str]
    Tls13: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ciphers=json_data.get("Ciphers"),
            Http2=json_data.get("Http2"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Tls13=json_data.get("Tls13"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingsDefinition = SettingsDefinition


