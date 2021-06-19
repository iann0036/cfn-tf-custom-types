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
    AutoTerminateInstanceOnDelete: Optional[bool]
    AvailabilityDomain: Optional[str]
    CompartmentId: Optional[str]
    DecrementSizeOnDelete: Optional[bool]
    DisplayName: Optional[str]
    FaultDomain: Optional[str]
    Id: Optional[str]
    InstanceConfigurationId: Optional[str]
    InstanceId: Optional[str]
    InstancePoolId: Optional[str]
    LoadBalancerBackends: Optional[Sequence["_LoadBalancerBackendsDefinition"]]
    Region: Optional[str]
    Shape: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
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
            AutoTerminateInstanceOnDelete=json_data.get("AutoTerminateInstanceOnDelete"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CompartmentId=json_data.get("CompartmentId"),
            DecrementSizeOnDelete=json_data.get("DecrementSizeOnDelete"),
            DisplayName=json_data.get("DisplayName"),
            FaultDomain=json_data.get("FaultDomain"),
            Id=json_data.get("Id"),
            InstanceConfigurationId=json_data.get("InstanceConfigurationId"),
            InstanceId=json_data.get("InstanceId"),
            InstancePoolId=json_data.get("InstancePoolId"),
            LoadBalancerBackends=deserialize_list(json_data.get("LoadBalancerBackends"), LoadBalancerBackendsDefinition),
            Region=json_data.get("Region"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoadBalancerBackendsDefinition(BaseModel):
    BackendHealthStatus: Optional[str]
    BackendName: Optional[str]
    BackendSetName: Optional[str]
    LoadBalancerId: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerBackendsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerBackendsDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendHealthStatus=json_data.get("BackendHealthStatus"),
            BackendName=json_data.get("BackendName"),
            BackendSetName=json_data.get("BackendSetName"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerBackendsDefinition = LoadBalancerBackendsDefinition


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


