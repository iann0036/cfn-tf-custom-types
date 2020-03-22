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
    Id: Optional[str]
    IdentityPoolId: Optional[str]
    Roles: Optional[Sequence["_Roles"]]
    RoleMapping: Optional[Sequence["_RoleMapping"]]
    MappingRule: Optional[Sequence["_MappingRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            IdentityPoolId=json_data.get("IdentityPoolId"),
            Roles=json_data.get("Roles"),
            RoleMapping=json_data.get("RoleMapping"),
            MappingRule=json_data.get("MappingRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Roles:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Roles"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Roles"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Roles = Roles


@dataclass
class RoleMapping:
    AmbiguousRoleResolution: Optional[str]
    IdentityProvider: Optional[str]
    Type: Optional[str]
    MappingRule: Optional[Sequence["_MappingRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoleMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleMapping"]:
        if not json_data:
            return None
        return cls(
            AmbiguousRoleResolution=json_data.get("AmbiguousRoleResolution"),
            IdentityProvider=json_data.get("IdentityProvider"),
            Type=json_data.get("Type"),
            MappingRule=json_data.get("MappingRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleMapping = RoleMapping


@dataclass
class MappingRule:
    Claim: Optional[str]
    MatchType: Optional[str]
    RoleArn: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingRule"]:
        if not json_data:
            return None
        return cls(
            Claim=json_data.get("Claim"),
            MatchType=json_data.get("MatchType"),
            RoleArn=json_data.get("RoleArn"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingRule = MappingRule


