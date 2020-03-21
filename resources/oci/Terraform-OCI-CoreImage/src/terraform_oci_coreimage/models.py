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
    AgentFeatures: Optional[Sequence["_AgentFeatures"]]
    BaseImageId: Optional[str]
    CompartmentId: Optional[str]
    CreateImageAllowed: Optional[bool]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    InstanceId: Optional[str]
    LaunchMode: Optional[str]
    LaunchOptions: Optional[Sequence["_LaunchOptions"]]
    OperatingSystem: Optional[str]
    OperatingSystemVersion: Optional[str]
    SizeInMbs: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    ImageSourceDetails: Optional[Sequence["_ImageSourceDetails"]]
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
            AgentFeatures=json_data.get("AgentFeatures"),
            BaseImageId=json_data.get("BaseImageId"),
            CompartmentId=json_data.get("CompartmentId"),
            CreateImageAllowed=json_data.get("CreateImageAllowed"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            LaunchMode=json_data.get("LaunchMode"),
            LaunchOptions=json_data.get("LaunchOptions"),
            OperatingSystem=json_data.get("OperatingSystem"),
            OperatingSystemVersion=json_data.get("OperatingSystemVersion"),
            SizeInMbs=json_data.get("SizeInMbs"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            ImageSourceDetails=json_data.get("ImageSourceDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AgentFeatures:
    IsManagementSupported: Optional[bool]
    IsMonitoringSupported: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AgentFeatures"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AgentFeatures"]:
        if not json_data:
            return None
        return cls(
            IsManagementSupported=json_data.get("IsManagementSupported"),
            IsMonitoringSupported=json_data.get("IsMonitoringSupported"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AgentFeatures = AgentFeatures


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
class LaunchOptions:
    BootVolumeType: Optional[str]
    Firmware: Optional[str]
    IsConsistentVolumeNamingEnabled: Optional[bool]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    NetworkType: Optional[str]
    RemoteDataVolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchOptions"]:
        if not json_data:
            return None
        return cls(
            BootVolumeType=json_data.get("BootVolumeType"),
            Firmware=json_data.get("Firmware"),
            IsConsistentVolumeNamingEnabled=json_data.get("IsConsistentVolumeNamingEnabled"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            NetworkType=json_data.get("NetworkType"),
            RemoteDataVolumeType=json_data.get("RemoteDataVolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchOptions = LaunchOptions


@dataclass
class ImageSourceDetails:
    BucketName: Optional[str]
    NamespaceName: Optional[str]
    ObjectName: Optional[str]
    OperatingSystem: Optional[str]
    OperatingSystemVersion: Optional[str]
    SourceImageType: Optional[str]
    SourceType: Optional[str]
    SourceUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageSourceDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageSourceDetails"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            NamespaceName=json_data.get("NamespaceName"),
            ObjectName=json_data.get("ObjectName"),
            OperatingSystem=json_data.get("OperatingSystem"),
            OperatingSystemVersion=json_data.get("OperatingSystemVersion"),
            SourceImageType=json_data.get("SourceImageType"),
            SourceType=json_data.get("SourceType"),
            SourceUri=json_data.get("SourceUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageSourceDetails = ImageSourceDetails


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


