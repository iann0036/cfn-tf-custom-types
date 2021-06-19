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
    ConferenceNumber: Optional[str]
    ConferenceUrl: Optional[str]
    Description: Optional[str]
    From: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RespondersMessage: Optional[str]
    Runnability: Optional[str]
    SubscribersMessage: Optional[str]
    Team: Optional[str]
    Type: Optional[str]
    Responder: Optional[Sequence["_ResponderDefinition"]]
    Subscriber: Optional[Sequence["_SubscriberDefinition"]]

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
            ConferenceNumber=json_data.get("ConferenceNumber"),
            ConferenceUrl=json_data.get("ConferenceUrl"),
            Description=json_data.get("Description"),
            From=json_data.get("From"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RespondersMessage=json_data.get("RespondersMessage"),
            Runnability=json_data.get("Runnability"),
            SubscribersMessage=json_data.get("SubscribersMessage"),
            Team=json_data.get("Team"),
            Type=json_data.get("Type"),
            Responder=deserialize_list(json_data.get("Responder"), ResponderDefinition),
            Subscriber=deserialize_list(json_data.get("Subscriber"), SubscriberDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResponderDefinition(BaseModel):
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponderDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponderDefinition = ResponderDefinition


@dataclass
class SubscriberDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubscriberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubscriberDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubscriberDefinition = SubscriberDefinition


