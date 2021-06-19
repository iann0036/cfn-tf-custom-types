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
    Arn: Optional[str]
    ConfirmationTimeoutInMinutes: Optional[float]
    ConfirmationWasAuthenticated: Optional[bool]
    DeliveryPolicy: Optional[str]
    Endpoint: Optional[str]
    EndpointAutoConfirms: Optional[bool]
    FilterPolicy: Optional[str]
    Id: Optional[str]
    OwnerId: Optional[str]
    PendingConfirmation: Optional[bool]
    Protocol: Optional[str]
    RawMessageDelivery: Optional[bool]
    RedrivePolicy: Optional[str]
    SubscriptionRoleArn: Optional[str]
    TopicArn: Optional[str]

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
            Arn=json_data.get("Arn"),
            ConfirmationTimeoutInMinutes=json_data.get("ConfirmationTimeoutInMinutes"),
            ConfirmationWasAuthenticated=json_data.get("ConfirmationWasAuthenticated"),
            DeliveryPolicy=json_data.get("DeliveryPolicy"),
            Endpoint=json_data.get("Endpoint"),
            EndpointAutoConfirms=json_data.get("EndpointAutoConfirms"),
            FilterPolicy=json_data.get("FilterPolicy"),
            Id=json_data.get("Id"),
            OwnerId=json_data.get("OwnerId"),
            PendingConfirmation=json_data.get("PendingConfirmation"),
            Protocol=json_data.get("Protocol"),
            RawMessageDelivery=json_data.get("RawMessageDelivery"),
            RedrivePolicy=json_data.get("RedrivePolicy"),
            SubscriptionRoleArn=json_data.get("SubscriptionRoleArn"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


