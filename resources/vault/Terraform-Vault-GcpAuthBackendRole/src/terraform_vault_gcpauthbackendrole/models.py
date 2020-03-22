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
    AddGroupAliases: Optional[bool]
    AllowGceInference: Optional[bool]
    Backend: Optional[str]
    BoundInstanceGroups: Optional[Sequence[str]]
    BoundLabels: Optional[Sequence[str]]
    BoundProjects: Optional[Sequence[str]]
    BoundRegions: Optional[Sequence[str]]
    BoundServiceAccounts: Optional[Sequence[str]]
    BoundZones: Optional[Sequence[str]]
    Id: Optional[str]
    MaxJwtExp: Optional[str]
    MaxTtl: Optional[str]
    Period: Optional[str]
    Policies: Optional[Sequence[str]]
    ProjectId: Optional[str]
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
    Ttl: Optional[str]
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
            AddGroupAliases=json_data.get("AddGroupAliases"),
            AllowGceInference=json_data.get("AllowGceInference"),
            Backend=json_data.get("Backend"),
            BoundInstanceGroups=json_data.get("BoundInstanceGroups"),
            BoundLabels=json_data.get("BoundLabels"),
            BoundProjects=json_data.get("BoundProjects"),
            BoundRegions=json_data.get("BoundRegions"),
            BoundServiceAccounts=json_data.get("BoundServiceAccounts"),
            BoundZones=json_data.get("BoundZones"),
            Id=json_data.get("Id"),
            MaxJwtExp=json_data.get("MaxJwtExp"),
            MaxTtl=json_data.get("MaxTtl"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            ProjectId=json_data.get("ProjectId"),
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
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


