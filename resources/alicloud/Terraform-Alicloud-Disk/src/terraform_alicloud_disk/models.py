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
    Category: Optional[str]
    DeleteAutoSnapshot: Optional[bool]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    EnableAutoSnapshot: Optional[bool]
    Encrypted: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupId: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

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
            Category=json_data.get("Category"),
            DeleteAutoSnapshot=json_data.get("DeleteAutoSnapshot"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            EnableAutoSnapshot=json_data.get("EnableAutoSnapshot"),
            Encrypted=json_data.get("Encrypted"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
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


