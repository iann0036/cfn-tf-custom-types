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
    ContextDashboardId: Optional[str]
    Id: Optional[str]
    PropertyName: Optional[str]
    PropertyValue: Optional[str]
    TargetExternalUrl: Optional[Sequence["_TargetExternalUrlDefinition"]]
    TargetSignalfxDashboard: Optional[Sequence["_TargetSignalfxDashboardDefinition"]]
    TargetSplunk: Optional[Sequence["_TargetSplunkDefinition"]]

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
            ContextDashboardId=json_data.get("ContextDashboardId"),
            Id=json_data.get("Id"),
            PropertyName=json_data.get("PropertyName"),
            PropertyValue=json_data.get("PropertyValue"),
            TargetExternalUrl=deserialize_list(json_data.get("TargetExternalUrl"), TargetExternalUrlDefinition),
            TargetSignalfxDashboard=deserialize_list(json_data.get("TargetSignalfxDashboard"), TargetSignalfxDashboardDefinition),
            TargetSplunk=deserialize_list(json_data.get("TargetSplunk"), TargetSplunkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TargetExternalUrlDefinition(BaseModel):
    MinimumTimeWindow: Optional[str]
    Name: Optional[str]
    PropertyKeyMapping: Optional[Sequence["_PropertyKeyMappingDefinition"]]
    TimeFormat: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetExternalUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetExternalUrlDefinition"]:
        if not json_data:
            return None
        return cls(
            MinimumTimeWindow=json_data.get("MinimumTimeWindow"),
            Name=json_data.get("Name"),
            PropertyKeyMapping=deserialize_list(json_data.get("PropertyKeyMapping"), PropertyKeyMappingDefinition),
            TimeFormat=json_data.get("TimeFormat"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetExternalUrlDefinition = TargetExternalUrlDefinition


@dataclass
class PropertyKeyMappingDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyKeyMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyKeyMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyKeyMappingDefinition = PropertyKeyMappingDefinition


@dataclass
class TargetSignalfxDashboardDefinition(BaseModel):
    DashboardGroupId: Optional[str]
    DashboardId: Optional[str]
    IsDefault: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetSignalfxDashboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetSignalfxDashboardDefinition"]:
        if not json_data:
            return None
        return cls(
            DashboardGroupId=json_data.get("DashboardGroupId"),
            DashboardId=json_data.get("DashboardId"),
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetSignalfxDashboardDefinition = TargetSignalfxDashboardDefinition


@dataclass
class TargetSplunkDefinition(BaseModel):
    Name: Optional[str]
    PropertyKeyMapping: Optional[Sequence["_PropertyKeyMappingDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetSplunkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetSplunkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PropertyKeyMapping=deserialize_list(json_data.get("PropertyKeyMapping"), PropertyKeyMappingDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetSplunkDefinition = TargetSplunkDefinition


@dataclass
class PropertyKeyMappingDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyKeyMappingDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyKeyMappingDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyKeyMappingDefinition2 = PropertyKeyMappingDefinition2


