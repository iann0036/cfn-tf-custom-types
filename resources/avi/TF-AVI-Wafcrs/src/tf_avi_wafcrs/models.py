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
    Description: Optional[str]
    Id: Optional[str]
    Integrity: Optional[str]
    Name: Optional[str]
    ReleaseDate: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Version: Optional[str]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Integrity=json_data.get("Integrity"),
            Name=json_data.get("Name"),
            ReleaseDate=json_data.get("ReleaseDate"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GroupsDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupsDefinition = GroupsDefinition


@dataclass
class ExcludeListDefinition(BaseModel):
    Description: Optional[str]
    MatchElement: Optional[str]
    UriPath: Optional[str]
    ClientSubnet: Optional[Sequence["_ClientSubnetDefinition"]]
    MatchElementCriteria: Optional[Sequence["_MatchElementCriteriaDefinition"]]
    UriMatchCriteria: Optional[Sequence["_UriMatchCriteriaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeListDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            MatchElement=json_data.get("MatchElement"),
            UriPath=json_data.get("UriPath"),
            ClientSubnet=deserialize_list(json_data.get("ClientSubnet"), ClientSubnetDefinition),
            MatchElementCriteria=deserialize_list(json_data.get("MatchElementCriteria"), MatchElementCriteriaDefinition),
            UriMatchCriteria=deserialize_list(json_data.get("UriMatchCriteria"), UriMatchCriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeListDefinition = ExcludeListDefinition


@dataclass
class ClientSubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSubnetDefinition = ClientSubnetDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class MatchElementCriteriaDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchOp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchElementCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchElementCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchOp=json_data.get("MatchOp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchElementCriteriaDefinition = MatchElementCriteriaDefinition


@dataclass
class UriMatchCriteriaDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchOp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UriMatchCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriMatchCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchOp=json_data.get("MatchOp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriMatchCriteriaDefinition = UriMatchCriteriaDefinition


@dataclass
class RulesDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    IsSensitive: Optional[bool]
    Mode: Optional[str]
    Name: Optional[str]
    Rule: Optional[str]
    RuleId: Optional[str]
    Tags: Optional[Sequence[str]]
    ExcludeList: Optional[Sequence["_ExcludeListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            IsSensitive=json_data.get("IsSensitive"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Rule=json_data.get("Rule"),
            RuleId=json_data.get("RuleId"),
            Tags=json_data.get("Tags"),
            ExcludeList=deserialize_list(json_data.get("ExcludeList"), ExcludeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


