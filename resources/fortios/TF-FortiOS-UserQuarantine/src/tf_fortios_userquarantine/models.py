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
    FirewallGroups: Optional[str]
    Id: Optional[str]
    Quarantine: Optional[str]
    TrafficPolicy: Optional[str]
    Vdomparam: Optional[str]
    Targets: Optional[Sequence["_TargetsDefinition"]]

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
            FirewallGroups=json_data.get("FirewallGroups"),
            Id=json_data.get("Id"),
            Quarantine=json_data.get("Quarantine"),
            TrafficPolicy=json_data.get("TrafficPolicy"),
            Vdomparam=json_data.get("Vdomparam"),
            Targets=deserialize_list(json_data.get("Targets"), TargetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TargetsDefinition(BaseModel):
    Description: Optional[str]
    Entry: Optional[str]
    Macs: Optional[Sequence["_MacsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Entry=json_data.get("Entry"),
            Macs=deserialize_list(json_data.get("Macs"), MacsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetsDefinition = TargetsDefinition


@dataclass
class MacsDefinition(BaseModel):
    Description: Optional[str]
    Drop: Optional[str]
    EntryId: Optional[float]
    Mac: Optional[str]
    Parent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MacsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Drop=json_data.get("Drop"),
            EntryId=json_data.get("EntryId"),
            Mac=json_data.get("Mac"),
            Parent=json_data.get("Parent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacsDefinition = MacsDefinition


