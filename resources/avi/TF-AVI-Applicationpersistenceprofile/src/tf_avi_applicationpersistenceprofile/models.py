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
    Description: Optional[str]
    Id: Optional[str]
    IsFederated: Optional[bool]
    Name: Optional[str]
    PersistenceType: Optional[str]
    ServerHmDownRecovery: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    AppCookiePersistenceProfile: Optional[Sequence["_AppCookiePersistenceProfileDefinition"]]
    HdrPersistenceProfile: Optional[Sequence["_HdrPersistenceProfileDefinition"]]
    HttpCookiePersistenceProfile: Optional[Sequence["_HttpCookiePersistenceProfileDefinition"]]
    IpPersistenceProfile: Optional[Sequence["_IpPersistenceProfileDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsFederated=json_data.get("IsFederated"),
            Name=json_data.get("Name"),
            PersistenceType=json_data.get("PersistenceType"),
            ServerHmDownRecovery=json_data.get("ServerHmDownRecovery"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            AppCookiePersistenceProfile=deserialize_list(json_data.get("AppCookiePersistenceProfile"), AppCookiePersistenceProfileDefinition),
            HdrPersistenceProfile=deserialize_list(json_data.get("HdrPersistenceProfile"), HdrPersistenceProfileDefinition),
            HttpCookiePersistenceProfile=deserialize_list(json_data.get("HttpCookiePersistenceProfile"), HttpCookiePersistenceProfileDefinition),
            IpPersistenceProfile=deserialize_list(json_data.get("IpPersistenceProfile"), IpPersistenceProfileDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppCookiePersistenceProfileDefinition(BaseModel):
    EncryptionKey: Optional[str]
    PrstHdrName: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AppCookiePersistenceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppCookiePersistenceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionKey=json_data.get("EncryptionKey"),
            PrstHdrName=json_data.get("PrstHdrName"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppCookiePersistenceProfileDefinition = AppCookiePersistenceProfileDefinition


@dataclass
class HdrPersistenceProfileDefinition(BaseModel):
    PrstHdrName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HdrPersistenceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HdrPersistenceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            PrstHdrName=json_data.get("PrstHdrName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HdrPersistenceProfileDefinition = HdrPersistenceProfileDefinition


@dataclass
class HttpCookiePersistenceProfileDefinition(BaseModel):
    AlwaysSendCookie: Optional[bool]
    CookieName: Optional[str]
    EncryptionKey: Optional[str]
    Timeout: Optional[float]
    Key: Optional[Sequence["_KeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpCookiePersistenceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpCookiePersistenceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AlwaysSendCookie=json_data.get("AlwaysSendCookie"),
            CookieName=json_data.get("CookieName"),
            EncryptionKey=json_data.get("EncryptionKey"),
            Timeout=json_data.get("Timeout"),
            Key=deserialize_list(json_data.get("Key"), KeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpCookiePersistenceProfileDefinition = HttpCookiePersistenceProfileDefinition


@dataclass
class KeyDefinition(BaseModel):
    AesKey: Optional[str]
    HmacKey: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDefinition"]:
        if not json_data:
            return None
        return cls(
            AesKey=json_data.get("AesKey"),
            HmacKey=json_data.get("HmacKey"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDefinition = KeyDefinition


@dataclass
class IpPersistenceProfileDefinition(BaseModel):
    IpMask: Optional[float]
    IpPersistentTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpPersistenceProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPersistenceProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            IpMask=json_data.get("IpMask"),
            IpPersistentTimeout=json_data.get("IpPersistentTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPersistenceProfileDefinition = IpPersistenceProfileDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


