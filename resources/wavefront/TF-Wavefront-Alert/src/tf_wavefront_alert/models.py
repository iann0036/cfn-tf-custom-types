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
    AdditionalInformation: Optional[str]
    AlertType: Optional[str]
    CanModify: Optional[Sequence[str]]
    CanView: Optional[Sequence[str]]
    Condition: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    DisplayExpression: Optional[str]
    Id: Optional[str]
    Minutes: Optional[float]
    Name: Optional[str]
    NotificationResendFrequencyMinutes: Optional[float]
    ResolveAfterMinutes: Optional[float]
    Severity: Optional[str]
    Tags: Optional[Sequence[str]]
    Target: Optional[str]
    ThresholdTargets: Optional[Sequence["_ThresholdTargetsDefinition"]]

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
            AdditionalInformation=json_data.get("AdditionalInformation"),
            AlertType=json_data.get("AlertType"),
            CanModify=json_data.get("CanModify"),
            CanView=json_data.get("CanView"),
            Condition=json_data.get("Condition"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            DisplayExpression=json_data.get("DisplayExpression"),
            Id=json_data.get("Id"),
            Minutes=json_data.get("Minutes"),
            Name=json_data.get("Name"),
            NotificationResendFrequencyMinutes=json_data.get("NotificationResendFrequencyMinutes"),
            ResolveAfterMinutes=json_data.get("ResolveAfterMinutes"),
            Severity=json_data.get("Severity"),
            Tags=json_data.get("Tags"),
            Target=json_data.get("Target"),
            ThresholdTargets=deserialize_list(json_data.get("ThresholdTargets"), ThresholdTargetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConditionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class ThresholdTargetsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdTargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdTargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdTargetsDefinition = ThresholdTargetsDefinition


