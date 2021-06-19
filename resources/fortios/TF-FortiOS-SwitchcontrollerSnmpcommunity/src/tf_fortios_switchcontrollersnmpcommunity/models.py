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
    DynamicSortSubtable: Optional[str]
    Events: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    QueryV1Port: Optional[float]
    QueryV1Status: Optional[str]
    QueryV2cPort: Optional[float]
    QueryV2cStatus: Optional[str]
    Status: Optional[str]
    TrapV1Lport: Optional[float]
    TrapV1Rport: Optional[float]
    TrapV1Status: Optional[str]
    TrapV2cLport: Optional[float]
    TrapV2cRport: Optional[float]
    TrapV2cStatus: Optional[str]
    Vdomparam: Optional[str]
    Hosts: Optional[Sequence["_HostsDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Events=json_data.get("Events"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            QueryV1Port=json_data.get("QueryV1Port"),
            QueryV1Status=json_data.get("QueryV1Status"),
            QueryV2cPort=json_data.get("QueryV2cPort"),
            QueryV2cStatus=json_data.get("QueryV2cStatus"),
            Status=json_data.get("Status"),
            TrapV1Lport=json_data.get("TrapV1Lport"),
            TrapV1Rport=json_data.get("TrapV1Rport"),
            TrapV1Status=json_data.get("TrapV1Status"),
            TrapV2cLport=json_data.get("TrapV2cLport"),
            TrapV2cRport=json_data.get("TrapV2cRport"),
            TrapV2cStatus=json_data.get("TrapV2cStatus"),
            Vdomparam=json_data.get("Vdomparam"),
            Hosts=deserialize_list(json_data.get("Hosts"), HostsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


