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
    Arn: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Schedule: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    WorkflowName: Optional[str]
    Actions: Optional[Sequence["_Actions"]]
    Predicate: Optional[Sequence["_Predicate"]]
    Timeouts: Optional["_Timeouts"]
    Conditions: Optional[Sequence["_Conditions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Schedule=json_data.get("Schedule"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            WorkflowName=json_data.get("WorkflowName"),
            Actions=json_data.get("Actions"),
            Predicate=json_data.get("Predicate"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Conditions=json_data.get("Conditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Actions:
    Arguments: Optional[Sequence["_Arguments"]]
    CrawlerName: Optional[str]
    JobName: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Actions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Actions"]:
        if not json_data:
            return None
        return cls(
            Arguments=json_data.get("Arguments"),
            CrawlerName=json_data.get("CrawlerName"),
            JobName=json_data.get("JobName"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Actions = Actions


@dataclass
class Arguments:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Arguments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Arguments"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Arguments = Arguments


@dataclass
class Predicate:
    Logical: Optional[str]
    Conditions: Optional[Sequence["_Conditions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Predicate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Predicate"]:
        if not json_data:
            return None
        return cls(
            Logical=json_data.get("Logical"),
            Conditions=json_data.get("Conditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Predicate = Predicate


@dataclass
class Conditions:
    CrawlState: Optional[str]
    CrawlerName: Optional[str]
    JobName: Optional[str]
    LogicalOperator: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            CrawlState=json_data.get("CrawlState"),
            CrawlerName=json_data.get("CrawlerName"),
            JobName=json_data.get("JobName"),
            LogicalOperator=json_data.get("LogicalOperator"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


