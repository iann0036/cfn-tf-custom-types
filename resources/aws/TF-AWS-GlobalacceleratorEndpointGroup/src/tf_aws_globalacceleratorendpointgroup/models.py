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
    Arn: Optional[str]
    EndpointGroupRegion: Optional[str]
    HealthCheckIntervalSeconds: Optional[float]
    HealthCheckPath: Optional[str]
    HealthCheckPort: Optional[float]
    HealthCheckProtocol: Optional[str]
    Id: Optional[str]
    ListenerArn: Optional[str]
    ThresholdCount: Optional[float]
    TrafficDialPercentage: Optional[float]
    EndpointConfiguration: Optional[Sequence["_EndpointConfigurationDefinition"]]
    PortOverride: Optional[Sequence["_PortOverrideDefinition"]]
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
            Arn=json_data.get("Arn"),
            EndpointGroupRegion=json_data.get("EndpointGroupRegion"),
            HealthCheckIntervalSeconds=json_data.get("HealthCheckIntervalSeconds"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            HealthCheckProtocol=json_data.get("HealthCheckProtocol"),
            Id=json_data.get("Id"),
            ListenerArn=json_data.get("ListenerArn"),
            ThresholdCount=json_data.get("ThresholdCount"),
            TrafficDialPercentage=json_data.get("TrafficDialPercentage"),
            EndpointConfiguration=deserialize_list(json_data.get("EndpointConfiguration"), EndpointConfigurationDefinition),
            PortOverride=deserialize_list(json_data.get("PortOverride"), PortOverrideDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointConfigurationDefinition(BaseModel):
    ClientIpPreservationEnabled: Optional[bool]
    EndpointId: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIpPreservationEnabled=json_data.get("ClientIpPreservationEnabled"),
            EndpointId=json_data.get("EndpointId"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigurationDefinition = EndpointConfigurationDefinition


@dataclass
class PortOverrideDefinition(BaseModel):
    EndpointPort: Optional[float]
    ListenerPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointPort=json_data.get("EndpointPort"),
            ListenerPort=json_data.get("ListenerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortOverrideDefinition = PortOverrideDefinition


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


