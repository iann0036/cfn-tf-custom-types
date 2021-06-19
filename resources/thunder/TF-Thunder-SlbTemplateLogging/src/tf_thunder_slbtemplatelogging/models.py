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
    Auto: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    KeepEnd: Optional[float]
    KeepStart: Optional[float]
    LocalLogging: Optional[float]
    Mask: Optional[str]
    Name: Optional[str]
    PcreMask: Optional[str]
    Pool: Optional[str]
    PoolShared: Optional[str]
    ServiceGroup: Optional[str]
    SharedPartitionPool: Optional[float]
    SharedPartitionTcpProxyTemplate: Optional[float]
    TcpProxy: Optional[str]
    TemplateTcpProxyShared: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]

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
            Auto=json_data.get("Auto"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            KeepEnd=json_data.get("KeepEnd"),
            KeepStart=json_data.get("KeepStart"),
            LocalLogging=json_data.get("LocalLogging"),
            Mask=json_data.get("Mask"),
            Name=json_data.get("Name"),
            PcreMask=json_data.get("PcreMask"),
            Pool=json_data.get("Pool"),
            PoolShared=json_data.get("PoolShared"),
            ServiceGroup=json_data.get("ServiceGroup"),
            SharedPartitionPool=json_data.get("SharedPartitionPool"),
            SharedPartitionTcpProxyTemplate=json_data.get("SharedPartitionTcpProxyTemplate"),
            TcpProxy=json_data.get("TcpProxy"),
            TemplateTcpProxyShared=json_data.get("TemplateTcpProxyShared"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


