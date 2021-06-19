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
    DefaultPolicy: Optional[str]
    DisableDnsTemplate: Optional[float]
    DnssecServiceGroup: Optional[str]
    Drop: Optional[float]
    EnableCacheSharing: Optional[float]
    Forward: Optional[str]
    Id: Optional[str]
    MaxCacheEntrySize: Optional[float]
    MaxCacheSize: Optional[float]
    MaxQueryLength: Optional[float]
    Name: Optional[str]
    Period: Optional[float]
    QueryIdSwitch: Optional[float]
    RedirectToTcpPort: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    ClassList: Optional[Sequence["_ClassListDefinition"]]
    ResponseRateLimiting: Optional[Sequence["_ResponseRateLimitingDefinition"]]

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
            DefaultPolicy=json_data.get("DefaultPolicy"),
            DisableDnsTemplate=json_data.get("DisableDnsTemplate"),
            DnssecServiceGroup=json_data.get("DnssecServiceGroup"),
            Drop=json_data.get("Drop"),
            EnableCacheSharing=json_data.get("EnableCacheSharing"),
            Forward=json_data.get("Forward"),
            Id=json_data.get("Id"),
            MaxCacheEntrySize=json_data.get("MaxCacheEntrySize"),
            MaxCacheSize=json_data.get("MaxCacheSize"),
            MaxQueryLength=json_data.get("MaxQueryLength"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            QueryIdSwitch=json_data.get("QueryIdSwitch"),
            RedirectToTcpPort=json_data.get("RedirectToTcpPort"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            ClassList=deserialize_list(json_data.get("ClassList"), ClassListDefinition),
            ResponseRateLimiting=deserialize_list(json_data.get("ResponseRateLimiting"), ResponseRateLimitingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClassListDefinition(BaseModel):
    Name: Optional[str]
    Uuid: Optional[str]
    LidList: Optional[Sequence["_LidListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
            LidList=deserialize_list(json_data.get("LidList"), LidListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassListDefinition = ClassListDefinition


@dataclass
class LidListDefinition(BaseModel):
    ActionValue: Optional[str]
    ConnRateLimit: Optional[float]
    Lidnum: Optional[float]
    Lockout: Optional[float]
    Log: Optional[float]
    LogInterval: Optional[float]
    OverLimitAction: Optional[float]
    Per: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LidListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LidListDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionValue=json_data.get("ActionValue"),
            ConnRateLimit=json_data.get("ConnRateLimit"),
            Lidnum=json_data.get("Lidnum"),
            Lockout=json_data.get("Lockout"),
            Log=json_data.get("Log"),
            LogInterval=json_data.get("LogInterval"),
            OverLimitAction=json_data.get("OverLimitAction"),
            Per=json_data.get("Per"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LidListDefinition = LidListDefinition


@dataclass
class ResponseRateLimitingDefinition(BaseModel):
    Action: Optional[str]
    EnableLog: Optional[float]
    FilterResponseRate: Optional[float]
    ResponseRate: Optional[float]
    SlipRate: Optional[float]
    Uuid: Optional[str]
    Window: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseRateLimitingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseRateLimitingDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            EnableLog=json_data.get("EnableLog"),
            FilterResponseRate=json_data.get("FilterResponseRate"),
            ResponseRate=json_data.get("ResponseRate"),
            SlipRate=json_data.get("SlipRate"),
            Uuid=json_data.get("Uuid"),
            Window=json_data.get("Window"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseRateLimitingDefinition = ResponseRateLimitingDefinition


