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
    CloseWaitTimeout: Optional[float]
    DefaultsFrom: Optional[str]
    DeferredAccept: Optional[str]
    FastOpen: Optional[str]
    Finwait2timeout: Optional[float]
    FinwaitTimeout: Optional[float]
    IdleTimeout: Optional[float]
    KeepaliveInterval: Optional[float]
    Name: Optional[str]
    Partition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CloseWaitTimeout=json_data.get("CloseWaitTimeout"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            DeferredAccept=json_data.get("DeferredAccept"),
            FastOpen=json_data.get("FastOpen"),
            Finwait2timeout=json_data.get("Finwait2timeout"),
            FinwaitTimeout=json_data.get("FinwaitTimeout"),
            IdleTimeout=json_data.get("IdleTimeout"),
            KeepaliveInterval=json_data.get("KeepaliveInterval"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


