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
    BusSubType: Optional[str]
    BusType: Optional[str]
    DatastoreName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Iops: Optional[float]
    IsAttached: Optional[bool]
    Name: Optional[str]
    Org: Optional[str]
    OwnerName: Optional[str]
    SizeInMb: Optional[float]
    StorageProfile: Optional[str]
    Vdc: Optional[str]

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
            BusSubType=json_data.get("BusSubType"),
            BusType=json_data.get("BusType"),
            DatastoreName=json_data.get("DatastoreName"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Iops=json_data.get("Iops"),
            IsAttached=json_data.get("IsAttached"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            OwnerName=json_data.get("OwnerName"),
            SizeInMb=json_data.get("SizeInMb"),
            StorageProfile=json_data.get("StorageProfile"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


