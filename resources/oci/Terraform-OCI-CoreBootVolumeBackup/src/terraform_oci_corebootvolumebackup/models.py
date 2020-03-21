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
    BootVolumeId: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    ExpirationTime: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    ImageId: Optional[str]
    KmsKeyId: Optional[str]
    SizeInGbs: Optional[str]
    SourceBootVolumeBackupId: Optional[str]
    SourceType: Optional[str]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTags"]]
    TimeCreated: Optional[str]
    TimeRequestReceived: Optional[str]
    Type: Optional[str]
    UniqueSizeInGbs: Optional[str]
    SourceDetails: Optional[Sequence["_SourceDetails"]]
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
            BootVolumeId=json_data.get("BootVolumeId"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            ExpirationTime=json_data.get("ExpirationTime"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SizeInGbs=json_data.get("SizeInGbs"),
            SourceBootVolumeBackupId=json_data.get("SourceBootVolumeBackupId"),
            SourceType=json_data.get("SourceType"),
            State=json_data.get("State"),
            SystemTags=json_data.get("SystemTags"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeRequestReceived=json_data.get("TimeRequestReceived"),
            Type=json_data.get("Type"),
            UniqueSizeInGbs=json_data.get("UniqueSizeInGbs"),
            SourceDetails=json_data.get("SourceDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class SystemTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTags = SystemTags


@dataclass
class SourceDetails:
    BootVolumeBackupId: Optional[str]
    KmsKeyId: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetails"]:
        if not json_data:
            return None
        return cls(
            BootVolumeBackupId=json_data.get("BootVolumeBackupId"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetails = SourceDetails


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


