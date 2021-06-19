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
    AdvancedFilter: Optional[bool]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    ArfsSettings: Optional[Sequence["_ArfsSettingsDefinition"]]
    ClassId: Optional[str]
    CompletionQueueSettings: Optional[Sequence["_CompletionQueueSettingsDefinition"]]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    Id: Optional[str]
    InterruptScaling: Optional[bool]
    InterruptSettings: Optional[Sequence["_InterruptSettingsDefinition"]]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NvgreSettings: Optional[Sequence["_NvgreSettingsDefinition"]]
    ObjectType: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    RoceSettings: Optional[Sequence["_RoceSettingsDefinition"]]
    RssHashSettings: Optional[Sequence["_RssHashSettingsDefinition"]]
    RssSettings: Optional[bool]
    RxQueueSettings: Optional[Sequence["_RxQueueSettingsDefinition"]]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TcpOffloadSettings: Optional[Sequence["_TcpOffloadSettingsDefinition"]]
    TxQueueSettings: Optional[Sequence["_TxQueueSettingsDefinition"]]
    UplinkFailbackTimeout: Optional[float]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    VxlanSettings: Optional[Sequence["_VxlanSettingsDefinition"]]

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
            AdvancedFilter=json_data.get("AdvancedFilter"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            ArfsSettings=deserialize_list(json_data.get("ArfsSettings"), ArfsSettingsDefinition),
            ClassId=json_data.get("ClassId"),
            CompletionQueueSettings=deserialize_list(json_data.get("CompletionQueueSettings"), CompletionQueueSettingsDefinition),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            Id=json_data.get("Id"),
            InterruptScaling=json_data.get("InterruptScaling"),
            InterruptSettings=deserialize_list(json_data.get("InterruptSettings"), InterruptSettingsDefinition),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NvgreSettings=deserialize_list(json_data.get("NvgreSettings"), NvgreSettingsDefinition),
            ObjectType=json_data.get("ObjectType"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            RoceSettings=deserialize_list(json_data.get("RoceSettings"), RoceSettingsDefinition),
            RssHashSettings=deserialize_list(json_data.get("RssHashSettings"), RssHashSettingsDefinition),
            RssSettings=json_data.get("RssSettings"),
            RxQueueSettings=deserialize_list(json_data.get("RxQueueSettings"), RxQueueSettingsDefinition),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TcpOffloadSettings=deserialize_list(json_data.get("TcpOffloadSettings"), TcpOffloadSettingsDefinition),
            TxQueueSettings=deserialize_list(json_data.get("TxQueueSettings"), TxQueueSettingsDefinition),
            UplinkFailbackTimeout=json_data.get("UplinkFailbackTimeout"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            VxlanSettings=deserialize_list(json_data.get("VxlanSettings"), VxlanSettingsDefinition),
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
class ArfsSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Enabled: Optional[bool]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArfsSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArfsSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Enabled=json_data.get("Enabled"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArfsSettingsDefinition = ArfsSettingsDefinition


@dataclass
class CompletionQueueSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    NrCount: Optional[float]
    ObjectType: Optional[str]
    RingSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CompletionQueueSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompletionQueueSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            NrCount=json_data.get("NrCount"),
            ObjectType=json_data.get("ObjectType"),
            RingSize=json_data.get("RingSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompletionQueueSettingsDefinition = CompletionQueueSettingsDefinition


@dataclass
class InterruptSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    CoalescingTime: Optional[float]
    CoalescingType: Optional[str]
    Mode: Optional[str]
    NrCount: Optional[float]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterruptSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterruptSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            CoalescingTime=json_data.get("CoalescingTime"),
            CoalescingType=json_data.get("CoalescingType"),
            Mode=json_data.get("Mode"),
            NrCount=json_data.get("NrCount"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterruptSettingsDefinition = InterruptSettingsDefinition


@dataclass
class NvgreSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Enabled: Optional[bool]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NvgreSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NvgreSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Enabled=json_data.get("Enabled"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NvgreSettingsDefinition = NvgreSettingsDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
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
_OrganizationDefinition = OrganizationDefinition


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
class RoceSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ClassOfService: Optional[float]
    Enabled: Optional[bool]
    MemoryRegions: Optional[float]
    NrVersion: Optional[float]
    ObjectType: Optional[str]
    QueuePairs: Optional[float]
    ResourceGroups: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RoceSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoceSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ClassOfService=json_data.get("ClassOfService"),
            Enabled=json_data.get("Enabled"),
            MemoryRegions=json_data.get("MemoryRegions"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            QueuePairs=json_data.get("QueuePairs"),
            ResourceGroups=json_data.get("ResourceGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoceSettingsDefinition = RoceSettingsDefinition


@dataclass
class RssHashSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Ipv4Hash: Optional[bool]
    Ipv6ExtHash: Optional[bool]
    Ipv6Hash: Optional[bool]
    ObjectType: Optional[str]
    TcpIpv4Hash: Optional[bool]
    TcpIpv6ExtHash: Optional[bool]
    TcpIpv6Hash: Optional[bool]
    UdpIpv4Hash: Optional[bool]
    UdpIpv6Hash: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RssHashSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RssHashSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Ipv4Hash=json_data.get("Ipv4Hash"),
            Ipv6ExtHash=json_data.get("Ipv6ExtHash"),
            Ipv6Hash=json_data.get("Ipv6Hash"),
            ObjectType=json_data.get("ObjectType"),
            TcpIpv4Hash=json_data.get("TcpIpv4Hash"),
            TcpIpv6ExtHash=json_data.get("TcpIpv6ExtHash"),
            TcpIpv6Hash=json_data.get("TcpIpv6Hash"),
            UdpIpv4Hash=json_data.get("UdpIpv4Hash"),
            UdpIpv6Hash=json_data.get("UdpIpv6Hash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RssHashSettingsDefinition = RssHashSettingsDefinition


@dataclass
class RxQueueSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    NrCount: Optional[float]
    ObjectType: Optional[str]
    RingSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RxQueueSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RxQueueSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            NrCount=json_data.get("NrCount"),
            ObjectType=json_data.get("ObjectType"),
            RingSize=json_data.get("RingSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RxQueueSettingsDefinition = RxQueueSettingsDefinition


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
class TcpOffloadSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    LargeReceive: Optional[bool]
    LargeSend: Optional[bool]
    ObjectType: Optional[str]
    RxChecksum: Optional[bool]
    TxChecksum: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TcpOffloadSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpOffloadSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            LargeReceive=json_data.get("LargeReceive"),
            LargeSend=json_data.get("LargeSend"),
            ObjectType=json_data.get("ObjectType"),
            RxChecksum=json_data.get("RxChecksum"),
            TxChecksum=json_data.get("TxChecksum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpOffloadSettingsDefinition = TcpOffloadSettingsDefinition


@dataclass
class TxQueueSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    NrCount: Optional[float]
    ObjectType: Optional[str]
    RingSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TxQueueSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxQueueSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            NrCount=json_data.get("NrCount"),
            ObjectType=json_data.get("ObjectType"),
            RingSize=json_data.get("RingSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxQueueSettingsDefinition = TxQueueSettingsDefinition


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


@dataclass
class VxlanSettingsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Enabled: Optional[bool]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VxlanSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VxlanSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Enabled=json_data.get("Enabled"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VxlanSettingsDefinition = VxlanSettingsDefinition


