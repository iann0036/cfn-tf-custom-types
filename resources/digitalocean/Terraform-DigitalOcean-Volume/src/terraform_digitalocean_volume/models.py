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
    Description: Optional[str]
    DropletIds: Optional[Sequence[float]]
    FilesystemLabel: Optional[str]
    FilesystemType: Optional[str]
    InitialFilesystemLabel: Optional[str]
    InitialFilesystemType: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]
    Tags: Optional[Sequence[str]]
    Urn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DropletIds=json_data.get("DropletIds"),
            FilesystemLabel=json_data.get("FilesystemLabel"),
            FilesystemType=json_data.get("FilesystemType"),
            InitialFilesystemLabel=json_data.get("InitialFilesystemLabel"),
            InitialFilesystemType=json_data.get("InitialFilesystemType"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            Tags=json_data.get("Tags"),
            Urn=json_data.get("Urn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


