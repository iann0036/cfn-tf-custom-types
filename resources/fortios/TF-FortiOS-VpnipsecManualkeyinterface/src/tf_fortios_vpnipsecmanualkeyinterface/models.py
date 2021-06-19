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
    AddrType: Optional[str]
    AuthAlg: Optional[str]
    AuthKey: Optional[str]
    EncAlg: Optional[str]
    EncKey: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    IpVersion: Optional[str]
    LocalGw: Optional[str]
    LocalGw6: Optional[str]
    LocalSpi: Optional[str]
    Name: Optional[str]
    RemoteGw: Optional[str]
    RemoteGw6: Optional[str]
    RemoteSpi: Optional[str]
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
            AddrType=json_data.get("AddrType"),
            AuthAlg=json_data.get("AuthAlg"),
            AuthKey=json_data.get("AuthKey"),
            EncAlg=json_data.get("EncAlg"),
            EncKey=json_data.get("EncKey"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpVersion=json_data.get("IpVersion"),
            LocalGw=json_data.get("LocalGw"),
            LocalGw6=json_data.get("LocalGw6"),
            LocalSpi=json_data.get("LocalSpi"),
            Name=json_data.get("Name"),
            RemoteGw=json_data.get("RemoteGw"),
            RemoteGw6=json_data.get("RemoteGw6"),
            RemoteSpi=json_data.get("RemoteSpi"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


