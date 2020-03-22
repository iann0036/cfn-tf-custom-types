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
    Attempts: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Parallelism: Optional[float]
    ResourceGroupName: Optional[str]
    Size: Optional[float]
    Source: Optional[str]
    SourceUri: Optional[str]
    StorageAccountName: Optional[str]
    StorageContainerName: Optional[str]
    Type: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Attempts=json_data.get("Attempts"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parallelism=json_data.get("Parallelism"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Size=json_data.get("Size"),
            Source=json_data.get("Source"),
            SourceUri=json_data.get("SourceUri"),
            StorageAccountName=json_data.get("StorageAccountName"),
            StorageContainerName=json_data.get("StorageContainerName"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


