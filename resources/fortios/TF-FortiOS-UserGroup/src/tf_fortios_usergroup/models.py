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
    AuthConcurrentOverride: Optional[str]
    AuthConcurrentValue: Optional[float]
    Authtimeout: Optional[float]
    Company: Optional[str]
    DynamicSortSubtable: Optional[str]
    Email: Optional[str]
    Expire: Optional[float]
    ExpireType: Optional[str]
    Fosid: Optional[float]
    GroupType: Optional[str]
    HttpDigestRealm: Optional[str]
    Id: Optional[str]
    MaxAccounts: Optional[float]
    MobilePhone: Optional[str]
    MultipleGuestAdd: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    SmsCustomServer: Optional[str]
    SmsServer: Optional[str]
    Sponsor: Optional[str]
    SsoAttributeValue: Optional[str]
    UserId: Optional[str]
    UserName: Optional[str]
    Vdomparam: Optional[str]
    Guest: Optional[Sequence["_GuestDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]
    Member: Optional[Sequence["_MemberDefinition"]]

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
            AuthConcurrentOverride=json_data.get("AuthConcurrentOverride"),
            AuthConcurrentValue=json_data.get("AuthConcurrentValue"),
            Authtimeout=json_data.get("Authtimeout"),
            Company=json_data.get("Company"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Email=json_data.get("Email"),
            Expire=json_data.get("Expire"),
            ExpireType=json_data.get("ExpireType"),
            Fosid=json_data.get("Fosid"),
            GroupType=json_data.get("GroupType"),
            HttpDigestRealm=json_data.get("HttpDigestRealm"),
            Id=json_data.get("Id"),
            MaxAccounts=json_data.get("MaxAccounts"),
            MobilePhone=json_data.get("MobilePhone"),
            MultipleGuestAdd=json_data.get("MultipleGuestAdd"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            SmsCustomServer=json_data.get("SmsCustomServer"),
            SmsServer=json_data.get("SmsServer"),
            Sponsor=json_data.get("Sponsor"),
            SsoAttributeValue=json_data.get("SsoAttributeValue"),
            UserId=json_data.get("UserId"),
            UserName=json_data.get("UserName"),
            Vdomparam=json_data.get("Vdomparam"),
            Guest=deserialize_list(json_data.get("Guest"), GuestDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            Member=deserialize_list(json_data.get("Member"), MemberDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuestDefinition(BaseModel):
    Comment: Optional[str]
    Company: Optional[str]
    Email: Optional[str]
    Expiration: Optional[str]
    Id: Optional[float]
    MobilePhone: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Sponsor: Optional[str]
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Company=json_data.get("Company"),
            Email=json_data.get("Email"),
            Expiration=json_data.get("Expiration"),
            Id=json_data.get("Id"),
            MobilePhone=json_data.get("MobilePhone"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Sponsor=json_data.get("Sponsor"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestDefinition = GuestDefinition


@dataclass
class MatchDefinition(BaseModel):
    GroupName: Optional[str]
    Id: Optional[float]
    ServerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Id=json_data.get("Id"),
            ServerName=json_data.get("ServerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class MemberDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberDefinition = MemberDefinition


