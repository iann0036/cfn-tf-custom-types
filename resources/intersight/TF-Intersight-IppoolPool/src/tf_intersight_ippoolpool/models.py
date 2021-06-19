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
    Assigned: Optional[float]
    AssignmentOrder: Optional[str]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    Id: Optional[str]
    IpV4Blocks: Optional[Sequence["_IpV4BlocksDefinition"]]
    IpV4Config: Optional[Sequence["_IpV4ConfigDefinition"]]
    IpV6Blocks: Optional[Sequence["_IpV6BlocksDefinition"]]
    IpV6Config: Optional[Sequence["_IpV6ConfigDefinition"]]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    ShadowPools: Optional[Sequence["_ShadowPoolsDefinition"]]
    SharedScope: Optional[str]
    Size: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    V4Assigned: Optional[float]
    V4Size: Optional[float]
    V6Assigned: Optional[float]
    V6Size: Optional[float]
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
            Assigned=json_data.get("Assigned"),
            AssignmentOrder=json_data.get("AssignmentOrder"),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            Id=json_data.get("Id"),
            IpV4Blocks=deserialize_list(json_data.get("IpV4Blocks"), IpV4BlocksDefinition),
            IpV4Config=deserialize_list(json_data.get("IpV4Config"), IpV4ConfigDefinition),
            IpV6Blocks=deserialize_list(json_data.get("IpV6Blocks"), IpV6BlocksDefinition),
            IpV6Config=deserialize_list(json_data.get("IpV6Config"), IpV6ConfigDefinition),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            ShadowPools=deserialize_list(json_data.get("ShadowPools"), ShadowPoolsDefinition),
            SharedScope=json_data.get("SharedScope"),
            Size=json_data.get("Size"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            V4Assigned=json_data.get("V4Assigned"),
            V4Size=json_data.get("V4Size"),
            V6Assigned=json_data.get("V6Assigned"),
            V6Size=json_data.get("V6Size"),
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
class IpV4BlocksDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    From: Optional[str]
    ObjectType: Optional[str]
    Size: Optional[float]
    To: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpV4BlocksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpV4BlocksDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            From=json_data.get("From"),
            ObjectType=json_data.get("ObjectType"),
            Size=json_data.get("Size"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpV4BlocksDefinition = IpV4BlocksDefinition


@dataclass
class IpV4ConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Gateway: Optional[str]
    Netmask: Optional[str]
    ObjectType: Optional[str]
    PrimaryDns: Optional[str]
    SecondaryDns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpV4ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpV4ConfigDefinition"]:
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
_IpV4ConfigDefinition = IpV4ConfigDefinition


@dataclass
class IpV6BlocksDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    From: Optional[str]
    ObjectType: Optional[str]
    Size: Optional[float]
    To: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpV6BlocksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpV6BlocksDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            From=json_data.get("From"),
            ObjectType=json_data.get("ObjectType"),
            Size=json_data.get("Size"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpV6BlocksDefinition = IpV6BlocksDefinition


@dataclass
class IpV6ConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Gateway: Optional[str]
    ObjectType: Optional[str]
    Prefix: Optional[float]
    PrimaryDns: Optional[str]
    SecondaryDns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpV6ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpV6ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Gateway=json_data.get("Gateway"),
            ObjectType=json_data.get("ObjectType"),
            Prefix=json_data.get("Prefix"),
            PrimaryDns=json_data.get("PrimaryDns"),
            SecondaryDns=json_data.get("SecondaryDns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpV6ConfigDefinition = IpV6ConfigDefinition


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
class ShadowPoolsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShadowPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShadowPoolsDefinition"]:
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
_ShadowPoolsDefinition = ShadowPoolsDefinition


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


