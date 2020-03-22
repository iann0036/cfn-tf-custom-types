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
    AutoPlacement: Optional[str]
    AvailabilityZone: Optional[str]
    AvailableMemory: Optional[str]
    AvailableVcpus: Optional[str]
    Cores: Optional[str]
    HostType: Optional[str]
    HostTypeName: Optional[str]
    Id: Optional[str]
    InstanceTotal: Optional[str]
    InstanceUuids: Optional[Sequence[str]]
    Memory: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Sockets: Optional[str]
    Status: Optional[str]
    Vcpus: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoPlacement=json_data.get("AutoPlacement"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AvailableMemory=json_data.get("AvailableMemory"),
            AvailableVcpus=json_data.get("AvailableVcpus"),
            Cores=json_data.get("Cores"),
            HostType=json_data.get("HostType"),
            HostTypeName=json_data.get("HostTypeName"),
            Id=json_data.get("Id"),
            InstanceTotal=json_data.get("InstanceTotal"),
            InstanceUuids=json_data.get("InstanceUuids"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Sockets=json_data.get("Sockets"),
            Status=json_data.get("Status"),
            Vcpus=json_data.get("Vcpus"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


