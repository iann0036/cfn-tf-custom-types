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
    ClientId: Optional[str]
    ClientSecretKey: Optional[str]
    ClientSecretScope: Optional[str]
    ClusterId: Optional[str]
    ContainerName: Optional[str]
    Directory: Optional[str]
    Id: Optional[str]
    InitializeFileSystem: Optional[bool]
    MountName: Optional[str]
    Source: Optional[str]
    StorageAccountName: Optional[str]
    TenantId: Optional[str]

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
            ClientId=json_data.get("ClientId"),
            ClientSecretKey=json_data.get("ClientSecretKey"),
            ClientSecretScope=json_data.get("ClientSecretScope"),
            ClusterId=json_data.get("ClusterId"),
            ContainerName=json_data.get("ContainerName"),
            Directory=json_data.get("Directory"),
            Id=json_data.get("Id"),
            InitializeFileSystem=json_data.get("InitializeFileSystem"),
            MountName=json_data.get("MountName"),
            Source=json_data.get("Source"),
            StorageAccountName=json_data.get("StorageAccountName"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


