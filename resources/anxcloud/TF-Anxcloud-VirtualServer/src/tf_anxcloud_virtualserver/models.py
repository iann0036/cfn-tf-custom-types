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
    BootDelay: Optional[float]
    CpuPerformanceType: Optional[str]
    Cpus: Optional[float]
    CriticalOperationConfirmed: Optional[bool]
    Dns: Optional[Sequence[str]]
    EnterBiosSetup: Optional[bool]
    ForceRestartIfNeeded: Optional[bool]
    Hostname: Optional[str]
    Id: Optional[str]
    Info: Optional[Sequence["_InfoDefinition3"]]
    LocationId: Optional[str]
    Memory: Optional[float]
    Password: Optional[str]
    Script: Optional[str]
    Sockets: Optional[float]
    SshKey: Optional[str]
    Tags: Optional[Sequence[str]]
    TemplateId: Optional[str]
    TemplateType: Optional[str]
    Disk: Optional[Sequence["_DiskDefinition"]]
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
            BootDelay=json_data.get("BootDelay"),
            CpuPerformanceType=json_data.get("CpuPerformanceType"),
            Cpus=json_data.get("Cpus"),
            CriticalOperationConfirmed=json_data.get("CriticalOperationConfirmed"),
            Dns=json_data.get("Dns"),
            EnterBiosSetup=json_data.get("EnterBiosSetup"),
            ForceRestartIfNeeded=json_data.get("ForceRestartIfNeeded"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Info=deserialize_list(json_data.get("Info"), InfoDefinition3),
            LocationId=json_data.get("LocationId"),
            Memory=json_data.get("Memory"),
            Password=json_data.get("Password"),
            Script=json_data.get("Script"),
            Sockets=json_data.get("Sockets"),
            SshKey=json_data.get("SshKey"),
            Tags=json_data.get("Tags"),
            TemplateId=json_data.get("TemplateId"),
            TemplateType=json_data.get("TemplateType"),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InfoDefinition3(BaseModel):
    Cores: Optional[float]
    Cpu: Optional[float]
    CustomName: Optional[str]
    DisksInfo: Optional[Sequence["_InfoDefinition"]]
    DisksNumber: Optional[float]
    GuestOs: Optional[str]
    GuestToolsStatus: Optional[str]
    Identifier: Optional[str]
    LocationCode: Optional[str]
    LocationCountry: Optional[str]
    LocationName: Optional[str]
    Name: Optional[str]
    Network: Optional[Sequence["_InfoDefinition2"]]
    Ram: Optional[float]
    Status: Optional[str]
    VersionTools: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfoDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoDefinition3"]:
        if not json_data:
            return None
        return cls(
            Cores=json_data.get("Cores"),
            Cpu=json_data.get("Cpu"),
            CustomName=json_data.get("CustomName"),
            DisksInfo=deserialize_list(json_data.get("DisksInfo"), InfoDefinition),
            DisksNumber=json_data.get("DisksNumber"),
            GuestOs=json_data.get("GuestOs"),
            GuestToolsStatus=json_data.get("GuestToolsStatus"),
            Identifier=json_data.get("Identifier"),
            LocationCode=json_data.get("LocationCode"),
            LocationCountry=json_data.get("LocationCountry"),
            LocationName=json_data.get("LocationName"),
            Name=json_data.get("Name"),
            Network=deserialize_list(json_data.get("Network"), InfoDefinition2),
            Ram=json_data.get("Ram"),
            Status=json_data.get("Status"),
            VersionTools=json_data.get("VersionTools"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoDefinition3 = InfoDefinition3


@dataclass
class InfoDefinition(BaseModel):
    BusType: Optional[str]
    BusTypeLabel: Optional[str]
    DiskGb: Optional[float]
    DiskId: Optional[float]
    DiskType: Optional[str]
    Iops: Optional[float]
    Latency: Optional[float]
    StorageType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            BusType=json_data.get("BusType"),
            BusTypeLabel=json_data.get("BusTypeLabel"),
            DiskGb=json_data.get("DiskGb"),
            DiskId=json_data.get("DiskId"),
            DiskType=json_data.get("DiskType"),
            Iops=json_data.get("Iops"),
            Latency=json_data.get("Latency"),
            StorageType=json_data.get("StorageType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoDefinition = InfoDefinition


@dataclass
class InfoDefinition2(BaseModel):
    Id: Optional[float]
    IpV4: Optional[Sequence[str]]
    IpV6: Optional[Sequence[str]]
    MacAddress: Optional[str]
    Nic: Optional[float]
    Vlan: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfoDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoDefinition2"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IpV4=json_data.get("IpV4"),
            IpV6=json_data.get("IpV6"),
            MacAddress=json_data.get("MacAddress"),
            Nic=json_data.get("Nic"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoDefinition2 = InfoDefinition2


@dataclass
class DiskDefinition(BaseModel):
    DiskGb: Optional[float]
    DiskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskGb=json_data.get("DiskGb"),
            DiskType=json_data.get("DiskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Ips: Optional[Sequence[str]]
    NicType: Optional[str]
    VlanId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Ips=json_data.get("Ips"),
            NicType=json_data.get("NicType"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


