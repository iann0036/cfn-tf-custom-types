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
    ApiVersion: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    State: Optional[str]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    ContextFilterList: Optional[Sequence["_ContextFilterListDefinition"]]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    RoleReference: Optional[Sequence["_RoleReferenceDefinition"]]
    UserGroupReferenceList: Optional[Sequence["_UserGroupReferenceListDefinition"]]
    UserReferenceList: Optional[Sequence["_UserReferenceListDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            ContextFilterList=deserialize_list(json_data.get("ContextFilterList"), ContextFilterListDefinition),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            RoleReference=deserialize_list(json_data.get("RoleReference"), RoleReferenceDefinition),
            UserGroupReferenceList=deserialize_list(json_data.get("UserGroupReferenceList"), UserGroupReferenceListDefinition),
            UserReferenceList=deserialize_list(json_data.get("UserReferenceList"), UserReferenceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


@dataclass
class ContextFilterListDefinition(BaseModel):
    EntityFilterExpressionList: Optional[Sequence["_EntityFilterExpressionListDefinition"]]
    ScopeFilterExpressionList: Optional[Sequence["_ScopeFilterExpressionListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContextFilterListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContextFilterListDefinition"]:
        if not json_data:
            return None
        return cls(
            EntityFilterExpressionList=deserialize_list(json_data.get("EntityFilterExpressionList"), EntityFilterExpressionListDefinition),
            ScopeFilterExpressionList=deserialize_list(json_data.get("ScopeFilterExpressionList"), ScopeFilterExpressionListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContextFilterListDefinition = ContextFilterListDefinition


@dataclass
class EntityFilterExpressionListDefinition(BaseModel):
    LeftHandSideEntityType: Optional[str]
    Operator: Optional[str]
    RightHandSide: Optional[Sequence["_RightHandSideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntityFilterExpressionListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityFilterExpressionListDefinition"]:
        if not json_data:
            return None
        return cls(
            LeftHandSideEntityType=json_data.get("LeftHandSideEntityType"),
            Operator=json_data.get("Operator"),
            RightHandSide=deserialize_list(json_data.get("RightHandSide"), RightHandSideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityFilterExpressionListDefinition = EntityFilterExpressionListDefinition


@dataclass
class RightHandSideDefinition(BaseModel):
    Collection: Optional[str]
    UuidList: Optional[Sequence[str]]
    Categories: Optional[Sequence["_CategoriesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RightHandSideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RightHandSideDefinition"]:
        if not json_data:
            return None
        return cls(
            Collection=json_data.get("Collection"),
            UuidList=json_data.get("UuidList"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RightHandSideDefinition = RightHandSideDefinition


@dataclass
class ScopeFilterExpressionListDefinition(BaseModel):
    LeftHandSide: Optional[str]
    Operator: Optional[str]
    RightHandSide: Optional[Sequence["_RightHandSideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeFilterExpressionListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeFilterExpressionListDefinition"]:
        if not json_data:
            return None
        return cls(
            LeftHandSide=json_data.get("LeftHandSide"),
            Operator=json_data.get("Operator"),
            RightHandSide=deserialize_list(json_data.get("RightHandSide"), RightHandSideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeFilterExpressionListDefinition = ScopeFilterExpressionListDefinition


@dataclass
class OwnerReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class RoleReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoleReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleReferenceDefinition = RoleReferenceDefinition


@dataclass
class UserGroupReferenceListDefinition(BaseModel):
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserGroupReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserGroupReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserGroupReferenceListDefinition = UserGroupReferenceListDefinition


@dataclass
class UserReferenceListDefinition(BaseModel):
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserReferenceListDefinition = UserReferenceListDefinition


