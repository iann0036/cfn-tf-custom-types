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
    HyperVGeneration: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SourceVirtualMachineId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ZoneResilient: Optional[bool]
    DataDisk: Optional[Sequence["_DataDisk"]]
    OsDisk: Optional[Sequence["_OsDisk"]]
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
            HyperVGeneration=json_data.get("HyperVGeneration"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceVirtualMachineId=json_data.get("SourceVirtualMachineId"),
            Tags=json_data.get("Tags"),
            ZoneResilient=json_data.get("ZoneResilient"),
            DataDisk=json_data.get("DataDisk"),
            OsDisk=json_data.get("OsDisk"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class DataDisk:
    BlobUri: Optional[str]
    Caching: Optional[str]
    Lun: Optional[float]
    ManagedDiskId: Optional[str]
    SizeGb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisk"]:
        if not json_data:
            return None
        return cls(
            BlobUri=json_data.get("BlobUri"),
            Caching=json_data.get("Caching"),
            Lun=json_data.get("Lun"),
            ManagedDiskId=json_data.get("ManagedDiskId"),
            SizeGb=json_data.get("SizeGb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisk = DataDisk


@dataclass
class OsDisk:
    BlobUri: Optional[str]
    Caching: Optional[str]
    ManagedDiskId: Optional[str]
    OsState: Optional[str]
    OsType: Optional[str]
    SizeGb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OsDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDisk"]:
        if not json_data:
            return None
        return cls(
            BlobUri=json_data.get("BlobUri"),
            Caching=json_data.get("Caching"),
            ManagedDiskId=json_data.get("ManagedDiskId"),
            OsState=json_data.get("OsState"),
            OsType=json_data.get("OsType"),
            SizeGb=json_data.get("SizeGb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDisk = OsDisk


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


