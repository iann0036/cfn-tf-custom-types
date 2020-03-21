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
    AvailabilityZone: Optional[str]
    EbsOptimized: Optional[bool]
    EndDate: Optional[str]
    EndDateType: Optional[str]
    EphemeralStorage: Optional[bool]
    Id: Optional[str]
    InstanceCount: Optional[float]
    InstanceMatchCriteria: Optional[str]
    InstancePlatform: Optional[str]
    InstanceType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Tenancy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            EbsOptimized=json_data.get("EbsOptimized"),
            EndDate=json_data.get("EndDate"),
            EndDateType=json_data.get("EndDateType"),
            EphemeralStorage=json_data.get("EphemeralStorage"),
            Id=json_data.get("Id"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceMatchCriteria=json_data.get("InstanceMatchCriteria"),
            InstancePlatform=json_data.get("InstancePlatform"),
            InstanceType=json_data.get("InstanceType"),
            Tags=json_data.get("Tags"),
            Tenancy=json_data.get("Tenancy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


