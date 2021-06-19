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
    Enabled: Optional[bool]
    Id: Optional[str]
    Message: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Case: Optional[Sequence["_CaseDefinition"]]
    Options: Optional[Sequence["_OptionsDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]

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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Case=deserialize_list(json_data.get("Case"), CaseDefinition),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CaseDefinition(BaseModel):
    Condition: Optional[str]
    Name: Optional[str]
    Notifications: Optional[Sequence[str]]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Name=json_data.get("Name"),
            Notifications=json_data.get("Notifications"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaseDefinition = CaseDefinition


@dataclass
class OptionsDefinition(BaseModel):
    EvaluationWindow: Optional[float]
    KeepAlive: Optional[float]
    MaxSignalDuration: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationWindow=json_data.get("EvaluationWindow"),
            KeepAlive=json_data.get("KeepAlive"),
            MaxSignalDuration=json_data.get("MaxSignalDuration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class QueryDefinition(BaseModel):
    Aggregation: Optional[str]
    DistinctFields: Optional[Sequence[str]]
    GroupByFields: Optional[Sequence[str]]
    Metric: Optional[str]
    Name: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            DistinctFields=json_data.get("DistinctFields"),
            GroupByFields=json_data.get("GroupByFields"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


