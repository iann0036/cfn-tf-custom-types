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
    CreateDirectories: Optional[bool]
    Datacenter: Optional[str]
    Datastore: Optional[str]
    DestinationFile: Optional[str]
    SourceDatacenter: Optional[str]
    SourceDatastore: Optional[str]
    SourceFile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateDirectories=json_data.get("CreateDirectories"),
            Datacenter=json_data.get("Datacenter"),
            Datastore=json_data.get("Datastore"),
            DestinationFile=json_data.get("DestinationFile"),
            SourceDatacenter=json_data.get("SourceDatacenter"),
            SourceDatastore=json_data.get("SourceDatastore"),
            SourceFile=json_data.get("SourceFile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


