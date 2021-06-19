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
    DelayForServerGarbageCollection: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    IntelligentAutoscale: Optional[bool]
    IntelligentScaleinMargin: Optional[float]
    IntelligentScaleoutMargin: Optional[float]
    MaxScaleinAdjustmentStep: Optional[float]
    MaxScaleoutAdjustmentStep: Optional[float]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    ScaleinAlertconfigRefs: Optional[Sequence[str]]
    ScaleinCooldown: Optional[float]
    ScaleoutAlertconfigRefs: Optional[Sequence[str]]
    ScaleoutCooldown: Optional[float]
    TenantRef: Optional[str]
    UsePredictedLoad: Optional[bool]
    Uuid: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            DelayForServerGarbageCollection=json_data.get("DelayForServerGarbageCollection"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IntelligentAutoscale=json_data.get("IntelligentAutoscale"),
            IntelligentScaleinMargin=json_data.get("IntelligentScaleinMargin"),
            IntelligentScaleoutMargin=json_data.get("IntelligentScaleoutMargin"),
            MaxScaleinAdjustmentStep=json_data.get("MaxScaleinAdjustmentStep"),
            MaxScaleoutAdjustmentStep=json_data.get("MaxScaleoutAdjustmentStep"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            ScaleinAlertconfigRefs=json_data.get("ScaleinAlertconfigRefs"),
            ScaleinCooldown=json_data.get("ScaleinCooldown"),
            ScaleoutAlertconfigRefs=json_data.get("ScaleoutAlertconfigRefs"),
            ScaleoutCooldown=json_data.get("ScaleoutCooldown"),
            TenantRef=json_data.get("TenantRef"),
            UsePredictedLoad=json_data.get("UsePredictedLoad"),
            Uuid=json_data.get("Uuid"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


