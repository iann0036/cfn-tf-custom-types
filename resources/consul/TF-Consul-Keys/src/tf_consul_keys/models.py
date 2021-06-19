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
    Datacenter: Optional[str]
    Id: Optional[str]
    Namespace: Optional[str]
    Token: Optional[str]
    Var: Optional[Sequence["_VarDefinition"]]
    Key: Optional[Sequence["_KeyDefinition"]]

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
            Datacenter=json_data.get("Datacenter"),
            Id=json_data.get("Id"),
            Namespace=json_data.get("Namespace"),
            Token=json_data.get("Token"),
            Var=deserialize_list(json_data.get("Var"), VarDefinition),
            Key=deserialize_list(json_data.get("Key"), KeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VarDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VarDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VarDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VarDefinition = VarDefinition


@dataclass
class KeyDefinition(BaseModel):
    Default: Optional[str]
    Delete: Optional[bool]
    Flags: Optional[float]
    Name: Optional[str]
    Path: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Flags=json_data.get("Flags"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDefinition = KeyDefinition


