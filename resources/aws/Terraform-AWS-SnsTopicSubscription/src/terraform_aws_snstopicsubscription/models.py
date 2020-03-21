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
    Arn: Optional[str]
    ConfirmationTimeoutInMinutes: Optional[float]
    DeliveryPolicy: Optional[str]
    Endpoint: Optional[str]
    EndpointAutoConfirms: Optional[bool]
    FilterPolicy: Optional[str]
    Protocol: Optional[str]
    RawMessageDelivery: Optional[bool]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            ConfirmationTimeoutInMinutes=json_data.get("ConfirmationTimeoutInMinutes"),
            DeliveryPolicy=json_data.get("DeliveryPolicy"),
            Endpoint=json_data.get("Endpoint"),
            EndpointAutoConfirms=json_data.get("EndpointAutoConfirms"),
            FilterPolicy=json_data.get("FilterPolicy"),
            Protocol=json_data.get("Protocol"),
            RawMessageDelivery=json_data.get("RawMessageDelivery"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


