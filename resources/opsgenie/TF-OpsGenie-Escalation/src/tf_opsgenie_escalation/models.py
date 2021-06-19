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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OwnerTeamId: Optional[str]
    Repeat: Optional[Sequence["_RepeatDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OwnerTeamId=json_data.get("OwnerTeamId"),
            Repeat=deserialize_list(json_data.get("Repeat"), RepeatDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RepeatDefinition(BaseModel):
    CloseAlertAfterAll: Optional[bool]
    Count: Optional[float]
    ResetRecipientStates: Optional[bool]
    WaitInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RepeatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepeatDefinition"]:
        if not json_data:
            return None
        return cls(
            CloseAlertAfterAll=json_data.get("CloseAlertAfterAll"),
            Count=json_data.get("Count"),
            ResetRecipientStates=json_data.get("ResetRecipientStates"),
            WaitInterval=json_data.get("WaitInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepeatDefinition = RepeatDefinition


@dataclass
class RulesDefinition(BaseModel):
    Condition: Optional[str]
    Delay: Optional[float]
    NotifyType: Optional[str]
    Recipient: Optional[Sequence["_RecipientDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Delay=json_data.get("Delay"),
            NotifyType=json_data.get("NotifyType"),
            Recipient=deserialize_list(json_data.get("Recipient"), RecipientDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class RecipientDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecipientDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecipientDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecipientDefinition = RecipientDefinition


