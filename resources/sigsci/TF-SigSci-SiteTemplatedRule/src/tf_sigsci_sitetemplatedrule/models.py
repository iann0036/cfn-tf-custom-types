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
    Id: Optional[str]
    Name: Optional[str]
    SiteShortName: Optional[str]
    Alerts: Optional[Sequence["_AlertsDefinition"]]
    Detections: Optional[Sequence["_DetectionsDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SiteShortName=json_data.get("SiteShortName"),
            Alerts=deserialize_list(json_data.get("Alerts"), AlertsDefinition),
            Detections=deserialize_list(json_data.get("Detections"), DetectionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlertsDefinition(BaseModel):
    Action: Optional[str]
    BlockDurationSeconds: Optional[float]
    Enabled: Optional[bool]
    Interval: Optional[float]
    LongName: Optional[str]
    SkipNotifications: Optional[bool]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertsDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            BlockDurationSeconds=json_data.get("BlockDurationSeconds"),
            Enabled=json_data.get("Enabled"),
            Interval=json_data.get("Interval"),
            LongName=json_data.get("LongName"),
            SkipNotifications=json_data.get("SkipNotifications"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertsDefinition = AlertsDefinition


@dataclass
class DetectionsDefinition(BaseModel):
    Enabled: Optional[bool]
    Fields: Optional[Sequence["_FieldsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DetectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Fields=deserialize_list(json_data.get("Fields"), FieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetectionsDefinition = DetectionsDefinition


@dataclass
class FieldsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldsDefinition = FieldsDefinition


