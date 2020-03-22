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
    BaseUrl: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    MaxTtl: Optional[str]
    Organization: Optional[str]
    Path: Optional[str]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]
    Ttl: Optional[str]
    Tune: Optional[Sequence["_Tune"]]

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
            BaseUrl=json_data.get("BaseUrl"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            Organization=json_data.get("Organization"),
            Path=json_data.get("Path"),
            TokenBoundCidrs=json_data.get("TokenBoundCidrs"),
            TokenExplicitMaxTtl=json_data.get("TokenExplicitMaxTtl"),
            TokenMaxTtl=json_data.get("TokenMaxTtl"),
            TokenNoDefaultPolicy=json_data.get("TokenNoDefaultPolicy"),
            TokenNumUses=json_data.get("TokenNumUses"),
            TokenPeriod=json_data.get("TokenPeriod"),
            TokenPolicies=json_data.get("TokenPolicies"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenType=json_data.get("TokenType"),
            Ttl=json_data.get("Ttl"),
            Tune=json_data.get("Tune"),
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


