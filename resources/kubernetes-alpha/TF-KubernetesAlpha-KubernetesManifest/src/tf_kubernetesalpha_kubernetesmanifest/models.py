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
    Manifest: Optional[str]
    Object: Optional[str]
    WaitFor: Optional["_WaitForDefinition2"]

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
            Manifest=json_data.get("Manifest"),
            Object=json_data.get("Object"),
            WaitFor=WaitForDefinition2._deserialize(json_data.get("WaitFor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class WaitForDefinition2(BaseModel):
    Fields: Optional[Sequence["_WaitForDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WaitForDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaitForDefinition2"]:
        if not json_data:
            return None
        return cls(
            Fields=deserialize_list(json_data.get("Fields"), WaitForDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaitForDefinition2 = WaitForDefinition2


@dataclass
class WaitForDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WaitForDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaitForDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaitForDefinition = WaitForDefinition


