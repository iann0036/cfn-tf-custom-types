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
    Id: Optional[str]
    MethodPath: Optional[str]
    RestApiId: Optional[str]
    StageName: Optional[str]
    Settings: Optional[Sequence["_SettingsDefinition"]]

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
            Id=json_data.get("Id"),
            MethodPath=json_data.get("MethodPath"),
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
            Settings=deserialize_list(json_data.get("Settings"), SettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SettingsDefinition(BaseModel):
    CacheDataEncrypted: Optional[bool]
    CacheTtlInSeconds: Optional[float]
    CachingEnabled: Optional[bool]
    DataTraceEnabled: Optional[bool]
    LoggingLevel: Optional[str]
    MetricsEnabled: Optional[bool]
    RequireAuthorizationForCacheControl: Optional[bool]
    ThrottlingBurstLimit: Optional[float]
    ThrottlingRateLimit: Optional[float]
    UnauthorizedCacheControlHeaderStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheDataEncrypted=json_data.get("CacheDataEncrypted"),
            CacheTtlInSeconds=json_data.get("CacheTtlInSeconds"),
            CachingEnabled=json_data.get("CachingEnabled"),
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            LoggingLevel=json_data.get("LoggingLevel"),
            MetricsEnabled=json_data.get("MetricsEnabled"),
            RequireAuthorizationForCacheControl=json_data.get("RequireAuthorizationForCacheControl"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
            UnauthorizedCacheControlHeaderStrategy=json_data.get("UnauthorizedCacheControlHeaderStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingsDefinition = SettingsDefinition


