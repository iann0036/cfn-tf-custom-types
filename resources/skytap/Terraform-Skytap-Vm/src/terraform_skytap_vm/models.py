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
    Cpus: Optional[float]
    EnvironmentId: Optional[str]
    MaxCpus: Optional[float]
    MaxRam: Optional[float]
    Name: Optional[str]
    OsDiskSize: Optional[float]
    Ram: Optional[float]
    ServiceIps: Optional[Sequence["_ServiceIps"]]
    ServicePorts: Optional[Sequence["_ServicePorts"]]
    TemplateId: Optional[str]
    UserData: Optional[str]
    VmId: Optional[str]
    Disk: Optional[Sequence["_Disk"]]
    Label: Optional[Sequence["_Label"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    PublishedService: Optional[Sequence["_PublishedService"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cpus=json_data.get("Cpus"),
            EnvironmentId=json_data.get("EnvironmentId"),
            MaxCpus=json_data.get("MaxCpus"),
            MaxRam=json_data.get("MaxRam"),
            Name=json_data.get("Name"),
            OsDiskSize=json_data.get("OsDiskSize"),
            Ram=json_data.get("Ram"),
            ServiceIps=json_data.get("ServiceIps"),
            ServicePorts=json_data.get("ServicePorts"),
            TemplateId=json_data.get("TemplateId"),
            UserData=json_data.get("UserData"),
            VmId=json_data.get("VmId"),
            Disk=json_data.get("Disk"),
            Label=json_data.get("Label"),
            NetworkInterface=json_data.get("NetworkInterface"),
            PublishedService=json_data.get("PublishedService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceIps:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIps"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIps"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIps = ServiceIps


@dataclass
class ServicePorts:
    Key: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePorts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePorts"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePorts = ServicePorts


@dataclass
class Disk:
    Name: Optional[str]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class Label:
    Category: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Label"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Label"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Label = Label


@dataclass
class NetworkInterface:
    Hostname: Optional[str]
    InterfaceType: Optional[str]
    Ip: Optional[str]
    NetworkId: Optional[str]
    PublishedService: Optional[Sequence["_PublishedService"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            InterfaceType=json_data.get("InterfaceType"),
            Ip=json_data.get("Ip"),
            NetworkId=json_data.get("NetworkId"),
            PublishedService=json_data.get("PublishedService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class PublishedService:
    InternalPort: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublishedService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishedService"]:
        if not json_data:
            return None
        return cls(
            InternalPort=json_data.get("InternalPort"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishedService = PublishedService


