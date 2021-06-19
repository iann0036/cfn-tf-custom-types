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
    Arn: Optional[str]
    DbProxyName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ConnectionPoolConfig: Optional[Sequence["_ConnectionPoolConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Arn=json_data.get("Arn"),
            DbProxyName=json_data.get("DbProxyName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ConnectionPoolConfig=deserialize_list(json_data.get("ConnectionPoolConfig"), ConnectionPoolConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionPoolConfigDefinition(BaseModel):
    ConnectionBorrowTimeout: Optional[float]
    InitQuery: Optional[str]
    MaxConnectionsPercent: Optional[float]
    MaxIdleConnectionsPercent: Optional[float]
    SessionPinningFilters: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionPoolConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionPoolConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionBorrowTimeout=json_data.get("ConnectionBorrowTimeout"),
            InitQuery=json_data.get("InitQuery"),
            MaxConnectionsPercent=json_data.get("MaxConnectionsPercent"),
            MaxIdleConnectionsPercent=json_data.get("MaxIdleConnectionsPercent"),
            SessionPinningFilters=json_data.get("SessionPinningFilters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionPoolConfigDefinition = ConnectionPoolConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


