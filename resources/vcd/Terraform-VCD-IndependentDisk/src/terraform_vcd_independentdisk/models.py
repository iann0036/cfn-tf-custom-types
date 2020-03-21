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
    BusSubType: Optional[str]
    BusType: Optional[str]
    DatastoreName: Optional[str]
    Description: Optional[str]
    Iops: Optional[float]
    IsAttached: Optional[bool]
    Name: Optional[str]
    Org: Optional[str]
    OwnerName: Optional[str]
    Size: Optional[float]
    StorageProfile: Optional[str]
    Vdc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BusSubType=json_data.get("BusSubType"),
            BusType=json_data.get("BusType"),
            DatastoreName=json_data.get("DatastoreName"),
            Description=json_data.get("Description"),
            Iops=json_data.get("Iops"),
            IsAttached=json_data.get("IsAttached"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            OwnerName=json_data.get("OwnerName"),
            Size=json_data.get("Size"),
            StorageProfile=json_data.get("StorageProfile"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


