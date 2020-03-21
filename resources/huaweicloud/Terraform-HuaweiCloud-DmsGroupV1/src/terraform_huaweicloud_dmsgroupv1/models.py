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
    AvailableDeadletters: Optional[float]
    AvailableMessages: Optional[float]
    ConsumedMessages: Optional[float]
    Name: Optional[str]
    ProducedDeadletters: Optional[float]
    ProducedMessages: Optional[float]
    QueueId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailableDeadletters=json_data.get("AvailableDeadletters"),
            AvailableMessages=json_data.get("AvailableMessages"),
            ConsumedMessages=json_data.get("ConsumedMessages"),
            Name=json_data.get("Name"),
            ProducedDeadletters=json_data.get("ProducedDeadletters"),
            ProducedMessages=json_data.get("ProducedMessages"),
            QueueId=json_data.get("QueueId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


