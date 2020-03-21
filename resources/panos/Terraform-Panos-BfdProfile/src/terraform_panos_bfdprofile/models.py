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
    DetectionMultiplier: Optional[float]
    HoldTime: Optional[float]
    MinimumRxInterval: Optional[float]
    MinimumRxTtl: Optional[float]
    MinimumTxInterval: Optional[float]
    Mode: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DetectionMultiplier=json_data.get("DetectionMultiplier"),
            HoldTime=json_data.get("HoldTime"),
            MinimumRxInterval=json_data.get("MinimumRxInterval"),
            MinimumRxTtl=json_data.get("MinimumRxTtl"),
            MinimumTxInterval=json_data.get("MinimumTxInterval"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


