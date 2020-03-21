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
    AutoDeleteOnIdle: Optional[str]
    DeadLetteringOnMessageExpiration: Optional[bool]
    DefaultMessageTtl: Optional[str]
    EnableBatchedOperations: Optional[bool]
    ForwardDeadLetteredMessagesTo: Optional[str]
    ForwardTo: Optional[str]
    LockDuration: Optional[str]
    MaxDeliveryCount: Optional[float]
    Name: Optional[str]
    NamespaceName: Optional[str]
    RequiresSession: Optional[bool]
    ResourceGroupName: Optional[str]
    TopicName: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoDeleteOnIdle=json_data.get("AutoDeleteOnIdle"),
            DeadLetteringOnMessageExpiration=json_data.get("DeadLetteringOnMessageExpiration"),
            DefaultMessageTtl=json_data.get("DefaultMessageTtl"),
            EnableBatchedOperations=json_data.get("EnableBatchedOperations"),
            ForwardDeadLetteredMessagesTo=json_data.get("ForwardDeadLetteredMessagesTo"),
            ForwardTo=json_data.get("ForwardTo"),
            LockDuration=json_data.get("LockDuration"),
            MaxDeliveryCount=json_data.get("MaxDeliveryCount"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            RequiresSession=json_data.get("RequiresSession"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            TopicName=json_data.get("TopicName"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


