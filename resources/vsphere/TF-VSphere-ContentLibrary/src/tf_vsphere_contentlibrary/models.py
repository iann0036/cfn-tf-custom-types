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
    StorageBacking: Optional[Sequence[str]]
    Publication: Optional[Sequence["_PublicationDefinition"]]
    Subscription: Optional[Sequence["_SubscriptionDefinition"]]

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
            StorageBacking=json_data.get("StorageBacking"),
            Publication=deserialize_list(json_data.get("Publication"), PublicationDefinition),
            Subscription=deserialize_list(json_data.get("Subscription"), SubscriptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PublicationDefinition(BaseModel):
    AuthenticationMethod: Optional[str]
    Password: Optional[str]
    Published: Optional[bool]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicationDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationMethod=json_data.get("AuthenticationMethod"),
            Password=json_data.get("Password"),
            Published=json_data.get("Published"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicationDefinition = PublicationDefinition


@dataclass
class SubscriptionDefinition(BaseModel):
    AuthenticationMethod: Optional[str]
    AutomaticSync: Optional[bool]
    OnDemand: Optional[bool]
    Password: Optional[str]
    SubscriptionUrl: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubscriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubscriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationMethod=json_data.get("AuthenticationMethod"),
            AutomaticSync=json_data.get("AutomaticSync"),
            OnDemand=json_data.get("OnDemand"),
            Password=json_data.get("Password"),
            SubscriptionUrl=json_data.get("SubscriptionUrl"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubscriptionDefinition = SubscriptionDefinition


