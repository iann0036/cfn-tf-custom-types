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
    ActiveAuthScheme: Optional[str]
    AuthHttps: Optional[str]
    CaptivePortal: Optional[str]
    CaptivePortal6: Optional[str]
    CaptivePortalIp: Optional[str]
    CaptivePortalIp6: Optional[str]
    CaptivePortalPort: Optional[float]
    CaptivePortalSslPort: Optional[float]
    CaptivePortalType: Optional[str]
    Id: Optional[str]
    SsoAuthScheme: Optional[str]
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
            ActiveAuthScheme=json_data.get("ActiveAuthScheme"),
            AuthHttps=json_data.get("AuthHttps"),
            CaptivePortal=json_data.get("CaptivePortal"),
            CaptivePortal6=json_data.get("CaptivePortal6"),
            CaptivePortalIp=json_data.get("CaptivePortalIp"),
            CaptivePortalIp6=json_data.get("CaptivePortalIp6"),
            CaptivePortalPort=json_data.get("CaptivePortalPort"),
            CaptivePortalSslPort=json_data.get("CaptivePortalSslPort"),
            CaptivePortalType=json_data.get("CaptivePortalType"),
            Id=json_data.get("Id"),
            SsoAuthScheme=json_data.get("SsoAuthScheme"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


