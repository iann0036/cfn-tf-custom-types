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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    HealthCheckMonitorId: Optional[str]
    Id: Optional[str]
    Self: Optional[str]
    State: Optional[str]
    Template: Optional[str]
    TimeCreated: Optional[str]
    Ttl: Optional[float]
    Answers: Optional[Sequence["_Answers"]]
    Rules: Optional[Sequence["_Rules"]]
    Timeouts: Optional["_Timeouts"]
    Cases: Optional[Sequence["_Cases"]]
    DefaultAnswerData: Optional[Sequence["_DefaultAnswerData"]]
    AnswerData: Optional[Sequence["_AnswerData"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            HealthCheckMonitorId=json_data.get("HealthCheckMonitorId"),
            Id=json_data.get("Id"),
            Self=json_data.get("Self"),
            State=json_data.get("State"),
            Template=json_data.get("Template"),
            TimeCreated=json_data.get("TimeCreated"),
            Ttl=json_data.get("Ttl"),
            Answers=json_data.get("Answers"),
            Rules=json_data.get("Rules"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Cases=json_data.get("Cases"),
            DefaultAnswerData=json_data.get("DefaultAnswerData"),
            AnswerData=json_data.get("AnswerData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Answers:
    IsDisabled: Optional[bool]
    Name: Optional[str]
    Pool: Optional[str]
    Rdata: Optional[str]
    Rtype: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Answers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Answers"]:
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
_Answers = Answers


@dataclass
class Rules:
    DefaultCount: Optional[float]
    Description: Optional[str]
    RuleType: Optional[str]
    Cases: Optional[Sequence["_Cases"]]
    DefaultAnswerData: Optional[Sequence["_DefaultAnswerData"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            DefaultCount=json_data.get("DefaultCount"),
            Description=json_data.get("Description"),
            RuleType=json_data.get("RuleType"),
            Cases=json_data.get("Cases"),
            DefaultAnswerData=json_data.get("DefaultAnswerData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


@dataclass
class Cases:
    CaseCondition: Optional[str]
    Count: Optional[float]
    AnswerData: Optional[Sequence["_AnswerData"]]

    @classmethod
    def _deserialize(
        cls: Type["_Cases"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cases"]:
        if not json_data:
            return None
        return cls(
            CaseCondition=json_data.get("CaseCondition"),
            Count=json_data.get("Count"),
            AnswerData=json_data.get("AnswerData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cases = Cases


@dataclass
class AnswerData:
    AnswerCondition: Optional[str]
    ShouldKeep: Optional[bool]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AnswerData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswerData"]:
        if not json_data:
            return None
        return cls(
            AnswerCondition=json_data.get("AnswerCondition"),
            ShouldKeep=json_data.get("ShouldKeep"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswerData = AnswerData


@dataclass
class DefaultAnswerData:
    AnswerCondition: Optional[str]
    ShouldKeep: Optional[bool]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAnswerData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAnswerData"]:
        if not json_data:
            return None
        return cls(
            AnswerCondition=json_data.get("AnswerCondition"),
            ShouldKeep=json_data.get("ShouldKeep"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAnswerData = DefaultAnswerData


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


