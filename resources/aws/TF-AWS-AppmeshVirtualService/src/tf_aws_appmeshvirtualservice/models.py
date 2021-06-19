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
    Arn: Optional[str]
    CreatedDate: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    Name: Optional[str]
    ResourceOwner: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            Arn=json_data.get("Arn"),
            CreatedDate=json_data.get("CreatedDate"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            MeshOwner=json_data.get("MeshOwner"),
            Name=json_data.get("Name"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SpecDefinition(BaseModel):
    Provider: Optional[Sequence["_ProviderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            Provider=deserialize_list(json_data.get("Provider"), ProviderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class ProviderDefinition(BaseModel):
    VirtualNode: Optional[Sequence["_VirtualNodeDefinition"]]
    VirtualRouter: Optional[Sequence["_VirtualRouterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            VirtualNode=deserialize_list(json_data.get("VirtualNode"), VirtualNodeDefinition),
            VirtualRouter=deserialize_list(json_data.get("VirtualRouter"), VirtualRouterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderDefinition = ProviderDefinition


@dataclass
class VirtualNodeDefinition(BaseModel):
    VirtualNodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeDefinition"]:
        if not json_data:
            return None
        return cls(
            VirtualNodeName=json_data.get("VirtualNodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeDefinition = VirtualNodeDefinition


@dataclass
class VirtualRouterDefinition(BaseModel):
    VirtualRouterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualRouterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualRouterDefinition"]:
        if not json_data:
            return None
        return cls(
            VirtualRouterName=json_data.get("VirtualRouterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualRouterDefinition = VirtualRouterDefinition


