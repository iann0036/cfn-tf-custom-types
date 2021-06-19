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
    Agelimit: Optional[float]
    Destination: Optional[str]
    DropBlocked: Optional[str]
    DropHeuristic: Optional[str]
    DropInfected: Optional[str]
    Id: Optional[str]
    Lowspace: Optional[str]
    Maxfilesize: Optional[float]
    QuarantineQuota: Optional[float]
    StoreBlocked: Optional[str]
    StoreHeuristic: Optional[str]
    StoreInfected: Optional[str]
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
            Agelimit=json_data.get("Agelimit"),
            Destination=json_data.get("Destination"),
            DropBlocked=json_data.get("DropBlocked"),
            DropHeuristic=json_data.get("DropHeuristic"),
            DropInfected=json_data.get("DropInfected"),
            Id=json_data.get("Id"),
            Lowspace=json_data.get("Lowspace"),
            Maxfilesize=json_data.get("Maxfilesize"),
            QuarantineQuota=json_data.get("QuarantineQuota"),
            StoreBlocked=json_data.get("StoreBlocked"),
            StoreHeuristic=json_data.get("StoreHeuristic"),
            StoreInfected=json_data.get("StoreInfected"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


