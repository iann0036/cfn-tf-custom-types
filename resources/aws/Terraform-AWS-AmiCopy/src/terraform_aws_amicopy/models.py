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
    Architecture: Optional[str]
    Description: Optional[str]
    EnaSupport: Optional[bool]
    Encrypted: Optional[bool]
    ImageLocation: Optional[str]
    KernelId: Optional[str]
    KmsKeyId: Optional[str]
    ManageEbsSnapshots: Optional[bool]
    Name: Optional[str]
    RamdiskId: Optional[str]
    RootDeviceName: Optional[str]
    RootSnapshotId: Optional[str]
    SourceAmiId: Optional[str]
    SourceAmiRegion: Optional[str]
    SriovNetSupport: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VirtualizationType: Optional[str]
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
            Architecture=json_data.get("Architecture"),
            Description=json_data.get("Description"),
            EnaSupport=json_data.get("EnaSupport"),
            Encrypted=json_data.get("Encrypted"),
            ImageLocation=json_data.get("ImageLocation"),
            KernelId=json_data.get("KernelId"),
            KmsKeyId=json_data.get("KmsKeyId"),
            ManageEbsSnapshots=json_data.get("ManageEbsSnapshots"),
            Name=json_data.get("Name"),
            RamdiskId=json_data.get("RamdiskId"),
            RootDeviceName=json_data.get("RootDeviceName"),
            RootSnapshotId=json_data.get("RootSnapshotId"),
            SourceAmiId=json_data.get("SourceAmiId"),
            SourceAmiRegion=json_data.get("SourceAmiRegion"),
            SriovNetSupport=json_data.get("SriovNetSupport"),
            Tags=json_data.get("Tags"),
            VirtualizationType=json_data.get("VirtualizationType"),
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


