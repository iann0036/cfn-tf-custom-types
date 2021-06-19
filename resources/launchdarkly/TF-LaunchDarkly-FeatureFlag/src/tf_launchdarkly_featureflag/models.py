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
    DefaultOffVariation: Optional[str]
    DefaultOnVariation: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IncludeInSnippet: Optional[bool]
    Key: Optional[str]
    MaintainerId: Optional[str]
    Name: Optional[str]
    ProjectKey: Optional[str]
    Tags: Optional[Sequence[str]]
    Temporary: Optional[bool]
    VariationType: Optional[str]
    CustomProperties: Optional[Sequence["_CustomPropertiesDefinition"]]
    Variations: Optional[Sequence["_VariationsDefinition"]]

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
            DefaultOffVariation=json_data.get("DefaultOffVariation"),
            DefaultOnVariation=json_data.get("DefaultOnVariation"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IncludeInSnippet=json_data.get("IncludeInSnippet"),
            Key=json_data.get("Key"),
            MaintainerId=json_data.get("MaintainerId"),
            Name=json_data.get("Name"),
            ProjectKey=json_data.get("ProjectKey"),
            Tags=json_data.get("Tags"),
            Temporary=json_data.get("Temporary"),
            VariationType=json_data.get("VariationType"),
            CustomProperties=deserialize_list(json_data.get("CustomProperties"), CustomPropertiesDefinition),
            Variations=deserialize_list(json_data.get("Variations"), VariationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomPropertiesDefinition(BaseModel):
    Key: Optional[str]
    Name: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPropertiesDefinition = CustomPropertiesDefinition


@dataclass
class VariationsDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariationsDefinition = VariationsDefinition


