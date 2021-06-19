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
    CnnRouteType: Optional[str]
    CreateTime: Optional[str]
    EnableBgp: Optional[bool]
    GatewayType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NetworkInstanceId: Optional[str]
    NetworkType: Optional[str]

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
            CnnRouteType=json_data.get("CnnRouteType"),
            CreateTime=json_data.get("CreateTime"),
            EnableBgp=json_data.get("EnableBgp"),
            GatewayType=json_data.get("GatewayType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkInstanceId=json_data.get("NetworkInstanceId"),
            NetworkType=json_data.get("NetworkType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


