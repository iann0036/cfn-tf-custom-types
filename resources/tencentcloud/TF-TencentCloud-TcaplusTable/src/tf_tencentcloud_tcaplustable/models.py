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
    ClusterId: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    Error: Optional[str]
    Id: Optional[str]
    IdlId: Optional[str]
    ReservedReadCu: Optional[float]
    ReservedVolume: Optional[float]
    ReservedWriteCu: Optional[float]
    Status: Optional[str]
    TableIdlType: Optional[str]
    TableName: Optional[str]
    TableSize: Optional[float]
    TableType: Optional[str]
    TablegroupId: Optional[str]

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
            ClusterId=json_data.get("ClusterId"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Error=json_data.get("Error"),
            Id=json_data.get("Id"),
            IdlId=json_data.get("IdlId"),
            ReservedReadCu=json_data.get("ReservedReadCu"),
            ReservedVolume=json_data.get("ReservedVolume"),
            ReservedWriteCu=json_data.get("ReservedWriteCu"),
            Status=json_data.get("Status"),
            TableIdlType=json_data.get("TableIdlType"),
            TableName=json_data.get("TableName"),
            TableSize=json_data.get("TableSize"),
            TableType=json_data.get("TableType"),
            TablegroupId=json_data.get("TablegroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


