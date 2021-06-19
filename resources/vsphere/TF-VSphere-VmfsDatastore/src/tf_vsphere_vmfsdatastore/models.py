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
    Accessible: Optional[bool]
    Capacity: Optional[float]
    CustomAttributes: Optional[Sequence["_CustomAttributesDefinition"]]
    DatastoreClusterId: Optional[str]
    Disks: Optional[Sequence[str]]
    Folder: Optional[str]
    FreeSpace: Optional[float]
    HostSystemId: Optional[str]
    Id: Optional[str]
    MaintenanceMode: Optional[str]
    MultipleHostAccess: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    UncommittedSpace: Optional[float]
    Url: Optional[str]

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
            Accessible=json_data.get("Accessible"),
            Capacity=json_data.get("Capacity"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttributesDefinition),
            DatastoreClusterId=json_data.get("DatastoreClusterId"),
            Disks=json_data.get("Disks"),
            Folder=json_data.get("Folder"),
            FreeSpace=json_data.get("FreeSpace"),
            HostSystemId=json_data.get("HostSystemId"),
            Id=json_data.get("Id"),
            MaintenanceMode=json_data.get("MaintenanceMode"),
            MultipleHostAccess=json_data.get("MultipleHostAccess"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            UncommittedSpace=json_data.get("UncommittedSpace"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributesDefinition = CustomAttributesDefinition


