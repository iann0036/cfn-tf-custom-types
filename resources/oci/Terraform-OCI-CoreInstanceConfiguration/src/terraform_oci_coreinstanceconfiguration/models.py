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
    CompartmentId: Optional[str]
    DeferredFields: Optional[Sequence[str]]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    InstanceId: Optional[str]
    Source: Optional[str]
    TimeCreated: Optional[str]
    InstanceDetails: Optional[Sequence["_InstanceDetails"]]
    Timeouts: Optional["_Timeouts"]
    BlockVolumes: Optional[Sequence["_BlockVolumes"]]
    LaunchDetails: Optional[Sequence["_LaunchDetails"]]
    SecondaryVnics: Optional[Sequence["_SecondaryVnics"]]
    AttachDetails: Optional[Sequence["_AttachDetails"]]
    CreateDetails: Optional[Sequence["_CreateDetails"]]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetails"]]
    SourceDetails: Optional[Sequence["_SourceDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DeferredFields=json_data.get("DeferredFields"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            Source=json_data.get("Source"),
            TimeCreated=json_data.get("TimeCreated"),
            InstanceDetails=json_data.get("InstanceDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            BlockVolumes=json_data.get("BlockVolumes"),
            LaunchDetails=json_data.get("LaunchDetails"),
            SecondaryVnics=json_data.get("SecondaryVnics"),
            AttachDetails=json_data.get("AttachDetails"),
            CreateDetails=json_data.get("CreateDetails"),
            CreateVnicDetails=json_data.get("CreateVnicDetails"),
            SourceDetails=json_data.get("SourceDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class InstanceDetails:
    InstanceType: Optional[str]
    BlockVolumes: Optional[Sequence["_BlockVolumes"]]
    LaunchDetails: Optional[Sequence["_LaunchDetails"]]
    SecondaryVnics: Optional[Sequence["_SecondaryVnics"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceDetails"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            BlockVolumes=json_data.get("BlockVolumes"),
            LaunchDetails=json_data.get("LaunchDetails"),
            SecondaryVnics=json_data.get("SecondaryVnics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceDetails = InstanceDetails


@dataclass
class BlockVolumes:
    VolumeId: Optional[str]
    AttachDetails: Optional[Sequence["_AttachDetails"]]
    CreateDetails: Optional[Sequence["_CreateDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockVolumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockVolumes"]:
        if not json_data:
            return None
        return cls(
            VolumeId=json_data.get("VolumeId"),
            AttachDetails=json_data.get("AttachDetails"),
            CreateDetails=json_data.get("CreateDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockVolumes = BlockVolumes


@dataclass
class AttachDetails:
    DisplayName: Optional[str]
    IsReadOnly: Optional[bool]
    Type: Optional[str]
    UseChap: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AttachDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachDetails"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            IsReadOnly=json_data.get("IsReadOnly"),
            Type=json_data.get("Type"),
            UseChap=json_data.get("UseChap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachDetails = AttachDetails


@dataclass
class CreateDetails:
    AvailabilityDomain: Optional[str]
    BackupPolicyId: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags2"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags2"]]
    SizeInGbs: Optional[str]
    SourceDetails: Optional[Sequence["_SourceDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_CreateDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateDetails"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupPolicyId=json_data.get("BackupPolicyId"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            SizeInGbs=json_data.get("SizeInGbs"),
            SourceDetails=json_data.get("SourceDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateDetails = CreateDetails


@dataclass
class DefinedTags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags2 = DefinedTags2


@dataclass
class FreeformTags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags2 = FreeformTags2


@dataclass
class SourceDetails:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetails"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetails = SourceDetails


@dataclass
class LaunchDetails:
    AvailabilityDomain: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags3"]]
    DisplayName: Optional[str]
    ExtendedMetadata: Optional[Sequence["_ExtendedMetadata"]]
    FaultDomain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags3"]]
    IpxeScript: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Shape: Optional[str]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetails"]]
    SourceDetails: Optional[Sequence["_SourceDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchDetails"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            ExtendedMetadata=json_data.get("ExtendedMetadata"),
            FaultDomain=json_data.get("FaultDomain"),
            FreeformTags=json_data.get("FreeformTags"),
            IpxeScript=json_data.get("IpxeScript"),
            Metadata=json_data.get("Metadata"),
            Shape=json_data.get("Shape"),
            CreateVnicDetails=json_data.get("CreateVnicDetails"),
            SourceDetails=json_data.get("SourceDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchDetails = LaunchDetails


@dataclass
class DefinedTags3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags3 = DefinedTags3


@dataclass
class ExtendedMetadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedMetadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedMetadata = ExtendedMetadata


@dataclass
class FreeformTags3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags3 = FreeformTags3


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
class CreateVnicDetails:
    AssignPublicIp: Optional[bool]
    DisplayName: Optional[str]
    HostnameLabel: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PrivateIp: Optional[str]
    SkipSourceDestCheck: Optional[bool]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreateVnicDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateVnicDetails"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            DisplayName=json_data.get("DisplayName"),
            HostnameLabel=json_data.get("HostnameLabel"),
            NsgIds=json_data.get("NsgIds"),
            PrivateIp=json_data.get("PrivateIp"),
            SkipSourceDestCheck=json_data.get("SkipSourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateVnicDetails = CreateVnicDetails


@dataclass
class SecondaryVnics:
    DisplayName: Optional[str]
    NicIndex: Optional[float]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryVnics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryVnics"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            NicIndex=json_data.get("NicIndex"),
            CreateVnicDetails=json_data.get("CreateVnicDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryVnics = SecondaryVnics


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


