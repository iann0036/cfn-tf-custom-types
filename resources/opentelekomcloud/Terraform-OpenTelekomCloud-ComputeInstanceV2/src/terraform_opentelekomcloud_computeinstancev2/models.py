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
    AllMetadata: Optional[Sequence["_AllMetadata"]]
    AutoRecovery: Optional[bool]
    AvailabilityZone: Optional[str]
    ConfigDrive: Optional[bool]
    FlavorId: Optional[str]
    FlavorName: Optional[str]
    FloatingIp: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    KeyPair: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Region: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    StopBeforeDestroy: Optional[bool]
    Tag: Optional[Sequence["_Tag"]]
    Tags: Optional[Sequence[str]]
    UserData: Optional[str]
    VolumeAttached: Optional[Sequence["_VolumeAttached"]]
    BlockDevice: Optional[Sequence["_BlockDevice"]]
    Network: Optional[Sequence["_Network"]]
    Personality: Optional[Sequence["_Personality"]]
    SchedulerHints: Optional[Sequence["_SchedulerHints"]]
    Timeouts: Optional["_Timeouts"]
    Volume: Optional[Sequence["_Volume"]]

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
            AllMetadata=json_data.get("AllMetadata"),
            AutoRecovery=json_data.get("AutoRecovery"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ConfigDrive=json_data.get("ConfigDrive"),
            FlavorId=json_data.get("FlavorId"),
            FlavorName=json_data.get("FlavorName"),
            FloatingIp=json_data.get("FloatingIp"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            KeyPair=json_data.get("KeyPair"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SecurityGroups=json_data.get("SecurityGroups"),
            StopBeforeDestroy=json_data.get("StopBeforeDestroy"),
            Tag=json_data.get("Tag"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            VolumeAttached=json_data.get("VolumeAttached"),
            BlockDevice=json_data.get("BlockDevice"),
            Network=json_data.get("Network"),
            Personality=json_data.get("Personality"),
            SchedulerHints=json_data.get("SchedulerHints"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllMetadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllMetadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllMetadata = AllMetadata


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Tag:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class VolumeAttached:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeAttached"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeAttached"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeAttached = VolumeAttached


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
    FloatingIp: Optional[str]
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
            FloatingIp=json_data.get("FloatingIp"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


@dataclass
class Personality:
    Content: Optional[str]
    File: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Personality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Personality"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            File=json_data.get("File"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Personality = Personality


@dataclass
class SchedulerHints:
    BuildNearHostIp: Optional[str]
    DehId: Optional[str]
    DifferentHost: Optional[Sequence[str]]
    Group: Optional[str]
    Query: Optional[Sequence[str]]
    SameHost: Optional[Sequence[str]]
    TargetCell: Optional[str]
    Tenancy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulerHints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulerHints"]:
        if not json_data:
            return None
        return cls(
            BuildNearHostIp=json_data.get("BuildNearHostIp"),
            DehId=json_data.get("DehId"),
            DifferentHost=json_data.get("DifferentHost"),
            Group=json_data.get("Group"),
            Query=json_data.get("Query"),
            SameHost=json_data.get("SameHost"),
            TargetCell=json_data.get("TargetCell"),
            Tenancy=json_data.get("Tenancy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulerHints = SchedulerHints


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


@dataclass
class Volume:
    Device: Optional[str]
    Id: Optional[str]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            Id=json_data.get("Id"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


