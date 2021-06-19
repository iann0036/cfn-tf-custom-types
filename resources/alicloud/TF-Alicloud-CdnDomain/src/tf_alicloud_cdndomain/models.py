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
    BlockIps: Optional[Sequence[str]]
    CdnType: Optional[str]
    DomainName: Optional[str]
    Id: Optional[str]
    OptimizeEnable: Optional[str]
    PageCompressEnable: Optional[str]
    RangeEnable: Optional[str]
    Scope: Optional[str]
    SourcePort: Optional[float]
    SourceType: Optional[str]
    Sources: Optional[Sequence[str]]
    VideoSeekEnable: Optional[str]
    AuthConfig: Optional[Sequence["_AuthConfigDefinition"]]
    CacheConfig: Optional[Sequence["_CacheConfigDefinition"]]
    CertificateConfig: Optional[Sequence["_CertificateConfigDefinition"]]
    HttpHeaderConfig: Optional[Sequence["_HttpHeaderConfigDefinition"]]
    Page404Config: Optional[Sequence["_Page404ConfigDefinition"]]
    ParameterFilterConfig: Optional[Sequence["_ParameterFilterConfigDefinition"]]
    ReferConfig: Optional[Sequence["_ReferConfigDefinition"]]

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
            BlockIps=json_data.get("BlockIps"),
            CdnType=json_data.get("CdnType"),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            OptimizeEnable=json_data.get("OptimizeEnable"),
            PageCompressEnable=json_data.get("PageCompressEnable"),
            RangeEnable=json_data.get("RangeEnable"),
            Scope=json_data.get("Scope"),
            SourcePort=json_data.get("SourcePort"),
            SourceType=json_data.get("SourceType"),
            Sources=json_data.get("Sources"),
            VideoSeekEnable=json_data.get("VideoSeekEnable"),
            AuthConfig=deserialize_list(json_data.get("AuthConfig"), AuthConfigDefinition),
            CacheConfig=deserialize_list(json_data.get("CacheConfig"), CacheConfigDefinition),
            CertificateConfig=deserialize_list(json_data.get("CertificateConfig"), CertificateConfigDefinition),
            HttpHeaderConfig=deserialize_list(json_data.get("HttpHeaderConfig"), HttpHeaderConfigDefinition),
            Page404Config=deserialize_list(json_data.get("Page404Config"), Page404ConfigDefinition),
            ParameterFilterConfig=deserialize_list(json_data.get("ParameterFilterConfig"), ParameterFilterConfigDefinition),
            ReferConfig=deserialize_list(json_data.get("ReferConfig"), ReferConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthConfigDefinition(BaseModel):
    AuthType: Optional[str]
    MasterKey: Optional[str]
    SlaveKey: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AuthConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            MasterKey=json_data.get("MasterKey"),
            SlaveKey=json_data.get("SlaveKey"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthConfigDefinition = AuthConfigDefinition


@dataclass
class CacheConfigDefinition(BaseModel):
    CacheContent: Optional[str]
    CacheType: Optional[str]
    Ttl: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheContent=json_data.get("CacheContent"),
            CacheType=json_data.get("CacheType"),
            Ttl=json_data.get("Ttl"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheConfigDefinition = CacheConfigDefinition


@dataclass
class CertificateConfigDefinition(BaseModel):
    PrivateKey: Optional[str]
    ServerCertificate: Optional[str]
    ServerCertificateStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PrivateKey=json_data.get("PrivateKey"),
            ServerCertificate=json_data.get("ServerCertificate"),
            ServerCertificateStatus=json_data.get("ServerCertificateStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateConfigDefinition = CertificateConfigDefinition


@dataclass
class HttpHeaderConfigDefinition(BaseModel):
    HeaderKey: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderKey=json_data.get("HeaderKey"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderConfigDefinition = HttpHeaderConfigDefinition


@dataclass
class Page404ConfigDefinition(BaseModel):
    CustomPageUrl: Optional[str]
    PageType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Page404ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Page404ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomPageUrl=json_data.get("CustomPageUrl"),
            PageType=json_data.get("PageType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Page404ConfigDefinition = Page404ConfigDefinition


@dataclass
class ParameterFilterConfigDefinition(BaseModel):
    Enable: Optional[str]
    HashKeyArgs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterFilterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterFilterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            HashKeyArgs=json_data.get("HashKeyArgs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterFilterConfigDefinition = ParameterFilterConfigDefinition


@dataclass
class ReferConfigDefinition(BaseModel):
    AllowEmpty: Optional[str]
    ReferList: Optional[Sequence[str]]
    ReferType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowEmpty=json_data.get("AllowEmpty"),
            ReferList=json_data.get("ReferList"),
            ReferType=json_data.get("ReferType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferConfigDefinition = ReferConfigDefinition


