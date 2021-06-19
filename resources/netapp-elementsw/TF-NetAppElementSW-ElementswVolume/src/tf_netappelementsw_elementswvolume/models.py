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
    Account: Optional[str]
    Attributes: Optional[Sequence[str]]
    BurstIops: Optional[float]
    Enable512e: Optional[bool]
    Id: Optional[str]
    Iqn: Optional[str]
    MaxIops: Optional[float]
    MinIops: Optional[float]
    Name: Optional[str]
    TotalSize: Optional[float]

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
            Account=json_data.get("Account"),
            Attributes=json_data.get("Attributes"),
            BurstIops=json_data.get("BurstIops"),
            Enable512e=json_data.get("Enable512e"),
            Id=json_data.get("Id"),
            Iqn=json_data.get("Iqn"),
            MaxIops=json_data.get("MaxIops"),
            MinIops=json_data.get("MinIops"),
            Name=json_data.get("Name"),
            TotalSize=json_data.get("TotalSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


