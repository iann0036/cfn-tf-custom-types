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
    Comparison: Optional[str]
    CreatedAt: Optional[float]
    Enabled: Optional[bool]
    Event: Optional[str]
    IntegrationProvider: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[float]
    ProcessWhere: Optional[str]
    RunbookUrl: Optional[str]
    Select: Optional[str]
    Type: Optional[str]
    UpdatedAt: Optional[float]
    ViolationCloseTimer: Optional[float]
    Where: Optional[str]
    Critical: Optional[Sequence["_Critical"]]
    Warning: Optional[Sequence["_Warning"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Comparison=json_data.get("Comparison"),
            CreatedAt=json_data.get("CreatedAt"),
            Enabled=json_data.get("Enabled"),
            Event=json_data.get("Event"),
            IntegrationProvider=json_data.get("IntegrationProvider"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            ProcessWhere=json_data.get("ProcessWhere"),
            RunbookUrl=json_data.get("RunbookUrl"),
            Select=json_data.get("Select"),
            Type=json_data.get("Type"),
            UpdatedAt=json_data.get("UpdatedAt"),
            ViolationCloseTimer=json_data.get("ViolationCloseTimer"),
            Where=json_data.get("Where"),
            Critical=json_data.get("Critical"),
            Warning=json_data.get("Warning"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Critical:
    Duration: Optional[float]
    TimeFunction: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Critical"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Critical"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            TimeFunction=json_data.get("TimeFunction"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Critical = Critical


@dataclass
class Warning:
    Duration: Optional[float]
    TimeFunction: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Warning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Warning"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            TimeFunction=json_data.get("TimeFunction"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Warning = Warning


