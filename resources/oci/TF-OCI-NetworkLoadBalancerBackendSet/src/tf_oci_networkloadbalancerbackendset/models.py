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
    Backends: Optional[Sequence["_BackendsDefinition"]]
    Id: Optional[str]
    IsPreserveSource: Optional[bool]
    Name: Optional[str]
    NetworkLoadBalancerId: Optional[str]
    Policy: Optional[str]
    HealthChecker: Optional[Sequence["_HealthCheckerDefinition"]]
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
            Backends=deserialize_list(json_data.get("Backends"), BackendsDefinition),
            Id=json_data.get("Id"),
            IsPreserveSource=json_data.get("IsPreserveSource"),
            Name=json_data.get("Name"),
            NetworkLoadBalancerId=json_data.get("NetworkLoadBalancerId"),
            Policy=json_data.get("Policy"),
            HealthChecker=deserialize_list(json_data.get("HealthChecker"), HealthCheckerDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendsDefinition(BaseModel):
    IpAddress: Optional[str]
    IsBackup: Optional[bool]
    IsDrain: Optional[bool]
    IsOffline: Optional[bool]
    Name: Optional[str]
    Port: Optional[float]
    TargetId: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            IsBackup=json_data.get("IsBackup"),
            IsDrain=json_data.get("IsDrain"),
            IsOffline=json_data.get("IsOffline"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            TargetId=json_data.get("TargetId"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendsDefinition = BackendsDefinition


@dataclass
class HealthCheckerDefinition(BaseModel):
    IntervalInMillis: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    RequestData: Optional[str]
    ResponseBodyRegex: Optional[str]
    ResponseData: Optional[str]
    Retries: Optional[float]
    ReturnCode: Optional[float]
    TimeoutInMillis: Optional[float]
    UrlPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckerDefinition"]:
        if not json_data:
            return None
        return cls(
            IntervalInMillis=json_data.get("IntervalInMillis"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            RequestData=json_data.get("RequestData"),
            ResponseBodyRegex=json_data.get("ResponseBodyRegex"),
            ResponseData=json_data.get("ResponseData"),
            Retries=json_data.get("Retries"),
            ReturnCode=json_data.get("ReturnCode"),
            TimeoutInMillis=json_data.get("TimeoutInMillis"),
            UrlPath=json_data.get("UrlPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckerDefinition = HealthCheckerDefinition


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


