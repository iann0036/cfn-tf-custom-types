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
    Arn: Optional[str]
    Checksum: Optional[str]
    ChildDirected: Optional[bool]
    CreateVersion: Optional[bool]
    CreatedDate: Optional[str]
    Description: Optional[str]
    DetectSentiment: Optional[bool]
    EnableModelImprovements: Optional[bool]
    FailureReason: Optional[str]
    Id: Optional[str]
    IdleSessionTtlInSeconds: Optional[float]
    LastUpdatedDate: Optional[str]
    Locale: Optional[str]
    Name: Optional[str]
    NluIntentConfidenceThreshold: Optional[float]
    ProcessBehavior: Optional[str]
    Status: Optional[str]
    Version: Optional[str]
    VoiceId: Optional[str]
    AbortStatement: Optional[Sequence["_AbortStatementDefinition"]]
    ClarificationPrompt: Optional[Sequence["_ClarificationPromptDefinition"]]
    Intent: Optional[Sequence["_IntentDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Arn=json_data.get("Arn"),
            Checksum=json_data.get("Checksum"),
            ChildDirected=json_data.get("ChildDirected"),
            CreateVersion=json_data.get("CreateVersion"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            DetectSentiment=json_data.get("DetectSentiment"),
            EnableModelImprovements=json_data.get("EnableModelImprovements"),
            FailureReason=json_data.get("FailureReason"),
            Id=json_data.get("Id"),
            IdleSessionTtlInSeconds=json_data.get("IdleSessionTtlInSeconds"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            Locale=json_data.get("Locale"),
            Name=json_data.get("Name"),
            NluIntentConfidenceThreshold=json_data.get("NluIntentConfidenceThreshold"),
            ProcessBehavior=json_data.get("ProcessBehavior"),
            Status=json_data.get("Status"),
            Version=json_data.get("Version"),
            VoiceId=json_data.get("VoiceId"),
            AbortStatement=deserialize_list(json_data.get("AbortStatement"), AbortStatementDefinition),
            ClarificationPrompt=deserialize_list(json_data.get("ClarificationPrompt"), ClarificationPromptDefinition),
            Intent=deserialize_list(json_data.get("Intent"), IntentDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AbortStatementDefinition(BaseModel):
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AbortStatementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortStatementDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortStatementDefinition = AbortStatementDefinition


@dataclass
class MessageDefinition(BaseModel):
    Content: Optional[str]
    ContentType: Optional[str]
    GroupNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MessageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            ContentType=json_data.get("ContentType"),
            GroupNumber=json_data.get("GroupNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageDefinition = MessageDefinition


@dataclass
class ClarificationPromptDefinition(BaseModel):
    MaxAttempts: Optional[float]
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClarificationPromptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClarificationPromptDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxAttempts=json_data.get("MaxAttempts"),
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClarificationPromptDefinition = ClarificationPromptDefinition


@dataclass
class IntentDefinition(BaseModel):
    IntentName: Optional[str]
    IntentVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntentDefinition"]:
        if not json_data:
            return None
        return cls(
            IntentName=json_data.get("IntentName"),
            IntentVersion=json_data.get("IntentVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntentDefinition = IntentDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


