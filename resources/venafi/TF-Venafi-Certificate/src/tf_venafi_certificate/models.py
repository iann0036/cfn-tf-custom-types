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
    Algorithm: Optional[str]
    Certificate: Optional[str]
    CertificateDn: Optional[str]
    Chain: Optional[str]
    CommonName: Optional[str]
    CsrPem: Optional[str]
    CustomFields: Optional[Sequence["_CustomFieldsDefinition"]]
    EcdsaCurve: Optional[str]
    ExpirationWindow: Optional[float]
    Id: Optional[str]
    IssuerHint: Optional[str]
    KeyPassword: Optional[str]
    Pkcs12: Optional[str]
    PrivateKeyPem: Optional[str]
    RsaBits: Optional[float]
    SanDns: Optional[Sequence[str]]
    SanEmail: Optional[Sequence[str]]
    SanIp: Optional[Sequence[str]]
    ValidDays: Optional[float]

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
            Algorithm=json_data.get("Algorithm"),
            Certificate=json_data.get("Certificate"),
            CertificateDn=json_data.get("CertificateDn"),
            Chain=json_data.get("Chain"),
            CommonName=json_data.get("CommonName"),
            CsrPem=json_data.get("CsrPem"),
            CustomFields=deserialize_list(json_data.get("CustomFields"), CustomFieldsDefinition),
            EcdsaCurve=json_data.get("EcdsaCurve"),
            ExpirationWindow=json_data.get("ExpirationWindow"),
            Id=json_data.get("Id"),
            IssuerHint=json_data.get("IssuerHint"),
            KeyPassword=json_data.get("KeyPassword"),
            Pkcs12=json_data.get("Pkcs12"),
            PrivateKeyPem=json_data.get("PrivateKeyPem"),
            RsaBits=json_data.get("RsaBits"),
            SanDns=json_data.get("SanDns"),
            SanEmail=json_data.get("SanEmail"),
            SanIp=json_data.get("SanIp"),
            ValidDays=json_data.get("ValidDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomFieldsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomFieldsDefinition = CustomFieldsDefinition


