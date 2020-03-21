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
    Accessor: Optional[str]
    BoundIssuer: Optional[str]
    DefaultRole: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    JwksCaPem: Optional[str]
    JwksUrl: Optional[str]
    JwtSupportedAlgs: Optional[Sequence[str]]
    JwtValidationPubkeys: Optional[Sequence[str]]
    OidcClientId: Optional[str]
    OidcClientSecret: Optional[str]
    OidcDiscoveryCaPem: Optional[str]
    OidcDiscoveryUrl: Optional[str]
    Path: Optional[str]
    Tune: Optional[Sequence["_Tune"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accessor=json_data.get("Accessor"),
            BoundIssuer=json_data.get("BoundIssuer"),
            DefaultRole=json_data.get("DefaultRole"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            JwksCaPem=json_data.get("JwksCaPem"),
            JwksUrl=json_data.get("JwksUrl"),
            JwtSupportedAlgs=json_data.get("JwtSupportedAlgs"),
            JwtValidationPubkeys=json_data.get("JwtValidationPubkeys"),
            OidcClientId=json_data.get("OidcClientId"),
            OidcClientSecret=json_data.get("OidcClientSecret"),
            OidcDiscoveryCaPem=json_data.get("OidcDiscoveryCaPem"),
            OidcDiscoveryUrl=json_data.get("OidcDiscoveryUrl"),
            Path=json_data.get("Path"),
            Tune=json_data.get("Tune"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tune:
    AllowedResponseHeaders: Optional[Sequence[str]]
    AuditNonHmacRequestKeys: Optional[Sequence[str]]
    AuditNonHmacResponseKeys: Optional[Sequence[str]]
    DefaultLeaseTtl: Optional[str]
    ListingVisibility: Optional[str]
    MaxLeaseTtl: Optional[str]
    PassthroughRequestHeaders: Optional[Sequence[str]]
    TokenType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tune"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tune"]:
        if not json_data:
            return None
        return cls(
            AllowedResponseHeaders=json_data.get("AllowedResponseHeaders"),
            AuditNonHmacRequestKeys=json_data.get("AuditNonHmacRequestKeys"),
            AuditNonHmacResponseKeys=json_data.get("AuditNonHmacResponseKeys"),
            DefaultLeaseTtl=json_data.get("DefaultLeaseTtl"),
            ListingVisibility=json_data.get("ListingVisibility"),
            MaxLeaseTtl=json_data.get("MaxLeaseTtl"),
            PassthroughRequestHeaders=json_data.get("PassthroughRequestHeaders"),
            TokenType=json_data.get("TokenType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tune = Tune


