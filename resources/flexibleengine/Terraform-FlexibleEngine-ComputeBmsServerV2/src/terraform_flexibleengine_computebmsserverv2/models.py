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
    AccessIpV4: Optional[str]
    AccessIpV6: Optional[str]
    AdminPass: Optional[str]
    AvailabilityZone: Optional[str]
    ConfigDrive: Optional[bool]
    FlavorId: Optional[str]
    FlavorName: Optional[str]
    HostId: Optional[str]
    HostStatus: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    KernelId: Optional[str]
    KeyPair: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Region: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    StopBeforeDestroy: Optional[bool]
    TenantId: Optional[str]
    UserData: Optional[str]
    UserId: Optional[str]
    BlockDevice: Optional[Sequence["_BlockDevice"]]
    Network: Optional[Sequence["_Network"]]
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
            AccessIpV4=json_data.get("AccessIpV4"),
            AccessIpV6=json_data.get("AccessIpV6"),
            AdminPass=json_data.get("AdminPass"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ConfigDrive=json_data.get("ConfigDrive"),
            FlavorId=json_data.get("FlavorId"),
            FlavorName=json_data.get("FlavorName"),
            HostId=json_data.get("HostId"),
            HostStatus=json_data.get("HostStatus"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            KernelId=json_data.get("KernelId"),
            KeyPair=json_data.get("KeyPair"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SecurityGroups=json_data.get("SecurityGroups"),
            StopBeforeDestroy=json_data.get("StopBeforeDestroy"),
            TenantId=json_data.get("TenantId"),
            UserData=json_data.get("UserData"),
            UserId=json_data.get("UserId"),
            BlockDevice=json_data.get("BlockDevice"),
            Network=json_data.get("Network"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class BlockDevice:
    BootIndex: Optional[float]
    DeleteOnTermination: Optional[bool]
    DestinationType: Optional[str]
    DeviceName: Optional[str]
    GuestFormat: Optional[str]
    SourceType: Optional[str]
    Uuid: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDevice"]:
        if not json_data:
            return None
        return cls(
            BootIndex=json_data.get("BootIndex"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DestinationType=json_data.get("DestinationType"),
            DeviceName=json_data.get("DeviceName"),
            GuestFormat=json_data.get("GuestFormat"),
            SourceType=json_data.get("SourceType"),
            Uuid=json_data.get("Uuid"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDevice = BlockDevice


@dataclass
class Network:
    AccessNetwork: Optional[bool]
    FixedIpV4: Optional[str]
    FixedIpV6: Optional[str]
    Name: Optional[str]
    Port: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            AccessNetwork=json_data.get("AccessNetwork"),
            FixedIpV4=json_data.get("FixedIpV4"),
            FixedIpV6=json_data.get("FixedIpV6"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


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


