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
    Endpoint: Optional[str]
    Id: Optional[str]
    Owner: Optional[str]
    Protocol: Optional[str]
    Remark: Optional[str]
    Status: Optional[float]
    SubscriptionUrn: Optional[str]
    TopicUrn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Owner=json_data.get("Owner"),
            Protocol=json_data.get("Protocol"),
            Remark=json_data.get("Remark"),
            Status=json_data.get("Status"),
            SubscriptionUrn=json_data.get("SubscriptionUrn"),
            TopicUrn=json_data.get("TopicUrn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


