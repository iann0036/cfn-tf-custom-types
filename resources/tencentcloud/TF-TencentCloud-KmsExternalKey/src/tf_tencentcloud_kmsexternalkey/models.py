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
    Alias: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsArchived: Optional[bool]
    IsEnabled: Optional[bool]
    KeyMaterialBase64: Optional[str]
    KeyState: Optional[str]
    PendingDeleteWindowInDays: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ValidTo: Optional[float]
    WrappingAlgorithm: Optional[str]

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
            Alias=json_data.get("Alias"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsArchived=json_data.get("IsArchived"),
            IsEnabled=json_data.get("IsEnabled"),
            KeyMaterialBase64=json_data.get("KeyMaterialBase64"),
            KeyState=json_data.get("KeyState"),
            PendingDeleteWindowInDays=json_data.get("PendingDeleteWindowInDays"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ValidTo=json_data.get("ValidTo"),
            WrappingAlgorithm=json_data.get("WrappingAlgorithm"),
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


