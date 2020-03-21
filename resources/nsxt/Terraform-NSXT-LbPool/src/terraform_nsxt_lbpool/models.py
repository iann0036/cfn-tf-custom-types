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
    ActiveMonitorId: Optional[str]
    Algorithm: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    MinActiveMembers: Optional[float]
    PassiveMonitorId: Optional[str]
    Revision: Optional[float]
    TcpMultiplexingEnabled: Optional[bool]
    TcpMultiplexingNumber: Optional[float]
    Member: Optional[Sequence["_Member"]]
    MemberGroup: Optional[Sequence["_MemberGroup"]]
    SnatTranslation: Optional[Sequence["_SnatTranslation"]]
    Tag: Optional[Sequence["_Tag"]]
    GroupingObject: Optional[Sequence["_GroupingObject"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActiveMonitorId=json_data.get("ActiveMonitorId"),
            Algorithm=json_data.get("Algorithm"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MinActiveMembers=json_data.get("MinActiveMembers"),
            PassiveMonitorId=json_data.get("PassiveMonitorId"),
            Revision=json_data.get("Revision"),
            TcpMultiplexingEnabled=json_data.get("TcpMultiplexingEnabled"),
            TcpMultiplexingNumber=json_data.get("TcpMultiplexingNumber"),
            Member=json_data.get("Member"),
            MemberGroup=json_data.get("MemberGroup"),
            SnatTranslation=json_data.get("SnatTranslation"),
            Tag=json_data.get("Tag"),
            GroupingObject=json_data.get("GroupingObject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Member:
    AdminState: Optional[str]
    BackupMember: Optional[bool]
    DisplayName: Optional[str]
    IpAddress: Optional[str]
    MaxConcurrentConnections: Optional[float]
    Port: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Member"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Member"]:
        if not json_data:
            return None
        return cls(
            AdminState=json_data.get("AdminState"),
            BackupMember=json_data.get("BackupMember"),
            DisplayName=json_data.get("DisplayName"),
            IpAddress=json_data.get("IpAddress"),
            MaxConcurrentConnections=json_data.get("MaxConcurrentConnections"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Member = Member


@dataclass
class MemberGroup:
    IpVersionFilter: Optional[str]
    LimitIpListSize: Optional[bool]
    MaxIpListSize: Optional[float]
    Port: Optional[float]
    GroupingObject: Optional[Sequence["_GroupingObject"]]

    @classmethod
    def _deserialize(
        cls: Type["_MemberGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberGroup"]:
        if not json_data:
            return None
        return cls(
            IpVersionFilter=json_data.get("IpVersionFilter"),
            LimitIpListSize=json_data.get("LimitIpListSize"),
            MaxIpListSize=json_data.get("MaxIpListSize"),
            Port=json_data.get("Port"),
            GroupingObject=json_data.get("GroupingObject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberGroup = MemberGroup


@dataclass
class GroupingObject:
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupingObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupingObject"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupingObject = GroupingObject


@dataclass
class SnatTranslation:
    Ip: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnatTranslation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatTranslation"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatTranslation = SnatTranslation


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


