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
    AllowedRedirectUris: Optional[Sequence[str]]
    Backend: Optional[str]
    BoundAudiences: Optional[Sequence[str]]
    BoundCidrs: Optional[Sequence[str]]
    BoundClaims: Optional[Sequence["_BoundClaimsDefinition"]]
    BoundClaimsType: Optional[str]
    BoundSubject: Optional[str]
    ClaimMappings: Optional[Sequence["_ClaimMappingsDefinition"]]
    ClockSkewLeeway: Optional[float]
    ExpirationLeeway: Optional[float]
    GroupsClaim: Optional[str]
    GroupsClaimDelimiterPattern: Optional[str]
    Id: Optional[str]
    MaxTtl: Optional[float]
    NotBeforeLeeway: Optional[float]
    NumUses: Optional[float]
    OidcScopes: Optional[Sequence[str]]
    Period: Optional[float]
    Policies: Optional[Sequence[str]]
    RoleName: Optional[str]
    RoleType: Optional[str]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]
    Ttl: Optional[float]
    UserClaim: Optional[str]
    VerboseOidcLogging: Optional[bool]

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
            AllowedRedirectUris=json_data.get("AllowedRedirectUris"),
            Backend=json_data.get("Backend"),
            BoundAudiences=json_data.get("BoundAudiences"),
            BoundCidrs=json_data.get("BoundCidrs"),
            BoundClaims=deserialize_list(json_data.get("BoundClaims"), BoundClaimsDefinition),
            BoundClaimsType=json_data.get("BoundClaimsType"),
            BoundSubject=json_data.get("BoundSubject"),
            ClaimMappings=deserialize_list(json_data.get("ClaimMappings"), ClaimMappingsDefinition),
            ClockSkewLeeway=json_data.get("ClockSkewLeeway"),
            ExpirationLeeway=json_data.get("ExpirationLeeway"),
            GroupsClaim=json_data.get("GroupsClaim"),
            GroupsClaimDelimiterPattern=json_data.get("GroupsClaimDelimiterPattern"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            NotBeforeLeeway=json_data.get("NotBeforeLeeway"),
            NumUses=json_data.get("NumUses"),
            OidcScopes=json_data.get("OidcScopes"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            RoleName=json_data.get("RoleName"),
            RoleType=json_data.get("RoleType"),
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
            UserClaim=json_data.get("UserClaim"),
            VerboseOidcLogging=json_data.get("VerboseOidcLogging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BoundClaimsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BoundClaimsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoundClaimsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoundClaimsDefinition = BoundClaimsDefinition


@dataclass
class ClaimMappingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClaimMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClaimMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClaimMappingsDefinition = ClaimMappingsDefinition


