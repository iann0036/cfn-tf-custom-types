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
    DisplayName: Optional[str]
    GatewayPath: Optional[str]
    Id: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    Entry: Optional[Sequence["_EntryDefinition"]]
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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            GatewayPath=json_data.get("GatewayPath"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            Entry=deserialize_list(json_data.get("Entry"), EntryDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntryDefinition(BaseModel):
    Action: Optional[str]
    PrefixListMatches: Optional[Sequence[str]]
    CommunityListMatch: Optional[Sequence["_CommunityListMatchDefinition"]]
    Set: Optional[Sequence["_SetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            PrefixListMatches=json_data.get("PrefixListMatches"),
            CommunityListMatch=deserialize_list(json_data.get("CommunityListMatch"), CommunityListMatchDefinition),
            Set=deserialize_list(json_data.get("Set"), SetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntryDefinition = EntryDefinition


@dataclass
class CommunityListMatchDefinition(BaseModel):
    Criteria: Optional[str]
    MatchOperator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CommunityListMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommunityListMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Criteria=json_data.get("Criteria"),
            MatchOperator=json_data.get("MatchOperator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommunityListMatchDefinition = CommunityListMatchDefinition


@dataclass
class SetDefinition(BaseModel):
    AsPathPrepend: Optional[str]
    Community: Optional[str]
    LocalPreference: Optional[float]
    Med: Optional[float]
    PreferGlobalV6NextHop: Optional[bool]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetDefinition"]:
        if not json_data:
            return None
        return cls(
            AsPathPrepend=json_data.get("AsPathPrepend"),
            Community=json_data.get("Community"),
            LocalPreference=json_data.get("LocalPreference"),
            Med=json_data.get("Med"),
            PreferGlobalV6NextHop=json_data.get("PreferGlobalV6NextHop"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetDefinition = SetDefinition


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


