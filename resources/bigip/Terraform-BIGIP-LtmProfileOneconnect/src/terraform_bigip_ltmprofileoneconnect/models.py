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
    DefaultsFrom: Optional[str]
    IdleTimeoutOverride: Optional[str]
    MaxAge: Optional[float]
    MaxReuse: Optional[float]
    MaxSize: Optional[float]
    Name: Optional[str]
    Partition: Optional[str]
    SharePools: Optional[str]
    SourceMask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            IdleTimeoutOverride=json_data.get("IdleTimeoutOverride"),
            MaxAge=json_data.get("MaxAge"),
            MaxReuse=json_data.get("MaxReuse"),
            MaxSize=json_data.get("MaxSize"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            SharePools=json_data.get("SharePools"),
            SourceMask=json_data.get("SourceMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


