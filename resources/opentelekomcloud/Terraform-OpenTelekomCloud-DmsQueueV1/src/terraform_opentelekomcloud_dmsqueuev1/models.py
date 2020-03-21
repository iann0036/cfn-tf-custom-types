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
    Created: Optional[str]
    Description: Optional[str]
    GroupCount: Optional[float]
    MaxConsumeCount: Optional[float]
    MaxMsgSizeByte: Optional[float]
    Name: Optional[str]
    ProducedMessages: Optional[float]
    QueueMode: Optional[str]
    RedrivePolicy: Optional[str]
    Reservation: Optional[float]
    RetentionHours: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Created=json_data.get("Created"),
            Description=json_data.get("Description"),
            GroupCount=json_data.get("GroupCount"),
            MaxConsumeCount=json_data.get("MaxConsumeCount"),
            MaxMsgSizeByte=json_data.get("MaxMsgSizeByte"),
            Name=json_data.get("Name"),
            ProducedMessages=json_data.get("ProducedMessages"),
            QueueMode=json_data.get("QueueMode"),
            RedrivePolicy=json_data.get("RedrivePolicy"),
            Reservation=json_data.get("Reservation"),
            RetentionHours=json_data.get("RetentionHours"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


