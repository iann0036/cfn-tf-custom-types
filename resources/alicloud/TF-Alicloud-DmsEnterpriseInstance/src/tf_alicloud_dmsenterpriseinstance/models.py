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
    DataLinkName: Optional[str]
    DatabasePassword: Optional[str]
    DatabaseUser: Optional[str]
    DbaId: Optional[str]
    DbaNickName: Optional[str]
    DbaUid: Optional[float]
    DdlOnline: Optional[float]
    EcsInstanceId: Optional[str]
    EcsRegion: Optional[str]
    EnvType: Optional[str]
    ExportTimeout: Optional[float]
    Host: Optional[str]
    Id: Optional[str]
    InstanceAlias: Optional[str]
    InstanceId: Optional[str]
    InstanceName: Optional[str]
    InstanceSource: Optional[str]
    InstanceType: Optional[str]
    NetworkType: Optional[str]
    Port: Optional[float]
    QueryTimeout: Optional[float]
    SafeRule: Optional[str]
    SafeRuleId: Optional[str]
    Sid: Optional[str]
    SkipTest: Optional[bool]
    State: Optional[str]
    Status: Optional[str]
    Tid: Optional[float]
    UseDsql: Optional[float]
    VpcId: Optional[str]
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
            DataLinkName=json_data.get("DataLinkName"),
            DatabasePassword=json_data.get("DatabasePassword"),
            DatabaseUser=json_data.get("DatabaseUser"),
            DbaId=json_data.get("DbaId"),
            DbaNickName=json_data.get("DbaNickName"),
            DbaUid=json_data.get("DbaUid"),
            DdlOnline=json_data.get("DdlOnline"),
            EcsInstanceId=json_data.get("EcsInstanceId"),
            EcsRegion=json_data.get("EcsRegion"),
            EnvType=json_data.get("EnvType"),
            ExportTimeout=json_data.get("ExportTimeout"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            InstanceAlias=json_data.get("InstanceAlias"),
            InstanceId=json_data.get("InstanceId"),
            InstanceName=json_data.get("InstanceName"),
            InstanceSource=json_data.get("InstanceSource"),
            InstanceType=json_data.get("InstanceType"),
            NetworkType=json_data.get("NetworkType"),
            Port=json_data.get("Port"),
            QueryTimeout=json_data.get("QueryTimeout"),
            SafeRule=json_data.get("SafeRule"),
            SafeRuleId=json_data.get("SafeRuleId"),
            Sid=json_data.get("Sid"),
            SkipTest=json_data.get("SkipTest"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            Tid=json_data.get("Tid"),
            UseDsql=json_data.get("UseDsql"),
            VpcId=json_data.get("VpcId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


