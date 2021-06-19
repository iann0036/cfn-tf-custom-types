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
    Cpus: Optional[float]
    EnvironmentId: Optional[str]
    Id: Optional[str]
    MaxCpus: Optional[float]
    MaxRam: Optional[float]
    Name: Optional[str]
    OsDiskSize: Optional[float]
    Ram: Optional[float]
    ServiceIps: Optional[Sequence["_ServiceIpsDefinition"]]
    ServicePorts: Optional[Sequence["_ServicePortsDefinition"]]
    TemplateId: Optional[str]
    UserData: Optional[str]
    VmId: Optional[str]
    Disk: Optional[Sequence["_DiskDefinition"]]
    Label: Optional[Sequence["_LabelDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
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
            Cpus=json_data.get("Cpus"),
            EnvironmentId=json_data.get("EnvironmentId"),
            Id=json_data.get("Id"),
            MaxCpus=json_data.get("MaxCpus"),
            MaxRam=json_data.get("MaxRam"),
            Name=json_data.get("Name"),
            OsDiskSize=json_data.get("OsDiskSize"),
            Ram=json_data.get("Ram"),
            ServiceIps=deserialize_list(json_data.get("ServiceIps"), ServiceIpsDefinition),
            ServicePorts=deserialize_list(json_data.get("ServicePorts"), ServicePortsDefinition),
            TemplateId=json_data.get("TemplateId"),
            UserData=json_data.get("UserData"),
            VmId=json_data.get("VmId"),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Label=deserialize_list(json_data.get("Label"), LabelDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceIpsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIpsDefinition = ServiceIpsDefinition


@dataclass
class ServicePortsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServicePortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicePortsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicePortsDefinition = ServicePortsDefinition


@dataclass
class DiskDefinition(BaseModel):
    Name: Optional[str]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class LabelDefinition(BaseModel):
    Category: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelDefinition = LabelDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    Hostname: Optional[str]
    InterfaceType: Optional[str]
    Ip: Optional[str]
    NetworkId: Optional[str]
    PublishedService: Optional[Sequence["_PublishedServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            InterfaceType=json_data.get("InterfaceType"),
            Ip=json_data.get("Ip"),
            NetworkId=json_data.get("NetworkId"),
            PublishedService=deserialize_list(json_data.get("PublishedService"), PublishedServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class PublishedServiceDefinition(BaseModel):
    InternalPort: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublishedServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishedServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            InternalPort=json_data.get("InternalPort"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishedServiceDefinition = PublishedServiceDefinition


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


