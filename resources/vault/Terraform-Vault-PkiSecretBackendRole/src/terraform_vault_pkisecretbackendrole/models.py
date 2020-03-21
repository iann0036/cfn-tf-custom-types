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
    AllowAnyName: Optional[bool]
    AllowBareDomains: Optional[bool]
    AllowGlobDomains: Optional[bool]
    AllowIpSans: Optional[bool]
    AllowLocalhost: Optional[bool]
    AllowSubdomains: Optional[bool]
    AllowedDomains: Optional[Sequence[str]]
    AllowedOtherSans: Optional[Sequence[str]]
    AllowedUriSans: Optional[Sequence[str]]
    Backend: Optional[str]
    BasicConstraintsValidForNonCa: Optional[bool]
    ClientFlag: Optional[bool]
    CodeSigningFlag: Optional[bool]
    Country: Optional[Sequence[str]]
    EmailProtectionFlag: Optional[bool]
    EnforceHostnames: Optional[bool]
    ExtKeyUsage: Optional[Sequence[str]]
    GenerateLease: Optional[bool]
    KeyBits: Optional[float]
    KeyType: Optional[str]
    KeyUsage: Optional[Sequence[str]]
    Locality: Optional[Sequence[str]]
    MaxTtl: Optional[str]
    Name: Optional[str]
    NoStore: Optional[bool]
    NotBeforeDuration: Optional[str]
    Organization: Optional[Sequence[str]]
    Ou: Optional[Sequence[str]]
    PolicyIdentifiers: Optional[Sequence[str]]
    PostalCode: Optional[Sequence[str]]
    Province: Optional[Sequence[str]]
    RequireCn: Optional[bool]
    ServerFlag: Optional[bool]
    StreetAddress: Optional[Sequence[str]]
    Ttl: Optional[str]
    UseCsrCommonName: Optional[bool]
    UseCsrSans: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowAnyName=json_data.get("AllowAnyName"),
            AllowBareDomains=json_data.get("AllowBareDomains"),
            AllowGlobDomains=json_data.get("AllowGlobDomains"),
            AllowIpSans=json_data.get("AllowIpSans"),
            AllowLocalhost=json_data.get("AllowLocalhost"),
            AllowSubdomains=json_data.get("AllowSubdomains"),
            AllowedDomains=json_data.get("AllowedDomains"),
            AllowedOtherSans=json_data.get("AllowedOtherSans"),
            AllowedUriSans=json_data.get("AllowedUriSans"),
            Backend=json_data.get("Backend"),
            BasicConstraintsValidForNonCa=json_data.get("BasicConstraintsValidForNonCa"),
            ClientFlag=json_data.get("ClientFlag"),
            CodeSigningFlag=json_data.get("CodeSigningFlag"),
            Country=json_data.get("Country"),
            EmailProtectionFlag=json_data.get("EmailProtectionFlag"),
            EnforceHostnames=json_data.get("EnforceHostnames"),
            ExtKeyUsage=json_data.get("ExtKeyUsage"),
            GenerateLease=json_data.get("GenerateLease"),
            KeyBits=json_data.get("KeyBits"),
            KeyType=json_data.get("KeyType"),
            KeyUsage=json_data.get("KeyUsage"),
            Locality=json_data.get("Locality"),
            MaxTtl=json_data.get("MaxTtl"),
            Name=json_data.get("Name"),
            NoStore=json_data.get("NoStore"),
            NotBeforeDuration=json_data.get("NotBeforeDuration"),
            Organization=json_data.get("Organization"),
            Ou=json_data.get("Ou"),
            PolicyIdentifiers=json_data.get("PolicyIdentifiers"),
            PostalCode=json_data.get("PostalCode"),
            Province=json_data.get("Province"),
            RequireCn=json_data.get("RequireCn"),
            ServerFlag=json_data.get("ServerFlag"),
            StreetAddress=json_data.get("StreetAddress"),
            Ttl=json_data.get("Ttl"),
            UseCsrCommonName=json_data.get("UseCsrCommonName"),
            UseCsrSans=json_data.get("UseCsrSans"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


