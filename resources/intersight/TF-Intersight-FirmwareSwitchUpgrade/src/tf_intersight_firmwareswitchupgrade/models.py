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
    AccountMoid: Optional[str]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    Device: Optional[Sequence["_DeviceDefinition"]]
    DirectDownload: Optional[Sequence["_DirectDownloadDefinition2"]]
    Distributable: Optional[Sequence["_DistributableDefinition"]]
    DomainGroupMoid: Optional[str]
    EnableFabricEvacuation: Optional[bool]
    FileServer: Optional[Sequence["_FileServerDefinition"]]
    Id: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    NetworkElements: Optional[Sequence["_NetworkElementsDefinition"]]
    NetworkShare: Optional[Sequence["_NetworkShareDefinition4"]]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Release: Optional[Sequence["_ReleaseDefinition"]]
    SharedScope: Optional[str]
    SkipEstimateImpact: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UpgradeImpact: Optional[Sequence["_UpgradeImpactDefinition"]]
    UpgradeStatus: Optional[Sequence["_UpgradeStatusDefinition"]]
    UpgradeType: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]

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
            AccountMoid=json_data.get("AccountMoid"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            Device=deserialize_list(json_data.get("Device"), DeviceDefinition),
            DirectDownload=deserialize_list(json_data.get("DirectDownload"), DirectDownloadDefinition2),
            Distributable=deserialize_list(json_data.get("Distributable"), DistributableDefinition),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            EnableFabricEvacuation=json_data.get("EnableFabricEvacuation"),
            FileServer=deserialize_list(json_data.get("FileServer"), FileServerDefinition),
            Id=json_data.get("Id"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            NetworkElements=deserialize_list(json_data.get("NetworkElements"), NetworkElementsDefinition),
            NetworkShare=deserialize_list(json_data.get("NetworkShare"), NetworkShareDefinition4),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Release=deserialize_list(json_data.get("Release"), ReleaseDefinition),
            SharedScope=json_data.get("SharedScope"),
            SkipEstimateImpact=json_data.get("SkipEstimateImpact"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UpgradeImpact=deserialize_list(json_data.get("UpgradeImpact"), UpgradeImpactDefinition),
            UpgradeStatus=deserialize_list(json_data.get("UpgradeStatus"), UpgradeStatusDefinition),
            UpgradeType=json_data.get("UpgradeType"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class DeviceDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceDefinition = DeviceDefinition


@dataclass
class DirectDownloadDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    HttpServer: Optional[Sequence["_DirectDownloadDefinition"]]
    ImageSource: Optional[str]
    IsPasswordSet: Optional[bool]
    ObjectType: Optional[str]
    Password: Optional[str]
    Upgradeoption: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DirectDownloadDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectDownloadDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            HttpServer=deserialize_list(json_data.get("HttpServer"), DirectDownloadDefinition),
            ImageSource=json_data.get("ImageSource"),
            IsPasswordSet=json_data.get("IsPasswordSet"),
            ObjectType=json_data.get("ObjectType"),
            Password=json_data.get("Password"),
            Upgradeoption=json_data.get("Upgradeoption"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectDownloadDefinition2 = DirectDownloadDefinition2


@dataclass
class DirectDownloadDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    LocationLink: Optional[str]
    MountOptions: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DirectDownloadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectDownloadDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            LocationLink=json_data.get("LocationLink"),
            MountOptions=json_data.get("MountOptions"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectDownloadDefinition = DirectDownloadDefinition


@dataclass
class DistributableDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributableDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributableDefinition = DistributableDefinition


@dataclass
class FileServerDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileServerDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileServerDefinition = FileServerDefinition


@dataclass
class NetworkElementsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkElementsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkElementsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkElementsDefinition = NetworkElementsDefinition


@dataclass
class NetworkShareDefinition4(BaseModel):
    AdditionalProperties: Optional[str]
    CifsServer: Optional[Sequence["_NetworkShareDefinition"]]
    ClassId: Optional[str]
    HttpServer: Optional[Sequence["_NetworkShareDefinition2"]]
    IsPasswordSet: Optional[bool]
    MapType: Optional[str]
    NfsServer: Optional[Sequence["_NetworkShareDefinition3"]]
    ObjectType: Optional[str]
    Password: Optional[str]
    Upgradeoption: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkShareDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkShareDefinition4"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            CifsServer=deserialize_list(json_data.get("CifsServer"), NetworkShareDefinition),
            ClassId=json_data.get("ClassId"),
            HttpServer=deserialize_list(json_data.get("HttpServer"), NetworkShareDefinition2),
            IsPasswordSet=json_data.get("IsPasswordSet"),
            MapType=json_data.get("MapType"),
            NfsServer=deserialize_list(json_data.get("NfsServer"), NetworkShareDefinition3),
            ObjectType=json_data.get("ObjectType"),
            Password=json_data.get("Password"),
            Upgradeoption=json_data.get("Upgradeoption"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkShareDefinition4 = NetworkShareDefinition4


@dataclass
class NetworkShareDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    FileLocation: Optional[str]
    MountOptions: Optional[str]
    ObjectType: Optional[str]
    RemoteFile: Optional[str]
    RemoteIp: Optional[str]
    RemoteShare: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkShareDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkShareDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            FileLocation=json_data.get("FileLocation"),
            MountOptions=json_data.get("MountOptions"),
            ObjectType=json_data.get("ObjectType"),
            RemoteFile=json_data.get("RemoteFile"),
            RemoteIp=json_data.get("RemoteIp"),
            RemoteShare=json_data.get("RemoteShare"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkShareDefinition = NetworkShareDefinition


@dataclass
class NetworkShareDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    LocationLink: Optional[str]
    MountOptions: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkShareDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkShareDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            LocationLink=json_data.get("LocationLink"),
            MountOptions=json_data.get("MountOptions"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkShareDefinition2 = NetworkShareDefinition2


@dataclass
class NetworkShareDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    FileLocation: Optional[str]
    MountOptions: Optional[str]
    ObjectType: Optional[str]
    RemoteFile: Optional[str]
    RemoteIp: Optional[str]
    RemoteShare: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkShareDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkShareDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            FileLocation=json_data.get("FileLocation"),
            MountOptions=json_data.get("MountOptions"),
            ObjectType=json_data.get("ObjectType"),
            RemoteFile=json_data.get("RemoteFile"),
            RemoteIp=json_data.get("RemoteIp"),
            RemoteShare=json_data.get("RemoteShare"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkShareDefinition3 = NetworkShareDefinition3


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class ReleaseDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReleaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReleaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReleaseDefinition = ReleaseDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class UpgradeImpactDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeImpactDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeImpactDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeImpactDefinition = UpgradeImpactDefinition


@dataclass
class UpgradeStatusDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeStatusDefinition = UpgradeStatusDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


