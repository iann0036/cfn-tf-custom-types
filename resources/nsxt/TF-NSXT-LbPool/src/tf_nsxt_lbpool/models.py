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
    Member: Optional[Sequence["_MemberDefinition"]]
    MemberGroup: Optional[Sequence["_MemberGroupDefinition"]]
    SnatTranslation: Optional[Sequence["_SnatTranslationDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            Member=deserialize_list(json_data.get("Member"), MemberDefinition),
            MemberGroup=deserialize_list(json_data.get("MemberGroup"), MemberGroupDefinition),
            SnatTranslation=deserialize_list(json_data.get("SnatTranslation"), SnatTranslationDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MemberDefinition(BaseModel):
    AdminState: Optional[str]
    BackupMember: Optional[bool]
    DisplayName: Optional[str]
    IpAddress: Optional[str]
    MaxConcurrentConnections: Optional[float]
    Port: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberDefinition"]:
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
_MemberDefinition = MemberDefinition


@dataclass
class MemberGroupDefinition(BaseModel):
    IpVersionFilter: Optional[str]
    LimitIpListSize: Optional[bool]
    MaxIpListSize: Optional[float]
    Port: Optional[float]
    GroupingObject: Optional[Sequence["_GroupingObjectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MemberGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            IpVersionFilter=json_data.get("IpVersionFilter"),
            LimitIpListSize=json_data.get("LimitIpListSize"),
            MaxIpListSize=json_data.get("MaxIpListSize"),
            Port=json_data.get("Port"),
            GroupingObject=deserialize_list(json_data.get("GroupingObject"), GroupingObjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberGroupDefinition = MemberGroupDefinition


@dataclass
class GroupingObjectDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupingObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupingObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupingObjectDefinition = GroupingObjectDefinition


@dataclass
class SnatTranslationDefinition(BaseModel):
    Ip: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnatTranslationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnatTranslationDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnatTranslationDefinition = SnatTranslationDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


