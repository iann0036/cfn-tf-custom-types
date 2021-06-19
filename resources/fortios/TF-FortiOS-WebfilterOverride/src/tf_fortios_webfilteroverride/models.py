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
    Expires: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Initiator: Optional[str]
    Ip: Optional[str]
    Ip6: Optional[str]
    NewProfile: Optional[str]
    OldProfile: Optional[str]
    Scope: Optional[str]
    Status: Optional[str]
    User: Optional[str]
    UserGroup: Optional[str]
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
            Expires=json_data.get("Expires"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Initiator=json_data.get("Initiator"),
            Ip=json_data.get("Ip"),
            Ip6=json_data.get("Ip6"),
            NewProfile=json_data.get("NewProfile"),
            OldProfile=json_data.get("OldProfile"),
            Scope=json_data.get("Scope"),
            Status=json_data.get("Status"),
            User=json_data.get("User"),
            UserGroup=json_data.get("UserGroup"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


