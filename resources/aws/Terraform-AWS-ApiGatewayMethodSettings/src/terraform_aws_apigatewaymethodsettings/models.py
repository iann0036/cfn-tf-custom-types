# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Id: Optional[str]
    MethodPath: Optional[str]
    RestApiId: Optional[str]
    StageName: Optional[str]
    Settings: Optional[Sequence["_Settings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            MethodPath=json_data.get("MethodPath"),
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
            Settings=json_data.get("Settings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Settings:
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
        cls: Type["_Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Settings"]:
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
_Settings = Settings


