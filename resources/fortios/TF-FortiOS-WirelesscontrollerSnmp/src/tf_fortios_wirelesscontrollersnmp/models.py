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
    ContactInfo: Optional[str]
    DynamicSortSubtable: Optional[str]
    EngineId: Optional[str]
    Id: Optional[str]
    TrapHighCpuThreshold: Optional[float]
    TrapHighMemThreshold: Optional[float]
    Vdomparam: Optional[str]
    Community: Optional[Sequence["_CommunityDefinition"]]
    User: Optional[Sequence["_UserDefinition"]]

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
            ContactInfo=json_data.get("ContactInfo"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EngineId=json_data.get("EngineId"),
            Id=json_data.get("Id"),
            TrapHighCpuThreshold=json_data.get("TrapHighCpuThreshold"),
            TrapHighMemThreshold=json_data.get("TrapHighMemThreshold"),
            Vdomparam=json_data.get("Vdomparam"),
            Community=deserialize_list(json_data.get("Community"), CommunityDefinition),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CommunityDefinition(BaseModel):
    Id: Optional[float]
    Name: Optional[str]
    QueryV1Status: Optional[str]
    QueryV2cStatus: Optional[str]
    Status: Optional[str]
    TrapV1Status: Optional[str]
    TrapV2cStatus: Optional[str]
    Hosts: Optional[Sequence["_HostsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CommunityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommunityDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            QueryV1Status=json_data.get("QueryV1Status"),
            QueryV2cStatus=json_data.get("QueryV2cStatus"),
            Status=json_data.get("Status"),
            TrapV1Status=json_data.get("TrapV1Status"),
            TrapV2cStatus=json_data.get("TrapV2cStatus"),
            Hosts=deserialize_list(json_data.get("Hosts"), HostsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommunityDefinition = CommunityDefinition


@dataclass
class HostsDefinition(BaseModel):
    Id: Optional[float]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostsDefinition = HostsDefinition


@dataclass
class UserDefinition(BaseModel):
    AuthProto: Optional[str]
    AuthPwd: Optional[str]
    Name: Optional[str]
    NotifyHosts: Optional[str]
    PrivProto: Optional[str]
    PrivPwd: Optional[str]
    Queries: Optional[str]
    SecurityLevel: Optional[str]
    Status: Optional[str]
    TrapStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthProto=json_data.get("AuthProto"),
            AuthPwd=json_data.get("AuthPwd"),
            Name=json_data.get("Name"),
            NotifyHosts=json_data.get("NotifyHosts"),
            PrivProto=json_data.get("PrivProto"),
            PrivPwd=json_data.get("PrivPwd"),
            Queries=json_data.get("Queries"),
            SecurityLevel=json_data.get("SecurityLevel"),
            Status=json_data.get("Status"),
            TrapStatus=json_data.get("TrapStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


