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
    ActionSettings: Optional[Sequence["_ActionSettingsDefinition"]]
    Comments: Optional[str]
    Content: Optional[Sequence[str]]
    ContentDirection: Optional[str]
    ContentNegate: Optional[bool]
    CustomFields: Optional[Sequence["_CustomFieldsDefinition"]]
    Destination: Optional[Sequence[str]]
    DestinationNegate: Optional[bool]
    Enabled: Optional[bool]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    InlineLayer: Optional[str]
    InstallOn: Optional[Sequence[str]]
    Layer: Optional[str]
    Name: Optional[str]
    Position: Optional[Sequence["_PositionDefinition"]]
    Service: Optional[Sequence[str]]
    ServiceNegate: Optional[bool]
    Source: Optional[Sequence[str]]
    SourceNegate: Optional[bool]
    Time: Optional[Sequence[str]]
    Track: Optional[Sequence["_TrackDefinition"]]
    Vpn: Optional[str]
    UserCheck: Optional[Sequence["_UserCheckDefinition"]]

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
            ActionSettings=deserialize_list(json_data.get("ActionSettings"), ActionSettingsDefinition),
            Comments=json_data.get("Comments"),
            Content=json_data.get("Content"),
            ContentDirection=json_data.get("ContentDirection"),
            ContentNegate=json_data.get("ContentNegate"),
            CustomFields=deserialize_list(json_data.get("CustomFields"), CustomFieldsDefinition),
            Destination=json_data.get("Destination"),
            DestinationNegate=json_data.get("DestinationNegate"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            InlineLayer=json_data.get("InlineLayer"),
            InstallOn=json_data.get("InstallOn"),
            Layer=json_data.get("Layer"),
            Name=json_data.get("Name"),
            Position=deserialize_list(json_data.get("Position"), PositionDefinition),
            Service=json_data.get("Service"),
            ServiceNegate=json_data.get("ServiceNegate"),
            Source=json_data.get("Source"),
            SourceNegate=json_data.get("SourceNegate"),
            Time=json_data.get("Time"),
            Track=deserialize_list(json_data.get("Track"), TrackDefinition),
            Vpn=json_data.get("Vpn"),
            UserCheck=deserialize_list(json_data.get("UserCheck"), UserCheckDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionSettingsDefinition = ActionSettingsDefinition


@dataclass
class CustomFieldsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomFieldsDefinition = CustomFieldsDefinition


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
class TrackDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackDefinition = TrackDefinition


@dataclass
class UserCheckDefinition(BaseModel):
    Confirm: Optional[str]
    Frequency: Optional[str]
    Interaction: Optional[str]
    CustomFrequency: Optional[Sequence["_CustomFrequencyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UserCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Confirm=json_data.get("Confirm"),
            Frequency=json_data.get("Frequency"),
            Interaction=json_data.get("Interaction"),
            CustomFrequency=deserialize_list(json_data.get("CustomFrequency"), CustomFrequencyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserCheckDefinition = UserCheckDefinition


@dataclass
class CustomFrequencyDefinition(BaseModel):
    Every: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomFrequencyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomFrequencyDefinition"]:
        if not json_data:
            return None
        return cls(
            Every=json_data.get("Every"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomFrequencyDefinition = CustomFrequencyDefinition


