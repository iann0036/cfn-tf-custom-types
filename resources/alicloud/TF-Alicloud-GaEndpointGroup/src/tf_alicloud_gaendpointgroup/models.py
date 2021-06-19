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
    AcceleratorId: Optional[str]
    Description: Optional[str]
    EndpointGroupRegion: Optional[str]
    EndpointGroupType: Optional[str]
    EndpointRequestProtocol: Optional[str]
    HealthCheckIntervalSeconds: Optional[float]
    HealthCheckPath: Optional[str]
    HealthCheckPort: Optional[float]
    HealthCheckProtocol: Optional[str]
    Id: Optional[str]
    ListenerId: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    ThresholdCount: Optional[float]
    TrafficPercentage: Optional[float]
    EndpointConfigurations: Optional[Sequence["_EndpointConfigurationsDefinition"]]
    PortOverrides: Optional[Sequence["_PortOverridesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AcceleratorId=json_data.get("AcceleratorId"),
            Description=json_data.get("Description"),
            EndpointGroupRegion=json_data.get("EndpointGroupRegion"),
            EndpointGroupType=json_data.get("EndpointGroupType"),
            EndpointRequestProtocol=json_data.get("EndpointRequestProtocol"),
            HealthCheckIntervalSeconds=json_data.get("HealthCheckIntervalSeconds"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            HealthCheckProtocol=json_data.get("HealthCheckProtocol"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            ThresholdCount=json_data.get("ThresholdCount"),
            TrafficPercentage=json_data.get("TrafficPercentage"),
            EndpointConfigurations=deserialize_list(json_data.get("EndpointConfigurations"), EndpointConfigurationsDefinition),
            PortOverrides=deserialize_list(json_data.get("PortOverrides"), PortOverridesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointConfigurationsDefinition(BaseModel):
    EnableClientipPreservation: Optional[bool]
    Endpoint: Optional[str]
    Type: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableClientipPreservation=json_data.get("EnableClientipPreservation"),
            Endpoint=json_data.get("Endpoint"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigurationsDefinition = EndpointConfigurationsDefinition


@dataclass
class PortOverridesDefinition(BaseModel):
    EndpointPort: Optional[float]
    ListenerPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointPort=json_data.get("EndpointPort"),
            ListenerPort=json_data.get("ListenerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortOverridesDefinition = PortOverridesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


