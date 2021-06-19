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
    AutoDeleteOnIdle: Optional[str]
    DeadLetteringOnFilterEvaluationError: Optional[bool]
    DeadLetteringOnMessageExpiration: Optional[bool]
    DefaultMessageTtl: Optional[str]
    EnableBatchedOperations: Optional[bool]
    ForwardDeadLetteredMessagesTo: Optional[str]
    ForwardTo: Optional[str]
    Id: Optional[str]
    LockDuration: Optional[str]
    MaxDeliveryCount: Optional[float]
    Name: Optional[str]
    NamespaceName: Optional[str]
    RequiresSession: Optional[bool]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
    TopicName: Optional[str]
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
            AutoDeleteOnIdle=json_data.get("AutoDeleteOnIdle"),
            DeadLetteringOnFilterEvaluationError=json_data.get("DeadLetteringOnFilterEvaluationError"),
            DeadLetteringOnMessageExpiration=json_data.get("DeadLetteringOnMessageExpiration"),
            DefaultMessageTtl=json_data.get("DefaultMessageTtl"),
            EnableBatchedOperations=json_data.get("EnableBatchedOperations"),
            ForwardDeadLetteredMessagesTo=json_data.get("ForwardDeadLetteredMessagesTo"),
            ForwardTo=json_data.get("ForwardTo"),
            Id=json_data.get("Id"),
            LockDuration=json_data.get("LockDuration"),
            MaxDeliveryCount=json_data.get("MaxDeliveryCount"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            RequiresSession=json_data.get("RequiresSession"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
            TopicName=json_data.get("TopicName"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


