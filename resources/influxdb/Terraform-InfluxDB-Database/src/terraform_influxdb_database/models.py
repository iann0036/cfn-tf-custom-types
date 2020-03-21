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
    Name: Optional[str]
    RetentionPolicies: Optional[Sequence["_RetentionPolicies"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            RetentionPolicies=json_data.get("RetentionPolicies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RetentionPolicies:
    Default: Optional[bool]
    Duration: Optional[str]
    Name: Optional[str]
    Replication: Optional[float]
    Shardgroupduration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicies"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Duration=json_data.get("Duration"),
            Name=json_data.get("Name"),
            Replication=json_data.get("Replication"),
            Shardgroupduration=json_data.get("Shardgroupduration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicies = RetentionPolicies


