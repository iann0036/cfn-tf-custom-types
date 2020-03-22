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
    Arn: Optional[str]
    CreatedDate: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Spec: Optional[Sequence["_Spec"]]
    Backend: Optional[Sequence["_Backend"]]
    Listener: Optional[Sequence["_Listener"]]
    Logging: Optional[Sequence["_Logging"]]
    ServiceDiscovery: Optional[Sequence["_ServiceDiscovery"]]
    VirtualService: Optional[Sequence["_VirtualService"]]
    HealthCheck: Optional[Sequence["_HealthCheck"]]
    PortMapping: Optional[Sequence["_PortMapping"]]
    AccessLog: Optional[Sequence["_AccessLog"]]
    AwsCloudMap: Optional[Sequence["_AwsCloudMap"]]
    Dns: Optional[Sequence["_Dns"]]
    File: Optional[Sequence["_File"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CreatedDate=json_data.get("CreatedDate"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Spec=json_data.get("Spec"),
            Backend=json_data.get("Backend"),
            Listener=json_data.get("Listener"),
            Logging=json_data.get("Logging"),
            ServiceDiscovery=json_data.get("ServiceDiscovery"),
            VirtualService=json_data.get("VirtualService"),
            HealthCheck=json_data.get("HealthCheck"),
            PortMapping=json_data.get("PortMapping"),
            AccessLog=json_data.get("AccessLog"),
            AwsCloudMap=json_data.get("AwsCloudMap"),
            Dns=json_data.get("Dns"),
            File=json_data.get("File"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Spec:
    Backends: Optional[Sequence[str]]
    Backend: Optional[Sequence["_Backend"]]
    Listener: Optional[Sequence["_Listener"]]
    Logging: Optional[Sequence["_Logging"]]
    ServiceDiscovery: Optional[Sequence["_ServiceDiscovery"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            Backends=json_data.get("Backends"),
            Backend=json_data.get("Backend"),
            Listener=json_data.get("Listener"),
            Logging=json_data.get("Logging"),
            ServiceDiscovery=json_data.get("ServiceDiscovery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Backend:
    VirtualService: Optional[Sequence["_VirtualService"]]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
        if not json_data:
            return None
        return cls(
            VirtualService=json_data.get("VirtualService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


@dataclass
class VirtualService:
    VirtualServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualService"]:
        if not json_data:
            return None
        return cls(
            VirtualServiceName=json_data.get("VirtualServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualService = VirtualService


@dataclass
class Listener:
    HealthCheck: Optional[Sequence["_HealthCheck"]]
    PortMapping: Optional[Sequence["_PortMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listener"]:
        if not json_data:
            return None
        return cls(
            HealthCheck=json_data.get("HealthCheck"),
            PortMapping=json_data.get("PortMapping"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listener = Listener


@dataclass
class HealthCheck:
    HealthyThreshold: Optional[float]
    IntervalMillis: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TimeoutMillis: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheck"]:
        if not json_data:
            return None
        return cls(
            HealthyThreshold=json_data.get("HealthyThreshold"),
            IntervalMillis=json_data.get("IntervalMillis"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TimeoutMillis=json_data.get("TimeoutMillis"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


@dataclass
class PortMapping:
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMapping"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMapping = PortMapping


@dataclass
class Logging:
    AccessLog: Optional[Sequence["_AccessLog"]]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            AccessLog=json_data.get("AccessLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class AccessLog:
    File: Optional[Sequence["_File"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLog"]:
        if not json_data:
            return None
        return cls(
            File=json_data.get("File"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLog = AccessLog


@dataclass
class File:
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_File"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_File"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_File = File


@dataclass
class ServiceDiscovery:
    AwsCloudMap: Optional[Sequence["_AwsCloudMap"]]
    Dns: Optional[Sequence["_Dns"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDiscovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDiscovery"]:
        if not json_data:
            return None
        return cls(
            AwsCloudMap=json_data.get("AwsCloudMap"),
            Dns=json_data.get("Dns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDiscovery = ServiceDiscovery


@dataclass
class AwsCloudMap:
    Attributes: Optional[Sequence["_Attributes"]]
    NamespaceName: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudMap"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            NamespaceName=json_data.get("NamespaceName"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudMap = AwsCloudMap


@dataclass
class Attributes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


@dataclass
class Dns:
    Hostname: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dns"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dns = Dns


