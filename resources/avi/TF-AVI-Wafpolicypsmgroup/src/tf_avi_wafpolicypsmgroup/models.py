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
    Enable: Optional[bool]
    HitAction: Optional[str]
    Id: Optional[str]
    IsLearningGroup: Optional[bool]
    MissAction: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Locations: Optional[Sequence["_LocationsDefinition"]]
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
            Enable=json_data.get("Enable"),
            HitAction=json_data.get("HitAction"),
            Id=json_data.get("Id"),
            IsLearningGroup=json_data.get("IsLearningGroup"),
            MissAction=json_data.get("MissAction"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Locations=deserialize_list(json_data.get("Locations"), LocationsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LocationsDefinition(BaseModel):
    Description: Optional[str]
    Index: Optional[float]
    Name: Optional[str]
    Match: Optional[Sequence["_MatchDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LocationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationsDefinition = LocationsDefinition


@dataclass
class MatchDefinition(BaseModel):
    Host: Optional[Sequence["_HostDefinition"]]
    Methods: Optional[Sequence["_MethodsDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=deserialize_list(json_data.get("Host"), HostDefinition),
            Methods=deserialize_list(json_data.get("Methods"), MethodsDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class HostDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostDefinition = HostDefinition


@dataclass
class MethodsDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Methods: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MethodsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodsDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Methods=json_data.get("Methods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodsDefinition = MethodsDefinition


@dataclass
class PathDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class RulesDefinition(BaseModel):
    Description: Optional[str]
    Enable: Optional[bool]
    Index: Optional[float]
    MatchCase: Optional[str]
    MatchValueMaxLength: Optional[float]
    MatchValuePattern: Optional[str]
    MatchValueStringGroupKey: Optional[str]
    MatchValueStringGroupRef: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    ParanoiaLevel: Optional[str]
    RuleId: Optional[str]
    MatchElements: Optional[Sequence["_MatchElementsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            MatchCase=json_data.get("MatchCase"),
            MatchValueMaxLength=json_data.get("MatchValueMaxLength"),
            MatchValuePattern=json_data.get("MatchValuePattern"),
            MatchValueStringGroupKey=json_data.get("MatchValueStringGroupKey"),
            MatchValueStringGroupRef=json_data.get("MatchValueStringGroupRef"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            ParanoiaLevel=json_data.get("ParanoiaLevel"),
            RuleId=json_data.get("RuleId"),
            MatchElements=deserialize_list(json_data.get("MatchElements"), MatchElementsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class MatchElementsDefinition(BaseModel):
    Excluded: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    SubElement: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchElementsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchElementsDefinition"]:
        if not json_data:
            return None
        return cls(
            Excluded=json_data.get("Excluded"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            SubElement=json_data.get("SubElement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchElementsDefinition = MatchElementsDefinition


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


