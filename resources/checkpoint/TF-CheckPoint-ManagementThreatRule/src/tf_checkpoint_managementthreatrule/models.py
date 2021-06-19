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
    Action: Optional[str]
    Comments: Optional[str]
    Destination: Optional[Sequence[str]]
    DestinationNegate: Optional[bool]
    Enabled: Optional[bool]
    Exceptions: Optional[Sequence[str]]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    InstallOn: Optional[Sequence[str]]
    Layer: Optional[str]
    Name: Optional[str]
    Position: Optional[Sequence["_PositionDefinition"]]
    ProtectedScope: Optional[Sequence[str]]
    ProtectedScopeNegate: Optional[bool]
    Service: Optional[Sequence[str]]
    ServiceNegate: Optional[bool]
    Source: Optional[Sequence[str]]
    SourceNegate: Optional[bool]
    Track: Optional[str]
    TrackSettings: Optional[Sequence["_TrackSettingsDefinition"]]

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
            Action=json_data.get("Action"),
            Comments=json_data.get("Comments"),
            Destination=json_data.get("Destination"),
            DestinationNegate=json_data.get("DestinationNegate"),
            Enabled=json_data.get("Enabled"),
            Exceptions=json_data.get("Exceptions"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            InstallOn=json_data.get("InstallOn"),
            Layer=json_data.get("Layer"),
            Name=json_data.get("Name"),
            Position=deserialize_list(json_data.get("Position"), PositionDefinition),
            ProtectedScope=json_data.get("ProtectedScope"),
            ProtectedScopeNegate=json_data.get("ProtectedScopeNegate"),
            Service=json_data.get("Service"),
            ServiceNegate=json_data.get("ServiceNegate"),
            Source=json_data.get("Source"),
            SourceNegate=json_data.get("SourceNegate"),
            Track=json_data.get("Track"),
            TrackSettings=deserialize_list(json_data.get("TrackSettings"), TrackSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PositionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PositionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PositionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PositionDefinition = PositionDefinition


@dataclass
class TrackSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrackSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackSettingsDefinition = TrackSettingsDefinition


