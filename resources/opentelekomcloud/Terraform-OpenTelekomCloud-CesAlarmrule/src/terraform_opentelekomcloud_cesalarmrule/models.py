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
    AlarmActionEnabled: Optional[bool]
    AlarmDescription: Optional[str]
    AlarmEnabled: Optional[bool]
    AlarmName: Optional[str]
    AlarmState: Optional[str]
    Id: Optional[str]
    UpdateTime: Optional[float]
    AlarmActions: Optional[Sequence["_AlarmActions"]]
    Condition: Optional[Sequence["_Condition"]]
    InsufficientdataActions: Optional[Sequence["_InsufficientdataActions"]]
    Metric: Optional[Sequence["_Metric"]]
    OkActions: Optional[Sequence["_OkActions"]]
    Timeouts: Optional["_Timeouts"]
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlarmActionEnabled=json_data.get("AlarmActionEnabled"),
            AlarmDescription=json_data.get("AlarmDescription"),
            AlarmEnabled=json_data.get("AlarmEnabled"),
            AlarmName=json_data.get("AlarmName"),
            AlarmState=json_data.get("AlarmState"),
            Id=json_data.get("Id"),
            UpdateTime=json_data.get("UpdateTime"),
            AlarmActions=json_data.get("AlarmActions"),
            Condition=json_data.get("Condition"),
            InsufficientdataActions=json_data.get("InsufficientdataActions"),
            Metric=json_data.get("Metric"),
            OkActions=json_data.get("OkActions"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlarmActions:
    NotificationList: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmActions"]:
        if not json_data:
            return None
        return cls(
            NotificationList=json_data.get("NotificationList"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmActions = AlarmActions


@dataclass
class Condition:
    ComparisonOperator: Optional[str]
    Count: Optional[float]
    Filter: Optional[str]
    Period: Optional[float]
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Count=json_data.get("Count"),
            Filter=json_data.get("Filter"),
            Period=json_data.get("Period"),
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class InsufficientdataActions:
    NotificationList: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InsufficientdataActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsufficientdataActions"]:
        if not json_data:
            return None
        return cls(
            NotificationList=json_data.get("NotificationList"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsufficientdataActions = InsufficientdataActions


@dataclass
class Metric:
    MetricName: Optional[str]
    Namespace: Optional[str]
    Dimensions: Optional[Sequence["_Dimensions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            Dimensions=json_data.get("Dimensions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class Dimensions:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions = Dimensions


@dataclass
class OkActions:
    NotificationList: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OkActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OkActions"]:
        if not json_data:
            return None
        return cls(
            NotificationList=json_data.get("NotificationList"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OkActions = OkActions


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


