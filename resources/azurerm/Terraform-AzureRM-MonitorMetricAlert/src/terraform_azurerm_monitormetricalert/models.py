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
    AutoMitigate: Optional[bool]
    Description: Optional[str]
    Enabled: Optional[bool]
    Frequency: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Scopes: Optional[Sequence[str]]
    Severity: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    WindowSize: Optional[str]
    Action: Optional[Sequence["_Action"]]
    Criteria: Optional[Sequence["_Criteria"]]
    Timeouts: Optional["_Timeouts"]
    Dimension: Optional[Sequence["_Dimension"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoMitigate=json_data.get("AutoMitigate"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Scopes=json_data.get("Scopes"),
            Severity=json_data.get("Severity"),
            Tags=json_data.get("Tags"),
            WindowSize=json_data.get("WindowSize"),
            Action=json_data.get("Action"),
            Criteria=json_data.get("Criteria"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Dimension=json_data.get("Dimension"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Action:
    ActionGroupId: Optional[str]
    WebhookProperties: Optional[Sequence["_WebhookProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            ActionGroupId=json_data.get("ActionGroupId"),
            WebhookProperties=json_data.get("WebhookProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class WebhookProperties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookProperties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookProperties = WebhookProperties


@dataclass
class Criteria:
    Aggregation: Optional[str]
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    Operator: Optional[str]
    Threshold: Optional[float]
    Dimension: Optional[Sequence["_Dimension"]]

    @classmethod
    def _deserialize(
        cls: Type["_Criteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Criteria"]:
        if not json_data:
            return None
        return cls(
            Aggregation=json_data.get("Aggregation"),
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
            Dimension=json_data.get("Dimension"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Criteria = Criteria


@dataclass
class Dimension:
    Name: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Dimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimension"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimension = Dimension


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


