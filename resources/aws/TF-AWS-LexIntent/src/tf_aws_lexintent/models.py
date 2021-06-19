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
    CreateVersion: Optional[bool]
    CreatedDate: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    Name: Optional[str]
    ParentIntentSignature: Optional[str]
    SampleUtterances: Optional[Sequence[str]]
    Version: Optional[str]
    ConclusionStatement: Optional[Sequence["_ConclusionStatementDefinition"]]
    ConfirmationPrompt: Optional[Sequence["_ConfirmationPromptDefinition"]]
    DialogCodeHook: Optional[Sequence["_DialogCodeHookDefinition"]]
    FollowUpPrompt: Optional[Sequence["_FollowUpPromptDefinition"]]
    FulfillmentActivity: Optional[Sequence["_FulfillmentActivityDefinition"]]
    RejectionStatement: Optional[Sequence["_RejectionStatementDefinition"]]
    Slot: Optional[Sequence["_SlotDefinition"]]
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
            CreateVersion=json_data.get("CreateVersion"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            Name=json_data.get("Name"),
            ParentIntentSignature=json_data.get("ParentIntentSignature"),
            SampleUtterances=json_data.get("SampleUtterances"),
            Version=json_data.get("Version"),
            ConclusionStatement=deserialize_list(json_data.get("ConclusionStatement"), ConclusionStatementDefinition),
            ConfirmationPrompt=deserialize_list(json_data.get("ConfirmationPrompt"), ConfirmationPromptDefinition),
            DialogCodeHook=deserialize_list(json_data.get("DialogCodeHook"), DialogCodeHookDefinition),
            FollowUpPrompt=deserialize_list(json_data.get("FollowUpPrompt"), FollowUpPromptDefinition),
            FulfillmentActivity=deserialize_list(json_data.get("FulfillmentActivity"), FulfillmentActivityDefinition),
            RejectionStatement=deserialize_list(json_data.get("RejectionStatement"), RejectionStatementDefinition),
            Slot=deserialize_list(json_data.get("Slot"), SlotDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConclusionStatementDefinition(BaseModel):
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConclusionStatementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConclusionStatementDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConclusionStatementDefinition = ConclusionStatementDefinition


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
class ConfirmationPromptDefinition(BaseModel):
    MaxAttempts: Optional[float]
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfirmationPromptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfirmationPromptDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxAttempts=json_data.get("MaxAttempts"),
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfirmationPromptDefinition = ConfirmationPromptDefinition


@dataclass
class DialogCodeHookDefinition(BaseModel):
    MessageVersion: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DialogCodeHookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DialogCodeHookDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageVersion=json_data.get("MessageVersion"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DialogCodeHookDefinition = DialogCodeHookDefinition


@dataclass
class FollowUpPromptDefinition(BaseModel):
    Prompt: Optional[Sequence["_PromptDefinition"]]
    RejectionStatement: Optional[Sequence["_RejectionStatementDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FollowUpPromptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FollowUpPromptDefinition"]:
        if not json_data:
            return None
        return cls(
            Prompt=deserialize_list(json_data.get("Prompt"), PromptDefinition),
            RejectionStatement=deserialize_list(json_data.get("RejectionStatement"), RejectionStatementDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FollowUpPromptDefinition = FollowUpPromptDefinition


@dataclass
class PromptDefinition(BaseModel):
    MaxAttempts: Optional[float]
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PromptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PromptDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxAttempts=json_data.get("MaxAttempts"),
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PromptDefinition = PromptDefinition


@dataclass
class RejectionStatementDefinition(BaseModel):
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RejectionStatementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RejectionStatementDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RejectionStatementDefinition = RejectionStatementDefinition


@dataclass
class FulfillmentActivityDefinition(BaseModel):
    Type: Optional[str]
    CodeHook: Optional[Sequence["_CodeHookDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FulfillmentActivityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FulfillmentActivityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            CodeHook=deserialize_list(json_data.get("CodeHook"), CodeHookDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FulfillmentActivityDefinition = FulfillmentActivityDefinition


@dataclass
class CodeHookDefinition(BaseModel):
    MessageVersion: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CodeHookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeHookDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageVersion=json_data.get("MessageVersion"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeHookDefinition = CodeHookDefinition


@dataclass
class SlotDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ResponseCard: Optional[str]
    SampleUtterances: Optional[Sequence[str]]
    SlotConstraint: Optional[str]
    SlotType: Optional[str]
    SlotTypeVersion: Optional[str]
    ValueElicitationPrompt: Optional[Sequence["_ValueElicitationPromptDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SlotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ResponseCard=json_data.get("ResponseCard"),
            SampleUtterances=json_data.get("SampleUtterances"),
            SlotConstraint=json_data.get("SlotConstraint"),
            SlotType=json_data.get("SlotType"),
            SlotTypeVersion=json_data.get("SlotTypeVersion"),
            ValueElicitationPrompt=deserialize_list(json_data.get("ValueElicitationPrompt"), ValueElicitationPromptDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotDefinition = SlotDefinition


@dataclass
class ValueElicitationPromptDefinition(BaseModel):
    MaxAttempts: Optional[float]
    ResponseCard: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueElicitationPromptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueElicitationPromptDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxAttempts=json_data.get("MaxAttempts"),
            ResponseCard=json_data.get("ResponseCard"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueElicitationPromptDefinition = ValueElicitationPromptDefinition


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


