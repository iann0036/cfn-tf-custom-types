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
    EventType: Optional[str]
    FazEventName: Optional[str]
    FazEventSeverity: Optional[str]
    FazEventTags: Optional[str]
    Id: Optional[str]
    IocLevel: Optional[str]
    LicenseType: Optional[str]
    Logid: Optional[float]
    Name: Optional[str]
    ReportType: Optional[str]
    TriggerDay: Optional[float]
    TriggerFrequency: Optional[str]
    TriggerHour: Optional[float]
    TriggerMinute: Optional[float]
    TriggerType: Optional[str]
    TriggerWeekday: Optional[str]
    Vdomparam: Optional[str]
    Fields: Optional[Sequence["_FieldsDefinition"]]

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
            EventType=json_data.get("EventType"),
            FazEventName=json_data.get("FazEventName"),
            FazEventSeverity=json_data.get("FazEventSeverity"),
            FazEventTags=json_data.get("FazEventTags"),
            Id=json_data.get("Id"),
            IocLevel=json_data.get("IocLevel"),
            LicenseType=json_data.get("LicenseType"),
            Logid=json_data.get("Logid"),
            Name=json_data.get("Name"),
            ReportType=json_data.get("ReportType"),
            TriggerDay=json_data.get("TriggerDay"),
            TriggerFrequency=json_data.get("TriggerFrequency"),
            TriggerHour=json_data.get("TriggerHour"),
            TriggerMinute=json_data.get("TriggerMinute"),
            TriggerType=json_data.get("TriggerType"),
            TriggerWeekday=json_data.get("TriggerWeekday"),
            Vdomparam=json_data.get("Vdomparam"),
            Fields=deserialize_list(json_data.get("Fields"), FieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldsDefinition(BaseModel):
    Id: Optional[float]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldsDefinition = FieldsDefinition


