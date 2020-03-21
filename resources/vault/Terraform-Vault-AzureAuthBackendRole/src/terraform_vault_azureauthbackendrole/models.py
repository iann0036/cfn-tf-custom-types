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
    Backend: Optional[str]
    BoundGroupIds: Optional[Sequence[str]]
    BoundLocations: Optional[Sequence[str]]
    BoundResourceGroups: Optional[Sequence[str]]
    BoundScaleSets: Optional[Sequence[str]]
    BoundServicePrincipalIds: Optional[Sequence[str]]
    BoundSubscriptionIds: Optional[Sequence[str]]
    MaxTtl: Optional[float]
    Period: Optional[float]
    Policies: Optional[Sequence[str]]
    Role: Optional[str]
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

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            BoundGroupIds=json_data.get("BoundGroupIds"),
            BoundLocations=json_data.get("BoundLocations"),
            BoundResourceGroups=json_data.get("BoundResourceGroups"),
            BoundScaleSets=json_data.get("BoundScaleSets"),
            BoundServicePrincipalIds=json_data.get("BoundServicePrincipalIds"),
            BoundSubscriptionIds=json_data.get("BoundSubscriptionIds"),
            MaxTtl=json_data.get("MaxTtl"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            Role=json_data.get("Role"),
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
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


