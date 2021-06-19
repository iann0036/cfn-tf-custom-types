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
    Id: Optional[str]
    InsertBefore: Optional[str]
    IsDefault: Optional[bool]
    Revision: Optional[float]
    SectionType: Optional[str]
    Stateful: Optional[bool]
    AppliedTo: Optional[Sequence["_AppliedToDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]
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
            Id=json_data.get("Id"),
            InsertBefore=json_data.get("InsertBefore"),
            IsDefault=json_data.get("IsDefault"),
            Revision=json_data.get("Revision"),
            SectionType=json_data.get("SectionType"),
            Stateful=json_data.get("Stateful"),
            AppliedTo=deserialize_list(json_data.get("AppliedTo"), AppliedToDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppliedToDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppliedToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppliedToDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppliedToDefinition = AppliedToDefinition


@dataclass
class RuleDefinition(BaseModel):
    Action: Optional[str]
    Description: Optional[str]
    DestinationsExcluded: Optional[bool]
    Direction: Optional[str]
    Disabled: Optional[bool]
    DisplayName: Optional[str]
    IpProtocol: Optional[str]
    Logged: Optional[bool]
    Notes: Optional[str]
    RuleTag: Optional[str]
    SourcesExcluded: Optional[bool]
    AppliedTo: Optional[Sequence["_AppliedToDefinition"]]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DestinationsExcluded=json_data.get("DestinationsExcluded"),
            Direction=json_data.get("Direction"),
            Disabled=json_data.get("Disabled"),
            DisplayName=json_data.get("DisplayName"),
            IpProtocol=json_data.get("IpProtocol"),
            Logged=json_data.get("Logged"),
            Notes=json_data.get("Notes"),
            RuleTag=json_data.get("RuleTag"),
            SourcesExcluded=json_data.get("SourcesExcluded"),
            AppliedTo=deserialize_list(json_data.get("AppliedTo"), AppliedToDefinition),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class DestinationDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class ServiceDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class SourceDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


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


