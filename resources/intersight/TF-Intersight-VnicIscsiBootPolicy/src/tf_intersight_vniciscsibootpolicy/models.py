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
    AutoTargetvendorName: Optional[str]
    Chap: Optional[Sequence["_ChapDefinition"]]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    Id: Optional[str]
    InitiatorIpPool: Optional[Sequence["_InitiatorIpPoolDefinition"]]
    InitiatorIpSource: Optional[str]
    InitiatorStaticIpV4Address: Optional[str]
    InitiatorStaticIpV4Config: Optional[Sequence["_InitiatorStaticIpV4ConfigDefinition"]]
    IscsiAdapterPolicy: Optional[Sequence["_IscsiAdapterPolicyDefinition"]]
    ModTime: Optional[str]
    Moid: Optional[str]
    MutualChap: Optional[Sequence["_MutualChapDefinition"]]
    Name: Optional[str]
    ObjectType: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    PrimaryTargetPolicy: Optional[Sequence["_PrimaryTargetPolicyDefinition"]]
    SecondaryTargetPolicy: Optional[Sequence["_SecondaryTargetPolicyDefinition"]]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TargetSourceType: Optional[str]
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
            AutoTargetvendorName=json_data.get("AutoTargetvendorName"),
            Chap=deserialize_list(json_data.get("Chap"), ChapDefinition),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            Id=json_data.get("Id"),
            InitiatorIpPool=deserialize_list(json_data.get("InitiatorIpPool"), InitiatorIpPoolDefinition),
            InitiatorIpSource=json_data.get("InitiatorIpSource"),
            InitiatorStaticIpV4Address=json_data.get("InitiatorStaticIpV4Address"),
            InitiatorStaticIpV4Config=deserialize_list(json_data.get("InitiatorStaticIpV4Config"), InitiatorStaticIpV4ConfigDefinition),
            IscsiAdapterPolicy=deserialize_list(json_data.get("IscsiAdapterPolicy"), IscsiAdapterPolicyDefinition),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            MutualChap=deserialize_list(json_data.get("MutualChap"), MutualChapDefinition),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            PrimaryTargetPolicy=deserialize_list(json_data.get("PrimaryTargetPolicy"), PrimaryTargetPolicyDefinition),
            SecondaryTargetPolicy=deserialize_list(json_data.get("SecondaryTargetPolicy"), SecondaryTargetPolicyDefinition),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TargetSourceType=json_data.get("TargetSourceType"),
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
class ChapDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsPasswordSet: Optional[bool]
    ObjectType: Optional[str]
    Password: Optional[str]
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChapDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsPasswordSet=json_data.get("IsPasswordSet"),
            ObjectType=json_data.get("ObjectType"),
            Password=json_data.get("Password"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChapDefinition = ChapDefinition


@dataclass
class InitiatorIpPoolDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitiatorIpPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitiatorIpPoolDefinition"]:
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
_InitiatorIpPoolDefinition = InitiatorIpPoolDefinition


@dataclass
class InitiatorStaticIpV4ConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Gateway: Optional[str]
    Netmask: Optional[str]
    ObjectType: Optional[str]
    PrimaryDns: Optional[str]
    SecondaryDns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitiatorStaticIpV4ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitiatorStaticIpV4ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Gateway=json_data.get("Gateway"),
            Netmask=json_data.get("Netmask"),
            ObjectType=json_data.get("ObjectType"),
            PrimaryDns=json_data.get("PrimaryDns"),
            SecondaryDns=json_data.get("SecondaryDns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitiatorStaticIpV4ConfigDefinition = InitiatorStaticIpV4ConfigDefinition


@dataclass
class IscsiAdapterPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IscsiAdapterPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IscsiAdapterPolicyDefinition"]:
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
_IscsiAdapterPolicyDefinition = IscsiAdapterPolicyDefinition


@dataclass
class MutualChapDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    IsPasswordSet: Optional[bool]
    ObjectType: Optional[str]
    Password: Optional[str]
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MutualChapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MutualChapDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            IsPasswordSet=json_data.get("IsPasswordSet"),
            ObjectType=json_data.get("ObjectType"),
            Password=json_data.get("Password"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MutualChapDefinition = MutualChapDefinition


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
class PrimaryTargetPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryTargetPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryTargetPolicyDefinition"]:
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
_PrimaryTargetPolicyDefinition = PrimaryTargetPolicyDefinition


@dataclass
class SecondaryTargetPolicyDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryTargetPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryTargetPolicyDefinition"]:
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
_SecondaryTargetPolicyDefinition = SecondaryTargetPolicyDefinition


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


