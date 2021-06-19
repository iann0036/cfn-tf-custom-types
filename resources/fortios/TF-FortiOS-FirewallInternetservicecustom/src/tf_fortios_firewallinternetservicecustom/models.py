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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Reputation: Optional[float]
    Vdomparam: Optional[str]
    Entry: Optional[Sequence["_EntryDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Reputation=json_data.get("Reputation"),
            Vdomparam=json_data.get("Vdomparam"),
            Entry=deserialize_list(json_data.get("Entry"), EntryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntryDefinition(BaseModel):
    Id: Optional[float]
    Protocol: Optional[float]
    Dst: Optional[Sequence["_DstDefinition"]]
    PortRange: Optional[Sequence["_PortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Protocol=json_data.get("Protocol"),
            Dst=deserialize_list(json_data.get("Dst"), DstDefinition),
            PortRange=deserialize_list(json_data.get("PortRange"), PortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntryDefinition = EntryDefinition


@dataclass
class DstDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstDefinition = DstDefinition


@dataclass
class PortRangeDefinition(BaseModel):
    EndPort: Optional[float]
    Id: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            Id=json_data.get("Id"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRangeDefinition = PortRangeDefinition


