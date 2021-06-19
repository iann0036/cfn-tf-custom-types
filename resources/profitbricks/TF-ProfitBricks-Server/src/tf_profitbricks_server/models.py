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
    AvailabilityZone: Optional[str]
    BootCdrom: Optional[str]
    BootImage: Optional[str]
    BootVolume: Optional[str]
    Cores: Optional[float]
    CpuFamily: Optional[str]
    DatacenterId: Optional[str]
    FirewallruleId: Optional[str]
    Id: Optional[str]
    ImageName: Optional[str]
    ImagePassword: Optional[str]
    LicenceType: Optional[str]
    Name: Optional[str]
    PrimaryIp: Optional[str]
    PrimaryNic: Optional[str]
    Ram: Optional[float]
    SshKeyPath: Optional[Sequence[str]]
    Nic: Optional[Sequence["_NicDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Volume: Optional[Sequence["_VolumeDefinition"]]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BootCdrom=json_data.get("BootCdrom"),
            BootImage=json_data.get("BootImage"),
            BootVolume=json_data.get("BootVolume"),
            Cores=json_data.get("Cores"),
            CpuFamily=json_data.get("CpuFamily"),
            DatacenterId=json_data.get("DatacenterId"),
            FirewallruleId=json_data.get("FirewallruleId"),
            Id=json_data.get("Id"),
            ImageName=json_data.get("ImageName"),
            ImagePassword=json_data.get("ImagePassword"),
            LicenceType=json_data.get("LicenceType"),
            Name=json_data.get("Name"),
            PrimaryIp=json_data.get("PrimaryIp"),
            PrimaryNic=json_data.get("PrimaryNic"),
            Ram=json_data.get("Ram"),
            SshKeyPath=json_data.get("SshKeyPath"),
            Nic=deserialize_list(json_data.get("Nic"), NicDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Volume=deserialize_list(json_data.get("Volume"), VolumeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NicDefinition(BaseModel):
    Dhcp: Optional[bool]
    FirewallActive: Optional[bool]
    Ip: Optional[str]
    Lan: Optional[float]
    Name: Optional[str]
    Nat: Optional[bool]
    Firewall: Optional[Sequence["_FirewallDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicDefinition"]:
        if not json_data:
            return None
        return cls(
            Dhcp=json_data.get("Dhcp"),
            FirewallActive=json_data.get("FirewallActive"),
            Ip=json_data.get("Ip"),
            Lan=json_data.get("Lan"),
            Name=json_data.get("Name"),
            Nat=json_data.get("Nat"),
            Firewall=deserialize_list(json_data.get("Firewall"), FirewallDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicDefinition = NicDefinition


@dataclass
class FirewallDefinition(BaseModel):
    IcmpCode: Optional[str]
    IcmpType: Optional[str]
    Ip: Optional[str]
    Ips: Optional[Sequence[str]]
    Name: Optional[str]
    PortRangeEnd: Optional[float]
    PortRangeStart: Optional[float]
    Protocol: Optional[str]
    SourceIp: Optional[str]
    SourceMac: Optional[str]
    TargetIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallDefinition"]:
        if not json_data:
            return None
        return cls(
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Ip=json_data.get("Ip"),
            Ips=json_data.get("Ips"),
            Name=json_data.get("Name"),
            PortRangeEnd=json_data.get("PortRangeEnd"),
            PortRangeStart=json_data.get("PortRangeStart"),
            Protocol=json_data.get("Protocol"),
            SourceIp=json_data.get("SourceIp"),
            SourceMac=json_data.get("SourceMac"),
            TargetIp=json_data.get("TargetIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallDefinition = FirewallDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
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
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VolumeDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    Bus: Optional[str]
    DiskType: Optional[str]
    ImageName: Optional[str]
    ImagePassword: Optional[str]
    LicenceType: Optional[str]
    Name: Optional[str]
    Size: Optional[float]
    SshKeyPath: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Bus=json_data.get("Bus"),
            DiskType=json_data.get("DiskType"),
            ImageName=json_data.get("ImageName"),
            ImagePassword=json_data.get("ImagePassword"),
            LicenceType=json_data.get("LicenceType"),
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
            SshKeyPath=json_data.get("SshKeyPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeDefinition = VolumeDefinition


