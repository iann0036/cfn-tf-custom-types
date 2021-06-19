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
    Description: Optional[str]
    Disabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Notifications: Optional[Sequence[str]]
    Secret: Optional[str]
    DpmLimits: Optional[Sequence["_DpmLimitsDefinition"]]
    HostOrUsageLimits: Optional[Sequence["_HostOrUsageLimitsDefinition"]]

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
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Notifications=json_data.get("Notifications"),
            Secret=json_data.get("Secret"),
            DpmLimits=deserialize_list(json_data.get("DpmLimits"), DpmLimitsDefinition),
            HostOrUsageLimits=deserialize_list(json_data.get("HostOrUsageLimits"), HostOrUsageLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DpmLimitsDefinition(BaseModel):
    DpmLimit: Optional[float]
    DpmNotificationThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DpmLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DpmLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            DpmLimit=json_data.get("DpmLimit"),
            DpmNotificationThreshold=json_data.get("DpmNotificationThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DpmLimitsDefinition = DpmLimitsDefinition


@dataclass
class HostOrUsageLimitsDefinition(BaseModel):
    ContainerLimit: Optional[float]
    ContainerNotificationThreshold: Optional[float]
    CustomMetricsLimit: Optional[float]
    CustomMetricsNotificationThreshold: Optional[float]
    HighResMetricsLimit: Optional[float]
    HighResMetricsNotificationThreshold: Optional[float]
    HostLimit: Optional[float]
    HostNotificationThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostOrUsageLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostOrUsageLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerLimit=json_data.get("ContainerLimit"),
            ContainerNotificationThreshold=json_data.get("ContainerNotificationThreshold"),
            CustomMetricsLimit=json_data.get("CustomMetricsLimit"),
            CustomMetricsNotificationThreshold=json_data.get("CustomMetricsNotificationThreshold"),
            HighResMetricsLimit=json_data.get("HighResMetricsLimit"),
            HighResMetricsNotificationThreshold=json_data.get("HighResMetricsNotificationThreshold"),
            HostLimit=json_data.get("HostLimit"),
            HostNotificationThreshold=json_data.get("HostNotificationThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostOrUsageLimitsDefinition = HostOrUsageLimitsDefinition


