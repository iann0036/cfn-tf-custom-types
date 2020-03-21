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
    BlockIps: Optional[Sequence[str]]
    CdnType: Optional[str]
    DomainName: Optional[str]
    OptimizeEnable: Optional[str]
    PageCompressEnable: Optional[str]
    RangeEnable: Optional[str]
    Scope: Optional[str]
    SourcePort: Optional[float]
    SourceType: Optional[str]
    Sources: Optional[Sequence[str]]
    VideoSeekEnable: Optional[str]
    AuthConfig: Optional[Sequence["_AuthConfig"]]
    CacheConfig: Optional[Sequence["_CacheConfig"]]
    CertificateConfig: Optional[Sequence["_CertificateConfig"]]
    HttpHeaderConfig: Optional[Sequence["_HttpHeaderConfig"]]
    Page404Config: Optional[Sequence["_Page404Config"]]
    ParameterFilterConfig: Optional[Sequence["_ParameterFilterConfig"]]
    ReferConfig: Optional[Sequence["_ReferConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BlockIps=json_data.get("BlockIps"),
            CdnType=json_data.get("CdnType"),
            DomainName=json_data.get("DomainName"),
            OptimizeEnable=json_data.get("OptimizeEnable"),
            PageCompressEnable=json_data.get("PageCompressEnable"),
            RangeEnable=json_data.get("RangeEnable"),
            Scope=json_data.get("Scope"),
            SourcePort=json_data.get("SourcePort"),
            SourceType=json_data.get("SourceType"),
            Sources=json_data.get("Sources"),
            VideoSeekEnable=json_data.get("VideoSeekEnable"),
            AuthConfig=json_data.get("AuthConfig"),
            CacheConfig=json_data.get("CacheConfig"),
            CertificateConfig=json_data.get("CertificateConfig"),
            HttpHeaderConfig=json_data.get("HttpHeaderConfig"),
            Page404Config=json_data.get("Page404Config"),
            ParameterFilterConfig=json_data.get("ParameterFilterConfig"),
            ReferConfig=json_data.get("ReferConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthConfig:
    AuthType: Optional[str]
    MasterKey: Optional[str]
    SlaveKey: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AuthConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthConfig"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            MasterKey=json_data.get("MasterKey"),
            SlaveKey=json_data.get("SlaveKey"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthConfig = AuthConfig


@dataclass
class CacheConfig:
    CacheContent: Optional[str]
    CacheType: Optional[str]
    Ttl: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheConfig"]:
        if not json_data:
            return None
        return cls(
            CacheContent=json_data.get("CacheContent"),
            CacheType=json_data.get("CacheType"),
            Ttl=json_data.get("Ttl"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheConfig = CacheConfig


@dataclass
class CertificateConfig:
    PrivateKey: Optional[str]
    ServerCertificate: Optional[str]
    ServerCertificateStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateConfig"]:
        if not json_data:
            return None
        return cls(
            PrivateKey=json_data.get("PrivateKey"),
            ServerCertificate=json_data.get("ServerCertificate"),
            ServerCertificateStatus=json_data.get("ServerCertificateStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateConfig = CertificateConfig


@dataclass
class HttpHeaderConfig:
    HeaderKey: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderConfig"]:
        if not json_data:
            return None
        return cls(
            HeaderKey=json_data.get("HeaderKey"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderConfig = HttpHeaderConfig


@dataclass
class Page404Config:
    CustomPageUrl: Optional[str]
    PageType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Page404Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Page404Config"]:
        if not json_data:
            return None
        return cls(
            CustomPageUrl=json_data.get("CustomPageUrl"),
            PageType=json_data.get("PageType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Page404Config = Page404Config


@dataclass
class ParameterFilterConfig:
    Enable: Optional[str]
    HashKeyArgs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterFilterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterFilterConfig"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            HashKeyArgs=json_data.get("HashKeyArgs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterFilterConfig = ParameterFilterConfig


@dataclass
class ReferConfig:
    AllowEmpty: Optional[str]
    ReferList: Optional[Sequence[str]]
    ReferType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferConfig"]:
        if not json_data:
            return None
        return cls(
            AllowEmpty=json_data.get("AllowEmpty"),
            ReferList=json_data.get("ReferList"),
            ReferType=json_data.get("ReferType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferConfig = ReferConfig


