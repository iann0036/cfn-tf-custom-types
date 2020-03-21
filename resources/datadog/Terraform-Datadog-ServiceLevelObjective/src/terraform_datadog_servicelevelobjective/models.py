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
    Description: Optional[str]
    Groups: Optional[Sequence[str]]
    MonitorIds: Optional[Sequence[float]]
    MonitorSearch: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    Query: Optional[Sequence["_Query"]]
    Thresholds: Optional[Sequence["_Thresholds"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Groups=json_data.get("Groups"),
            MonitorIds=json_data.get("MonitorIds"),
            MonitorSearch=json_data.get("MonitorSearch"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Query=json_data.get("Query"),
            Thresholds=json_data.get("Thresholds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Query:
    Denominator: Optional[str]
    Numerator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Query"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Query"]:
        if not json_data:
            return None
        return cls(
            Denominator=json_data.get("Denominator"),
            Numerator=json_data.get("Numerator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Query = Query


@dataclass
class Thresholds:
    Target: Optional[float]
    TargetDisplay: Optional[str]
    Timeframe: Optional[str]
    Warning: Optional[float]
    WarningDisplay: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Thresholds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Thresholds"]:
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
_Thresholds = Thresholds


