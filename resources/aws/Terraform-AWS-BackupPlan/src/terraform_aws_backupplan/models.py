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
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Lifecycle: Optional[Sequence["_Lifecycle"]]

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
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            Rule=json_data.get("Rule"),
            Lifecycle=json_data.get("Lifecycle"),
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
class Rule:
    CompletionWindow: Optional[float]
    RecoveryPointTags: Optional[Sequence["_RecoveryPointTags"]]
    RuleName: Optional[str]
    Schedule: Optional[str]
    StartWindow: Optional[float]
    TargetVaultName: Optional[str]
    Lifecycle: Optional[Sequence["_Lifecycle"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            CompletionWindow=json_data.get("CompletionWindow"),
            RecoveryPointTags=json_data.get("RecoveryPointTags"),
            RuleName=json_data.get("RuleName"),
            Schedule=json_data.get("Schedule"),
            StartWindow=json_data.get("StartWindow"),
            TargetVaultName=json_data.get("TargetVaultName"),
            Lifecycle=json_data.get("Lifecycle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class RecoveryPointTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryPointTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryPointTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryPointTags = RecoveryPointTags


@dataclass
class Lifecycle:
    ColdStorageAfter: Optional[float]
    DeleteAfter: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Lifecycle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lifecycle"]:
        if not json_data:
            return None
        return cls(
            ColdStorageAfter=json_data.get("ColdStorageAfter"),
            DeleteAfter=json_data.get("DeleteAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lifecycle = Lifecycle


