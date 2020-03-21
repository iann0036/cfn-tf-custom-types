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
    Cmd: Optional[str]
    Endpoint: Optional[str]
    EndpointFullHostname: Optional[str]
    EndpointFullUrl: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    Instances: Optional[float]
    Memory: Optional[float]
    Name: Optional[str]
    Plan: Optional[str]
    PortMappings: Optional[Sequence["_PortMappings"]]
    Region: Optional[str]
    ServiceId: Optional[str]
    Environments: Optional[Sequence["_Environments"]]
    Ports: Optional[Sequence["_Ports"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cmd=json_data.get("Cmd"),
            Endpoint=json_data.get("Endpoint"),
            EndpointFullHostname=json_data.get("EndpointFullHostname"),
            EndpointFullUrl=json_data.get("EndpointFullUrl"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Instances=json_data.get("Instances"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            Plan=json_data.get("Plan"),
            PortMappings=json_data.get("PortMappings"),
            Region=json_data.get("Region"),
            ServiceId=json_data.get("ServiceId"),
            Environments=json_data.get("Environments"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortMappings:
    ContainerPort: Optional[float]
    Host: Optional[str]
    Ipaddress: Optional[str]
    ServicePort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMappings"]:
        if not json_data:
            return None
        return cls(
            ContainerPort=json_data.get("ContainerPort"),
            Host=json_data.get("Host"),
            Ipaddress=json_data.get("Ipaddress"),
            ServicePort=json_data.get("ServicePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMappings = PortMappings


@dataclass
class Environments:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environments"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environments = Environments


@dataclass
class Ports:
    Number: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            Number=json_data.get("Number"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


