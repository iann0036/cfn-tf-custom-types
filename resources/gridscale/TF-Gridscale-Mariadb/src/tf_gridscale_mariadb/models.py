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
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    ListenPort: Optional[Sequence["_ListenPortDefinition"]]
    MariadbBinlogFormat: Optional[str]
    MariadbDefaultTimeZone: Optional[str]
    MariadbLogBin: Optional[bool]
    MariadbMaxAllowedPacket: Optional[str]
    MariadbMaxConnections: Optional[float]
    MariadbQueryCache: Optional[bool]
    MariadbQueryCacheLimit: Optional[str]
    MariadbQueryCacheSize: Optional[str]
    MariadbServerId: Optional[float]
    MariadbSqlMode: Optional[str]
    MaxCoreCount: Optional[float]
    Name: Optional[str]
    NetworkUuid: Optional[str]
    Password: Optional[str]
    PerformanceClass: Optional[str]
    Release: Optional[str]
    SecurityZoneUuid: Optional[str]
    ServiceTemplateUuid: Optional[str]
    Status: Optional[str]
    UsageInMinutes: Optional[float]
    Username: Optional[str]
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
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            ListenPort=deserialize_list(json_data.get("ListenPort"), ListenPortDefinition),
            MariadbBinlogFormat=json_data.get("MariadbBinlogFormat"),
            MariadbDefaultTimeZone=json_data.get("MariadbDefaultTimeZone"),
            MariadbLogBin=json_data.get("MariadbLogBin"),
            MariadbMaxAllowedPacket=json_data.get("MariadbMaxAllowedPacket"),
            MariadbMaxConnections=json_data.get("MariadbMaxConnections"),
            MariadbQueryCache=json_data.get("MariadbQueryCache"),
            MariadbQueryCacheLimit=json_data.get("MariadbQueryCacheLimit"),
            MariadbQueryCacheSize=json_data.get("MariadbQueryCacheSize"),
            MariadbServerId=json_data.get("MariadbServerId"),
            MariadbSqlMode=json_data.get("MariadbSqlMode"),
            MaxCoreCount=json_data.get("MaxCoreCount"),
            Name=json_data.get("Name"),
            NetworkUuid=json_data.get("NetworkUuid"),
            Password=json_data.get("Password"),
            PerformanceClass=json_data.get("PerformanceClass"),
            Release=json_data.get("Release"),
            SecurityZoneUuid=json_data.get("SecurityZoneUuid"),
            ServiceTemplateUuid=json_data.get("ServiceTemplateUuid"),
            Status=json_data.get("Status"),
            UsageInMinutes=json_data.get("UsageInMinutes"),
            Username=json_data.get("Username"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ListenPortDefinition(BaseModel):
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ListenPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenPortDefinition = ListenPortDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


