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
    Id: Optional[str]
    InstancePoolId: Optional[str]
    Name: Optional[str]
    NlbId: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Strategy: Optional[str]
    TargetPort: Optional[float]
    Zone: Optional[str]
    Healthcheck: Optional[Sequence["_HealthcheckDefinition"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InstancePoolId=json_data.get("InstancePoolId"),
            Name=json_data.get("Name"),
            NlbId=json_data.get("NlbId"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Strategy=json_data.get("Strategy"),
            TargetPort=json_data.get("TargetPort"),
            Zone=json_data.get("Zone"),
            Healthcheck=deserialize_list(json_data.get("Healthcheck"), HealthcheckDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthcheckDefinition(BaseModel):
    Interval: Optional[float]
    Mode: Optional[str]
    Port: Optional[float]
    Retries: Optional[float]
    Timeout: Optional[float]
    TlsSni: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthcheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthcheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Mode=json_data.get("Mode"),
            Port=json_data.get("Port"),
            Retries=json_data.get("Retries"),
            Timeout=json_data.get("Timeout"),
            TlsSni=json_data.get("TlsSni"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthcheckDefinition = HealthcheckDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


