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
    CloudwatchRoleArn: Optional[str]
    ThrottleSettings: Optional[Sequence["_ThrottleSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CloudwatchRoleArn=json_data.get("CloudwatchRoleArn"),
            ThrottleSettings=json_data.get("ThrottleSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ThrottleSettings:
    BurstLimit: Optional[float]
    RateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThrottleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThrottleSettings"]:
        if not json_data:
            return None
        return cls(
            BurstLimit=json_data.get("BurstLimit"),
            RateLimit=json_data.get("RateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThrottleSettings = ThrottleSettings


