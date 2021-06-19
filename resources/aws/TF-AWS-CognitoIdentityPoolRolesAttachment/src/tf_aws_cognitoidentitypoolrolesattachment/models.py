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
    Id: Optional[str]
    IdentityPoolId: Optional[str]
    Roles: Optional[Sequence["_RolesDefinition"]]
    RoleMapping: Optional[Sequence["_RoleMappingDefinition"]]

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
            Id=json_data.get("Id"),
            IdentityPoolId=json_data.get("IdentityPoolId"),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
            RoleMapping=deserialize_list(json_data.get("RoleMapping"), RoleMappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RolesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolesDefinition = RolesDefinition


@dataclass
class RoleMappingDefinition(BaseModel):
    AmbiguousRoleResolution: Optional[str]
    IdentityProvider: Optional[str]
    Type: Optional[str]
    MappingRule: Optional[Sequence["_MappingRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoleMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            AmbiguousRoleResolution=json_data.get("AmbiguousRoleResolution"),
            IdentityProvider=json_data.get("IdentityProvider"),
            Type=json_data.get("Type"),
            MappingRule=deserialize_list(json_data.get("MappingRule"), MappingRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleMappingDefinition = RoleMappingDefinition


@dataclass
class MappingRuleDefinition(BaseModel):
    Claim: Optional[str]
    MatchType: Optional[str]
    RoleArn: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappingRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Claim=json_data.get("Claim"),
            MatchType=json_data.get("MatchType"),
            RoleArn=json_data.get("RoleArn"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingRuleDefinition = MappingRuleDefinition


