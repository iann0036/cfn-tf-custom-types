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
    Id: Optional[str]
    LoginPage: Optional[str]
    MaxConcurrentUser: Optional[float]
    NasIp: Optional[str]
    RadiusPort: Optional[float]
    RadiusServer: Optional[str]
    UrlPath: Optional[str]
    Vdomparam: Optional[str]
    VirtualHost: Optional[str]
    VirtualHostOnly: Optional[str]

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
            Id=json_data.get("Id"),
            LoginPage=json_data.get("LoginPage"),
            MaxConcurrentUser=json_data.get("MaxConcurrentUser"),
            NasIp=json_data.get("NasIp"),
            RadiusPort=json_data.get("RadiusPort"),
            RadiusServer=json_data.get("RadiusServer"),
            UrlPath=json_data.get("UrlPath"),
            Vdomparam=json_data.get("Vdomparam"),
            VirtualHost=json_data.get("VirtualHost"),
            VirtualHostOnly=json_data.get("VirtualHostOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


