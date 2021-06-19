# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    CdnUrl: Optional[str]
    CreatedAt: Optional[str]
    DeletedAt: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IndexFiles: Optional[bool]
    Name: Optional[str]
    Namespace: Optional[str]
    NamespaceUrl: Optional[str]
    RepositoryType: Optional[str]
    SelfHtmlUrl: Optional[str]
    SelfUrl: Optional[str]
    Slug: Optional[str]
    SlugPerm: Optional[str]
    StorageRegion: Optional[str]
    WaitForDeletion: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CdnUrl=json_data.get("CdnUrl"),
            CreatedAt=json_data.get("CreatedAt"),
            DeletedAt=json_data.get("DeletedAt"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IndexFiles=json_data.get("IndexFiles"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NamespaceUrl=json_data.get("NamespaceUrl"),
            RepositoryType=json_data.get("RepositoryType"),
            SelfHtmlUrl=json_data.get("SelfHtmlUrl"),
            SelfUrl=json_data.get("SelfUrl"),
            Slug=json_data.get("Slug"),
            SlugPerm=json_data.get("SlugPerm"),
            StorageRegion=json_data.get("StorageRegion"),
            WaitForDeletion=json_data.get("WaitForDeletion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


