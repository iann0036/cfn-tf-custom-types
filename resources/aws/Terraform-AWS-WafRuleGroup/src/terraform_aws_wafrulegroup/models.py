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
    Id: Optional[str]
    MetricName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ActivatedRule: Optional[Sequence["_ActivatedRule"]]
    Action: Optional[Sequence["_Action"]]

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
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            ActivatedRule=json_data.get("ActivatedRule"),
            Action=json_data.get("Action"),
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
class ActivatedRule:
    Priority: Optional[float]
    RuleId: Optional[str]
    Type: Optional[str]
    Action: Optional[Sequence["_Action"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActivatedRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActivatedRule"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            RuleId=json_data.get("RuleId"),
            Type=json_data.get("Type"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActivatedRule = ActivatedRule


@dataclass
class Action:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


