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
    AltNames: Optional[Sequence[str]]
    Backend: Optional[str]
    CaChain: Optional[str]
    Certificate: Optional[str]
    CommonName: Optional[str]
    Country: Optional[str]
    Csr: Optional[str]
    ExcludeCnFromSans: Optional[bool]
    Format: Optional[str]
    Id: Optional[str]
    IpSans: Optional[Sequence[str]]
    IssuingCa: Optional[str]
    Locality: Optional[str]
    MaxPathLength: Optional[float]
    Organization: Optional[str]
    OtherSans: Optional[Sequence[str]]
    Ou: Optional[str]
    PermittedDnsDomains: Optional[Sequence[str]]
    PostalCode: Optional[str]
    Province: Optional[str]
    Serial: Optional[str]
    StreetAddress: Optional[str]
    Ttl: Optional[str]
    UriSans: Optional[Sequence[str]]
    UseCsrValues: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AltNames=json_data.get("AltNames"),
            Backend=json_data.get("Backend"),
            CaChain=json_data.get("CaChain"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            Country=json_data.get("Country"),
            Csr=json_data.get("Csr"),
            ExcludeCnFromSans=json_data.get("ExcludeCnFromSans"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            IpSans=json_data.get("IpSans"),
            IssuingCa=json_data.get("IssuingCa"),
            Locality=json_data.get("Locality"),
            MaxPathLength=json_data.get("MaxPathLength"),
            Organization=json_data.get("Organization"),
            OtherSans=json_data.get("OtherSans"),
            Ou=json_data.get("Ou"),
            PermittedDnsDomains=json_data.get("PermittedDnsDomains"),
            PostalCode=json_data.get("PostalCode"),
            Province=json_data.get("Province"),
            Serial=json_data.get("Serial"),
            StreetAddress=json_data.get("StreetAddress"),
            Ttl=json_data.get("Ttl"),
            UriSans=json_data.get("UriSans"),
            UseCsrValues=json_data.get("UseCsrValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


