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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    HealthCheckMonitorId: Optional[str]
    Id: Optional[str]
    Self: Optional[str]
    State: Optional[str]
    Template: Optional[str]
    TimeCreated: Optional[str]
    Ttl: Optional[float]
    Answers: Optional[Sequence["_AnswersDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            HealthCheckMonitorId=json_data.get("HealthCheckMonitorId"),
            Id=json_data.get("Id"),
            Self=json_data.get("Self"),
            State=json_data.get("State"),
            Template=json_data.get("Template"),
            TimeCreated=json_data.get("TimeCreated"),
            Ttl=json_data.get("Ttl"),
            Answers=deserialize_list(json_data.get("Answers"), AnswersDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class AnswersDefinition(BaseModel):
    IsDisabled: Optional[bool]
    Name: Optional[str]
    Pool: Optional[str]
    Rdata: Optional[str]
    Rtype: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnswersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswersDefinition"]:
        if not json_data:
            return None
        return cls(
            IsDisabled=json_data.get("IsDisabled"),
            Name=json_data.get("Name"),
            Pool=json_data.get("Pool"),
            Rdata=json_data.get("Rdata"),
            Rtype=json_data.get("Rtype"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswersDefinition = AnswersDefinition


@dataclass
class RulesDefinition(BaseModel):
    DefaultCount: Optional[float]
    Description: Optional[str]
    RuleType: Optional[str]
    Cases: Optional[Sequence["_CasesDefinition"]]
    DefaultAnswerData: Optional[Sequence["_DefaultAnswerDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultCount=json_data.get("DefaultCount"),
            Description=json_data.get("Description"),
            RuleType=json_data.get("RuleType"),
            Cases=deserialize_list(json_data.get("Cases"), CasesDefinition),
            DefaultAnswerData=deserialize_list(json_data.get("DefaultAnswerData"), DefaultAnswerDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class CasesDefinition(BaseModel):
    CaseCondition: Optional[str]
    Count: Optional[float]
    AnswerData: Optional[Sequence["_AnswerDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CasesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CasesDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseCondition=json_data.get("CaseCondition"),
            Count=json_data.get("Count"),
            AnswerData=deserialize_list(json_data.get("AnswerData"), AnswerDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CasesDefinition = CasesDefinition


@dataclass
class AnswerDataDefinition(BaseModel):
    AnswerCondition: Optional[str]
    ShouldKeep: Optional[bool]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AnswerDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswerDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AnswerCondition=json_data.get("AnswerCondition"),
            ShouldKeep=json_data.get("ShouldKeep"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswerDataDefinition = AnswerDataDefinition


@dataclass
class DefaultAnswerDataDefinition(BaseModel):
    AnswerCondition: Optional[str]
    ShouldKeep: Optional[bool]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAnswerDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAnswerDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AnswerCondition=json_data.get("AnswerCondition"),
            ShouldKeep=json_data.get("ShouldKeep"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAnswerDataDefinition = DefaultAnswerDataDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


