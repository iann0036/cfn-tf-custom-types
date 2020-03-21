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
    BytesUsed: Optional[float]
    ContainerRead: Optional[Sequence[str]]
    ContainerSyncKey: Optional[str]
    ContainerSyncTo: Optional[str]
    ContainerWrite: Optional[Sequence[str]]
    CreatedAt: Optional[str]
    HistoryLocation: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    ObjectCount: Optional[float]
    StoragePolicy: Optional[str]
    VersionsLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BytesUsed=json_data.get("BytesUsed"),
            ContainerRead=json_data.get("ContainerRead"),
            ContainerSyncKey=json_data.get("ContainerSyncKey"),
            ContainerSyncTo=json_data.get("ContainerSyncTo"),
            ContainerWrite=json_data.get("ContainerWrite"),
            CreatedAt=json_data.get("CreatedAt"),
            HistoryLocation=json_data.get("HistoryLocation"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            ObjectCount=json_data.get("ObjectCount"),
            StoragePolicy=json_data.get("StoragePolicy"),
            VersionsLocation=json_data.get("VersionsLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


