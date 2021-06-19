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
    AccessIpV4: Optional[str]
    AllMetadata: Optional[Sequence["_AllMetadataDefinition"]]
    AvailabilityZone: Optional[str]
    ConfigDrive: Optional[bool]
    FlavorId: Optional[str]
    FlavorName: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    KeyPair: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    PowerState: Optional[str]
    Region: Optional[str]
    StopBeforeDestroy: Optional[bool]
    UserData: Optional[str]
    BlockDevice: Optional[Sequence["_BlockDeviceDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
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
            AccessIpV4=json_data.get("AccessIpV4"),
            AllMetadata=deserialize_list(json_data.get("AllMetadata"), AllMetadataDefinition),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ConfigDrive=json_data.get("ConfigDrive"),
            FlavorId=json_data.get("FlavorId"),
            FlavorName=json_data.get("FlavorName"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            KeyPair=json_data.get("KeyPair"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            PowerState=json_data.get("PowerState"),
            Region=json_data.get("Region"),
            StopBeforeDestroy=json_data.get("StopBeforeDestroy"),
            UserData=json_data.get("UserData"),
            BlockDevice=deserialize_list(json_data.get("BlockDevice"), BlockDeviceDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Volume=deserialize_list(json_data.get("Volume"), VolumeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllMetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllMetadataDefinition = AllMetadataDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class BlockDeviceDefinition(BaseModel):
    BootIndex: Optional[float]
    DeleteOnTermination: Optional[bool]
    DestinationType: Optional[str]
    SourceType: Optional[str]
    Uuid: Optional[str]
    VolumeSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            BootIndex=json_data.get("BootIndex"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DestinationType=json_data.get("DestinationType"),
            SourceType=json_data.get("SourceType"),
            Uuid=json_data.get("Uuid"),
            VolumeSize=json_data.get("VolumeSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceDefinition = BlockDeviceDefinition


@dataclass
class NetworkDefinition(BaseModel):
    AccessNetwork: Optional[bool]
    FixedIpV4: Optional[str]
    Name: Optional[str]
    Port: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessNetwork=json_data.get("AccessNetwork"),
            FixedIpV4=json_data.get("FixedIpV4"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


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


@dataclass
class VolumeDefinition(BaseModel):
    Device: Optional[str]
    Id: Optional[str]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            Id=json_data.get("Id"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeDefinition = VolumeDefinition


