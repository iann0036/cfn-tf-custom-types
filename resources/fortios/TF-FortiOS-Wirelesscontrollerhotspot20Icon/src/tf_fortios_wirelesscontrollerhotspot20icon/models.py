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
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    IconList: Optional[Sequence["_IconListDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            IconList=deserialize_list(json_data.get("IconList"), IconListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IconListDefinition(BaseModel):
    File: Optional[str]
    Height: Optional[float]
    Lang: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IconListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IconListDefinition"]:
        if not json_data:
            return None
        return cls(
            File=json_data.get("File"),
            Height=json_data.get("Height"),
            Lang=json_data.get("Lang"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IconListDefinition = IconListDefinition


