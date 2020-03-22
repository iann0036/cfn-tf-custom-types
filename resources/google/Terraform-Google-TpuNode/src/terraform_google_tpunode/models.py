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
    AcceleratorType: Optional[str]
    CidrBlock: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Network: Optional[str]
    NetworkEndpoints: Optional[Sequence["_NetworkEndpoints"]]
    Project: Optional[str]
    ServiceAccount: Optional[str]
    TensorflowVersion: Optional[str]
    Zone: Optional[str]
    SchedulingConfig: Optional[Sequence["_SchedulingConfig"]]
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
            AcceleratorType=json_data.get("AcceleratorType"),
            CidrBlock=json_data.get("CidrBlock"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            NetworkEndpoints=json_data.get("NetworkEndpoints"),
            Project=json_data.get("Project"),
            ServiceAccount=json_data.get("ServiceAccount"),
            TensorflowVersion=json_data.get("TensorflowVersion"),
            Zone=json_data.get("Zone"),
            SchedulingConfig=json_data.get("SchedulingConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class NetworkEndpoints:
    IpAddress: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkEndpoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkEndpoints"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkEndpoints = NetworkEndpoints


@dataclass
class SchedulingConfig:
    Preemptible: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulingConfig"]:
        if not json_data:
            return None
        return cls(
            Preemptible=json_data.get("Preemptible"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulingConfig = SchedulingConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


