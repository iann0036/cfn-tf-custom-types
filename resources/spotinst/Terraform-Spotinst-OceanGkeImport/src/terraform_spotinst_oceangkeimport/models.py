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
    ClusterControllerId: Optional[str]
    ClusterName: Optional[str]
    DesiredCapacity: Optional[float]
    Id: Optional[str]
    Location: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Whitelist: Optional[Sequence[str]]
    BackendServices: Optional[Sequence["_BackendServices"]]
    NamedPorts: Optional[Sequence["_NamedPorts"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterControllerId=json_data.get("ClusterControllerId"),
            ClusterName=json_data.get("ClusterName"),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Whitelist=json_data.get("Whitelist"),
            BackendServices=json_data.get("BackendServices"),
            NamedPorts=json_data.get("NamedPorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendServices:
    LocationType: Optional[str]
    Scheme: Optional[str]
    ServiceName: Optional[str]
    NamedPorts: Optional[Sequence["_NamedPorts"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendServices"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendServices"]:
        if not json_data:
            return None
        return cls(
            LocationType=json_data.get("LocationType"),
            Scheme=json_data.get("Scheme"),
            ServiceName=json_data.get("ServiceName"),
            NamedPorts=json_data.get("NamedPorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendServices = BackendServices


@dataclass
class NamedPorts:
    Name: Optional[str]
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NamedPorts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedPorts"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedPorts = NamedPorts


