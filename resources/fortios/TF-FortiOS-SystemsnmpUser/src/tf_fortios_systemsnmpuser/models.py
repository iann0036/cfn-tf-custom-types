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
    AuthProto: Optional[str]
    AuthPwd: Optional[str]
    Events: Optional[str]
    HaDirect: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NotifyHosts: Optional[str]
    NotifyHosts6: Optional[str]
    PrivProto: Optional[str]
    PrivPwd: Optional[str]
    Queries: Optional[str]
    QueryPort: Optional[float]
    SecurityLevel: Optional[str]
    SourceIp: Optional[str]
    SourceIpv6: Optional[str]
    Status: Optional[str]
    TrapLport: Optional[float]
    TrapRport: Optional[float]
    TrapStatus: Optional[str]
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
            AuthProto=json_data.get("AuthProto"),
            AuthPwd=json_data.get("AuthPwd"),
            Events=json_data.get("Events"),
            HaDirect=json_data.get("HaDirect"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotifyHosts=json_data.get("NotifyHosts"),
            NotifyHosts6=json_data.get("NotifyHosts6"),
            PrivProto=json_data.get("PrivProto"),
            PrivPwd=json_data.get("PrivPwd"),
            Queries=json_data.get("Queries"),
            QueryPort=json_data.get("QueryPort"),
            SecurityLevel=json_data.get("SecurityLevel"),
            SourceIp=json_data.get("SourceIp"),
            SourceIpv6=json_data.get("SourceIpv6"),
            Status=json_data.get("Status"),
            TrapLport=json_data.get("TrapLport"),
            TrapRport=json_data.get("TrapRport"),
            TrapStatus=json_data.get("TrapStatus"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


