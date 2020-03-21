# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Commitment: Optional[str]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SpecificReservationRequired: Optional[bool]
    Status: Optional[str]
    Zone: Optional[str]
    SpecificReservation: Optional[Sequence["_SpecificReservation"]]
    Timeouts: Optional["_Timeouts"]
    InstanceProperties: Optional[Sequence["_InstanceProperties"]]
    GuestAccelerators: Optional[Sequence["_GuestAccelerators"]]
    LocalSsds: Optional[Sequence["_LocalSsds"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Commitment=json_data.get("Commitment"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SpecificReservationRequired=json_data.get("SpecificReservationRequired"),
            Status=json_data.get("Status"),
            Zone=json_data.get("Zone"),
            SpecificReservation=json_data.get("SpecificReservation"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            InstanceProperties=json_data.get("InstanceProperties"),
            GuestAccelerators=json_data.get("GuestAccelerators"),
            LocalSsds=json_data.get("LocalSsds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SpecificReservation:
    Count: Optional[float]
    InstanceProperties: Optional[Sequence["_InstanceProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecificReservation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecificReservation"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            InstanceProperties=json_data.get("InstanceProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecificReservation = SpecificReservation


@dataclass
class InstanceProperties:
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    GuestAccelerators: Optional[Sequence["_GuestAccelerators"]]
    LocalSsds: Optional[Sequence["_LocalSsds"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceProperties"]:
        if not json_data:
            return None
        return cls(
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            GuestAccelerators=json_data.get("GuestAccelerators"),
            LocalSsds=json_data.get("LocalSsds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceProperties = InstanceProperties


@dataclass
class GuestAccelerators:
    AcceleratorCount: Optional[float]
    AcceleratorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestAccelerators"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestAccelerators"]:
        if not json_data:
            return None
        return cls(
            AcceleratorCount=json_data.get("AcceleratorCount"),
            AcceleratorType=json_data.get("AcceleratorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestAccelerators = GuestAccelerators


@dataclass
class LocalSsds:
    DiskSizeGb: Optional[float]
    Interface: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSsds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSsds"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Interface=json_data.get("Interface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSsds = LocalSsds


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


