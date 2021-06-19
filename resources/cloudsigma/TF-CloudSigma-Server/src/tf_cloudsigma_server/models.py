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
    Cpu: Optional[float]
    Id: Optional[str]
    Ipv4Address: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    ResourceUri: Optional[str]
    Smp: Optional[float]
    SshKeys: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    VncPassword: Optional[str]
    Drive: Optional[Sequence["_DriveDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
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
            Cpu=json_data.get("Cpu"),
            Id=json_data.get("Id"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            ResourceUri=json_data.get("ResourceUri"),
            Smp=json_data.get("Smp"),
            SshKeys=json_data.get("SshKeys"),
            Tags=json_data.get("Tags"),
            VncPassword=json_data.get("VncPassword"),
            Drive=deserialize_list(json_data.get("Drive"), DriveDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DriveDefinition(BaseModel):
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriveDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriveDefinition = DriveDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Ipv4Address: Optional[str]
    Type: Optional[str]
    VlanUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Address=json_data.get("Ipv4Address"),
            Type=json_data.get("Type"),
            VlanUuid=json_data.get("VlanUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


