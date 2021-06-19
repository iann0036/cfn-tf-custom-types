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
    Actions: Optional[Sequence[str]]
    AlertDescription: Optional[str]
    Alias: Optional[str]
    ContinuePolicy: Optional[bool]
    Enabled: Optional[bool]
    Entity: Optional[str]
    Id: Optional[str]
    IgnoreOriginalActions: Optional[bool]
    IgnoreOriginalDetails: Optional[bool]
    IgnoreOriginalResponders: Optional[bool]
    IgnoreOriginalTags: Optional[bool]
    Message: Optional[str]
    Name: Optional[str]
    PolicyDescription: Optional[str]
    Priority: Optional[str]
    Source: Optional[str]
    Tags: Optional[Sequence[str]]
    TeamId: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Responders: Optional[Sequence["_RespondersDefinition"]]
    TimeRestriction: Optional[Sequence["_TimeRestrictionDefinition"]]

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
            Actions=json_data.get("Actions"),
            AlertDescription=json_data.get("AlertDescription"),
            Alias=json_data.get("Alias"),
            ContinuePolicy=json_data.get("ContinuePolicy"),
            Enabled=json_data.get("Enabled"),
            Entity=json_data.get("Entity"),
            Id=json_data.get("Id"),
            IgnoreOriginalActions=json_data.get("IgnoreOriginalActions"),
            IgnoreOriginalDetails=json_data.get("IgnoreOriginalDetails"),
            IgnoreOriginalResponders=json_data.get("IgnoreOriginalResponders"),
            IgnoreOriginalTags=json_data.get("IgnoreOriginalTags"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            PolicyDescription=json_data.get("PolicyDescription"),
            Priority=json_data.get("Priority"),
            Source=json_data.get("Source"),
            Tags=json_data.get("Tags"),
            TeamId=json_data.get("TeamId"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Responders=deserialize_list(json_data.get("Responders"), RespondersDefinition),
            TimeRestriction=deserialize_list(json_data.get("TimeRestriction"), TimeRestrictionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Type: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    ExpectedValue: Optional[str]
    Field: Optional[str]
    Key: Optional[str]
    Not: Optional[bool]
    Operation: Optional[str]
    Order: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedValue=json_data.get("ExpectedValue"),
            Field=json_data.get("Field"),
            Key=json_data.get("Key"),
            Not=json_data.get("Not"),
            Operation=json_data.get("Operation"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class RespondersDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RespondersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RespondersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RespondersDefinition = RespondersDefinition


@dataclass
class TimeRestrictionDefinition(BaseModel):
    Type: Optional[str]
    Restriction: Optional[Sequence["_RestrictionDefinition"]]
    Restrictions: Optional[Sequence["_RestrictionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Restriction=deserialize_list(json_data.get("Restriction"), RestrictionDefinition),
            Restrictions=deserialize_list(json_data.get("Restrictions"), RestrictionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRestrictionDefinition = TimeRestrictionDefinition


@dataclass
class RestrictionDefinition(BaseModel):
    EndHour: Optional[float]
    EndMin: Optional[float]
    StartHour: Optional[float]
    StartMin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            EndHour=json_data.get("EndHour"),
            EndMin=json_data.get("EndMin"),
            StartHour=json_data.get("StartHour"),
            StartMin=json_data.get("StartMin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionDefinition = RestrictionDefinition


@dataclass
class RestrictionsDefinition(BaseModel):
    EndDay: Optional[str]
    EndHour: Optional[float]
    EndMin: Optional[float]
    StartDay: Optional[str]
    StartHour: Optional[float]
    StartMin: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndDay=json_data.get("EndDay"),
            EndHour=json_data.get("EndHour"),
            EndMin=json_data.get("EndMin"),
            StartDay=json_data.get("StartDay"),
            StartHour=json_data.get("StartHour"),
            StartMin=json_data.get("StartMin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionsDefinition = RestrictionsDefinition


