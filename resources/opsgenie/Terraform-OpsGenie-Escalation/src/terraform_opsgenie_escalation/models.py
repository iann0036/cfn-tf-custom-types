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
    Name: Optional[str]
    OwnerTeamId: Optional[str]
    Repeat: Optional[Sequence["_Repeat"]]
    Rules: Optional[Sequence["_Rules"]]
    Recipient: Optional[Sequence["_Recipient"]]

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
            Name=json_data.get("Name"),
            OwnerTeamId=json_data.get("OwnerTeamId"),
            Repeat=json_data.get("Repeat"),
            Rules=json_data.get("Rules"),
            Recipient=json_data.get("Recipient"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Repeat:
    CloseAlertAfterAll: Optional[bool]
    Count: Optional[float]
    ResetRecipientStates: Optional[bool]
    WaitInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Repeat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Repeat"]:
        if not json_data:
            return None
        return cls(
            CloseAlertAfterAll=json_data.get("CloseAlertAfterAll"),
            Count=json_data.get("Count"),
            ResetRecipientStates=json_data.get("ResetRecipientStates"),
            WaitInterval=json_data.get("WaitInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Repeat = Repeat


@dataclass
class Rules:
    Condition: Optional[str]
    Delay: Optional[float]
    NotifyType: Optional[str]
    Recipient: Optional[Sequence["_Recipient"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Delay=json_data.get("Delay"),
            NotifyType=json_data.get("NotifyType"),
            Recipient=json_data.get("Recipient"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


@dataclass
class Recipient:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Recipient"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recipient"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recipient = Recipient


