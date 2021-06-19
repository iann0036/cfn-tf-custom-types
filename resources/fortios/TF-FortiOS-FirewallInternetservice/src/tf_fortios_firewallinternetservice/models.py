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
    Database: Optional[str]
    Direction: Optional[str]
    ExtraIpRangeNumber: Optional[float]
    Fosid: Optional[float]
    IconId: Optional[float]
    Id: Optional[str]
    IpNumber: Optional[float]
    IpRangeNumber: Optional[float]
    Name: Optional[str]
    Obsolete: Optional[float]
    Reputation: Optional[float]
    Singularity: Optional[float]
    SldId: Optional[float]
    Vdomparam: Optional[str]

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
            Database=json_data.get("Database"),
            Direction=json_data.get("Direction"),
            ExtraIpRangeNumber=json_data.get("ExtraIpRangeNumber"),
            Fosid=json_data.get("Fosid"),
            IconId=json_data.get("IconId"),
            Id=json_data.get("Id"),
            IpNumber=json_data.get("IpNumber"),
            IpRangeNumber=json_data.get("IpRangeNumber"),
            Name=json_data.get("Name"),
            Obsolete=json_data.get("Obsolete"),
            Reputation=json_data.get("Reputation"),
            Singularity=json_data.get("Singularity"),
            SldId=json_data.get("SldId"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


