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
    ApplicationId: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    PromotionalMessagesPerSecond: Optional[float]
    SenderId: Optional[str]
    ShortCode: Optional[str]
    TransactionalMessagesPerSecond: Optional[float]

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
            ApplicationId=json_data.get("ApplicationId"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            PromotionalMessagesPerSecond=json_data.get("PromotionalMessagesPerSecond"),
            SenderId=json_data.get("SenderId"),
            ShortCode=json_data.get("ShortCode"),
            TransactionalMessagesPerSecond=json_data.get("TransactionalMessagesPerSecond"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


