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
    DataSourceId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Query: Optional[str]
    Tags: Optional[Sequence[str]]
    Parameter: Optional[Sequence["_ParameterDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

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
            DataSourceId=json_data.get("DataSourceId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
            Tags=json_data.get("Tags"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParameterDefinition(BaseModel):
    Name: Optional[str]
    Title: Optional[str]
    Date: Optional[Sequence["_DateDefinition"]]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]
    Datetime: Optional[Sequence["_DatetimeDefinition"]]
    DatetimeRange: Optional[Sequence["_DatetimeRangeDefinition"]]
    Datetimesec: Optional[Sequence["_DatetimesecDefinition"]]
    DatetimesecRange: Optional[Sequence["_DatetimesecRangeDefinition"]]
    Enum: Optional[Sequence["_EnumDefinition"]]
    Number: Optional[Sequence["_NumberDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]
    Text: Optional[Sequence["_TextDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Title=json_data.get("Title"),
            Date=deserialize_list(json_data.get("Date"), DateDefinition),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
            Datetime=deserialize_list(json_data.get("Datetime"), DatetimeDefinition),
            DatetimeRange=deserialize_list(json_data.get("DatetimeRange"), DatetimeRangeDefinition),
            Datetimesec=deserialize_list(json_data.get("Datetimesec"), DatetimesecDefinition),
            DatetimesecRange=deserialize_list(json_data.get("DatetimesecRange"), DatetimesecRangeDefinition),
            Enum=deserialize_list(json_data.get("Enum"), EnumDefinition),
            Number=deserialize_list(json_data.get("Number"), NumberDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            Text=deserialize_list(json_data.get("Text"), TextDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class DateDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateDefinition = DateDefinition


@dataclass
class DateRangeDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DateRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateRangeDefinition = DateRangeDefinition


@dataclass
class DatetimeDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatetimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatetimeDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatetimeDefinition = DatetimeDefinition


@dataclass
class DatetimeRangeDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatetimeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatetimeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatetimeRangeDefinition = DatetimeRangeDefinition


@dataclass
class DatetimesecDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatetimesecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatetimesecDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatetimesecDefinition = DatetimesecDefinition


@dataclass
class DatetimesecRangeDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatetimesecRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatetimesecRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatetimesecRangeDefinition = DatetimesecRangeDefinition


@dataclass
class EnumDefinition(BaseModel):
    Options: Optional[Sequence[str]]
    Value: Optional[str]
    Values: Optional[Sequence[str]]
    Multiple: Optional[Sequence["_MultipleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnumDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnumDefinition"]:
        if not json_data:
            return None
        return cls(
            Options=json_data.get("Options"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
            Multiple=deserialize_list(json_data.get("Multiple"), MultipleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnumDefinition = EnumDefinition


@dataclass
class MultipleDefinition(BaseModel):
    Prefix: Optional[str]
    Separator: Optional[str]
    Suffix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultipleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultipleDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Separator=json_data.get("Separator"),
            Suffix=json_data.get("Suffix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultipleDefinition = MultipleDefinition


@dataclass
class NumberDefinition(BaseModel):
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberDefinition = NumberDefinition


@dataclass
class QueryDefinition(BaseModel):
    QueryId: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence[str]]
    Multiple: Optional[Sequence["_MultipleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            QueryId=json_data.get("QueryId"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
            Multiple=deserialize_list(json_data.get("Multiple"), MultipleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class TextDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextDefinition = TextDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    Continuous: Optional[Sequence["_ContinuousDefinition"]]
    Daily: Optional[Sequence["_DailyDefinition"]]
    Weekly: Optional[Sequence["_WeeklyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Continuous=deserialize_list(json_data.get("Continuous"), ContinuousDefinition),
            Daily=deserialize_list(json_data.get("Daily"), DailyDefinition),
            Weekly=deserialize_list(json_data.get("Weekly"), WeeklyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class ContinuousDefinition(BaseModel):
    IntervalSeconds: Optional[float]
    UntilDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContinuousDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContinuousDefinition"]:
        if not json_data:
            return None
        return cls(
            IntervalSeconds=json_data.get("IntervalSeconds"),
            UntilDate=json_data.get("UntilDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContinuousDefinition = ContinuousDefinition


@dataclass
class DailyDefinition(BaseModel):
    IntervalDays: Optional[float]
    TimeOfDay: Optional[str]
    UntilDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DailyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyDefinition"]:
        if not json_data:
            return None
        return cls(
            IntervalDays=json_data.get("IntervalDays"),
            TimeOfDay=json_data.get("TimeOfDay"),
            UntilDate=json_data.get("UntilDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyDefinition = DailyDefinition


@dataclass
class WeeklyDefinition(BaseModel):
    DayOfWeek: Optional[str]
    IntervalWeeks: Optional[float]
    TimeOfDay: Optional[str]
    UntilDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            IntervalWeeks=json_data.get("IntervalWeeks"),
            TimeOfDay=json_data.get("TimeOfDay"),
            UntilDate=json_data.get("UntilDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyDefinition = WeeklyDefinition


