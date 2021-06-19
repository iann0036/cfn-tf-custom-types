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
    DeadLetteringOnMessageExpiration: Optional[bool]
    DefaultMessageTtl: Optional[str]
    DuplicateDetectionHistoryTimeWindow: Optional[str]
    EnableBatchedOperations: Optional[bool]
    EnableExpress: Optional[bool]
    EnablePartitioning: Optional[bool]
    ForwardDeadLetteredMessagesTo: Optional[str]
    ForwardTo: Optional[str]
    Id: Optional[str]
    LockDuration: Optional[str]
    MaxDeliveryCount: Optional[float]
    MaxSizeInMegabytes: Optional[float]
    Name: Optional[str]
    NamespaceName: Optional[str]
    RequiresDuplicateDetection: Optional[bool]
    RequiresSession: Optional[bool]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
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
            DeadLetteringOnMessageExpiration=json_data.get("DeadLetteringOnMessageExpiration"),
            DefaultMessageTtl=json_data.get("DefaultMessageTtl"),
            DuplicateDetectionHistoryTimeWindow=json_data.get("DuplicateDetectionHistoryTimeWindow"),
            EnableBatchedOperations=json_data.get("EnableBatchedOperations"),
            EnableExpress=json_data.get("EnableExpress"),
            EnablePartitioning=json_data.get("EnablePartitioning"),
            ForwardDeadLetteredMessagesTo=json_data.get("ForwardDeadLetteredMessagesTo"),
            ForwardTo=json_data.get("ForwardTo"),
            Id=json_data.get("Id"),
            LockDuration=json_data.get("LockDuration"),
            MaxDeliveryCount=json_data.get("MaxDeliveryCount"),
            MaxSizeInMegabytes=json_data.get("MaxSizeInMegabytes"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            RequiresDuplicateDetection=json_data.get("RequiresDuplicateDetection"),
            RequiresSession=json_data.get("RequiresSession"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
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


