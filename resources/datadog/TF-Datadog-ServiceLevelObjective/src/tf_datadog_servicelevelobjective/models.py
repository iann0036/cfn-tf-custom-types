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
    ForceDelete: Optional[bool]
    Groups: Optional[Sequence[str]]
    Id: Optional[str]
    MonitorIds: Optional[Sequence[float]]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    Validate: Optional[bool]
    Query: Optional[Sequence["_QueryDefinition"]]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

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
            ForceDelete=json_data.get("ForceDelete"),
            Groups=json_data.get("Groups"),
            Id=json_data.get("Id"),
            MonitorIds=json_data.get("MonitorIds"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Validate=json_data.get("Validate"),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class QueryDefinition(BaseModel):
    Denominator: Optional[str]
    Numerator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            Denominator=json_data.get("Denominator"),
            Numerator=json_data.get("Numerator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class ThresholdsDefinition(BaseModel):
    Target: Optional[float]
    TargetDisplay: Optional[str]
    Timeframe: Optional[str]
    Warning: Optional[float]
    WarningDisplay: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdsDefinition"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            TargetDisplay=json_data.get("TargetDisplay"),
            Timeframe=json_data.get("Timeframe"),
            Warning=json_data.get("Warning"),
            WarningDisplay=json_data.get("WarningDisplay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdsDefinition = ThresholdsDefinition


