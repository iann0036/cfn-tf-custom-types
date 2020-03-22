# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    CertRequestPem: Optional[str]
    DnsNames: Optional[Sequence[str]]
    Id: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    KeyAlgorithm: Optional[str]
    PrivateKeyPem: Optional[str]
    Uris: Optional[Sequence[str]]
    Subject: Optional[Sequence["_Subject"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertRequestPem=json_data.get("CertRequestPem"),
            DnsNames=json_data.get("DnsNames"),
            Id=json_data.get("Id"),
            IpAddresses=json_data.get("IpAddresses"),
            KeyAlgorithm=json_data.get("KeyAlgorithm"),
            PrivateKeyPem=json_data.get("PrivateKeyPem"),
            Uris=json_data.get("Uris"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Subject:
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
        cls: Type["_Subject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subject"]:
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
_Subject = Subject


