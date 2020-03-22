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
    AutoRecovery: Optional[bool]
    AvailabilityZone: Optional[str]
    DeleteDisksOnTermination: Optional[bool]
    Flavor: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    KeyName: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UserData: Optional[str]
    VpcId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisks"]]
    Nics: Optional[Sequence["_Nics"]]
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
            AutoRecovery=json_data.get("AutoRecovery"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DeleteDisksOnTermination=json_data.get("DeleteDisksOnTermination"),
            Flavor=json_data.get("Flavor"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            KeyName=json_data.get("KeyName"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            VpcId=json_data.get("VpcId"),
            DataDisks=json_data.get("DataDisks"),
            Nics=json_data.get("Nics"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class DataDisks:
    Size: Optional[float]
    SnapshotId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisks"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisks = DataDisks


@dataclass
class Nics:
    IpAddress: Optional[str]
    NetworkId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nics"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            NetworkId=json_data.get("NetworkId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nics = Nics


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


