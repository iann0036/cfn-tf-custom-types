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
    Commitment: Optional[str]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SpecificReservationRequired: Optional[bool]
    Status: Optional[str]
    Zone: Optional[str]
    SpecificReservation: Optional[Sequence["_SpecificReservationDefinition"]]
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
            Commitment=json_data.get("Commitment"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SpecificReservationRequired=json_data.get("SpecificReservationRequired"),
            Status=json_data.get("Status"),
            Zone=json_data.get("Zone"),
            SpecificReservation=deserialize_list(json_data.get("SpecificReservation"), SpecificReservationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SpecificReservationDefinition(BaseModel):
    Count: Optional[float]
    InstanceProperties: Optional[Sequence["_InstancePropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecificReservationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecificReservationDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            InstanceProperties=deserialize_list(json_data.get("InstanceProperties"), InstancePropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecificReservationDefinition = SpecificReservationDefinition


@dataclass
class InstancePropertiesDefinition(BaseModel):
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    GuestAccelerators: Optional[Sequence["_GuestAcceleratorsDefinition"]]
    LocalSsds: Optional[Sequence["_LocalSsdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstancePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            GuestAccelerators=deserialize_list(json_data.get("GuestAccelerators"), GuestAcceleratorsDefinition),
            LocalSsds=deserialize_list(json_data.get("LocalSsds"), LocalSsdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancePropertiesDefinition = InstancePropertiesDefinition


@dataclass
class GuestAcceleratorsDefinition(BaseModel):
    AcceleratorCount: Optional[float]
    AcceleratorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestAcceleratorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestAcceleratorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceleratorCount=json_data.get("AcceleratorCount"),
            AcceleratorType=json_data.get("AcceleratorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestAcceleratorsDefinition = GuestAcceleratorsDefinition


@dataclass
class LocalSsdsDefinition(BaseModel):
    DiskSizeGb: Optional[float]
    Interface: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSsdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSsdsDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Interface=json_data.get("Interface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSsdsDefinition = LocalSsdsDefinition


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


