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
    All: Optional[float]
    ConnectionResourceEvent: Optional[float]
    Id: Optional[str]
    ResourceUsageWarning: Optional[float]
    Server: Optional[float]
    ServerPort: Optional[float]
    SslCertChange: Optional[float]
    SslCertExpire: Optional[float]
    SystemThreshold: Optional[float]
    Uuid: Optional[str]
    Vip: Optional[float]
    VipPort: Optional[float]

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
            All=json_data.get("All"),
            ConnectionResourceEvent=json_data.get("ConnectionResourceEvent"),
            Id=json_data.get("Id"),
            ResourceUsageWarning=json_data.get("ResourceUsageWarning"),
            Server=json_data.get("Server"),
            ServerPort=json_data.get("ServerPort"),
            SslCertChange=json_data.get("SslCertChange"),
            SslCertExpire=json_data.get("SslCertExpire"),
            SystemThreshold=json_data.get("SystemThreshold"),
            Uuid=json_data.get("Uuid"),
            Vip=json_data.get("Vip"),
            VipPort=json_data.get("VipPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


