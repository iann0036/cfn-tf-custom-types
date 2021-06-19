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
    CertRequestPem: Optional[str]
    DnsNames: Optional[Sequence[str]]
    Id: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    KeyAlgorithm: Optional[str]
    PrivateKeyPem: Optional[str]
    Uris: Optional[Sequence[str]]
    Subject: Optional[Sequence["_SubjectDefinition"]]

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
            CertRequestPem=json_data.get("CertRequestPem"),
            DnsNames=json_data.get("DnsNames"),
            Id=json_data.get("Id"),
            IpAddresses=json_data.get("IpAddresses"),
            KeyAlgorithm=json_data.get("KeyAlgorithm"),
            PrivateKeyPem=json_data.get("PrivateKeyPem"),
            Uris=json_data.get("Uris"),
            Subject=deserialize_list(json_data.get("Subject"), SubjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SubjectDefinition(BaseModel):
    CommonName: Optional[str]
    Country: Optional[str]
    Locality: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    PostalCode: Optional[str]
    Province: Optional[str]
    SerialNumber: Optional[str]
    StreetAddress: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            Locality=json_data.get("Locality"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            PostalCode=json_data.get("PostalCode"),
            Province=json_data.get("Province"),
            SerialNumber=json_data.get("SerialNumber"),
            StreetAddress=json_data.get("StreetAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectDefinition = SubjectDefinition


