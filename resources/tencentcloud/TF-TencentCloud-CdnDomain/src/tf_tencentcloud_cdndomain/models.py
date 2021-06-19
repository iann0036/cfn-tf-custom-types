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
    Area: Optional[str]
    Cname: Optional[str]
    CreateTime: Optional[str]
    Domain: Optional[str]
    FullUrlCache: Optional[bool]
    Id: Optional[str]
    ProjectId: Optional[float]
    RangeOriginSwitch: Optional[str]
    ServiceType: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    HttpsConfig: Optional[Sequence["_HttpsConfigDefinition"]]
    Origin: Optional[Sequence["_OriginDefinition"]]
    RequestHeader: Optional[Sequence["_RequestHeaderDefinition"]]
    RuleCache: Optional[Sequence["_RuleCacheDefinition"]]

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
            Area=json_data.get("Area"),
            Cname=json_data.get("Cname"),
            CreateTime=json_data.get("CreateTime"),
            Domain=json_data.get("Domain"),
            FullUrlCache=json_data.get("FullUrlCache"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            RangeOriginSwitch=json_data.get("RangeOriginSwitch"),
            ServiceType=json_data.get("ServiceType"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            HttpsConfig=deserialize_list(json_data.get("HttpsConfig"), HttpsConfigDefinition),
            Origin=deserialize_list(json_data.get("Origin"), OriginDefinition),
            RequestHeader=deserialize_list(json_data.get("RequestHeader"), RequestHeaderDefinition),
            RuleCache=deserialize_list(json_data.get("RuleCache"), RuleCacheDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class HttpsConfigDefinition(BaseModel):
    Http2Switch: Optional[str]
    HttpsSwitch: Optional[str]
    OcspStaplingSwitch: Optional[str]
    SpdySwitch: Optional[str]
    VerifyClient: Optional[str]
    ClientCertificateConfig: Optional[Sequence["_ClientCertificateConfigDefinition"]]
    ForceRedirect: Optional[Sequence["_ForceRedirectDefinition"]]
    ServerCertificateConfig: Optional[Sequence["_ServerCertificateConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Http2Switch=json_data.get("Http2Switch"),
            HttpsSwitch=json_data.get("HttpsSwitch"),
            OcspStaplingSwitch=json_data.get("OcspStaplingSwitch"),
            SpdySwitch=json_data.get("SpdySwitch"),
            VerifyClient=json_data.get("VerifyClient"),
            ClientCertificateConfig=deserialize_list(json_data.get("ClientCertificateConfig"), ClientCertificateConfigDefinition),
            ForceRedirect=deserialize_list(json_data.get("ForceRedirect"), ForceRedirectDefinition),
            ServerCertificateConfig=deserialize_list(json_data.get("ServerCertificateConfig"), ServerCertificateConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsConfigDefinition = HttpsConfigDefinition


@dataclass
class ClientCertificateConfigDefinition(BaseModel):
    CertificateContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientCertificateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientCertificateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateContent=json_data.get("CertificateContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientCertificateConfigDefinition = ClientCertificateConfigDefinition


@dataclass
class ForceRedirectDefinition(BaseModel):
    RedirectStatusCode: Optional[float]
    RedirectType: Optional[str]
    Switch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForceRedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForceRedirectDefinition"]:
        if not json_data:
            return None
        return cls(
            RedirectStatusCode=json_data.get("RedirectStatusCode"),
            RedirectType=json_data.get("RedirectType"),
            Switch=json_data.get("Switch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForceRedirectDefinition = ForceRedirectDefinition


@dataclass
class ServerCertificateConfigDefinition(BaseModel):
    CertificateContent: Optional[str]
    CertificateId: Optional[str]
    Message: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCertificateConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCertificateConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateContent=json_data.get("CertificateContent"),
            CertificateId=json_data.get("CertificateId"),
            Message=json_data.get("Message"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCertificateConfigDefinition = ServerCertificateConfigDefinition


@dataclass
class OriginDefinition(BaseModel):
    BackupOriginList: Optional[Sequence[str]]
    BackupOriginType: Optional[str]
    BackupServerName: Optional[str]
    CosPrivateAccess: Optional[str]
    OriginList: Optional[Sequence[str]]
    OriginPullProtocol: Optional[str]
    OriginType: Optional[str]
    ServerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginDefinition"]:
        if not json_data:
            return None
        return cls(
            BackupOriginList=json_data.get("BackupOriginList"),
            BackupOriginType=json_data.get("BackupOriginType"),
            BackupServerName=json_data.get("BackupServerName"),
            CosPrivateAccess=json_data.get("CosPrivateAccess"),
            OriginList=json_data.get("OriginList"),
            OriginPullProtocol=json_data.get("OriginPullProtocol"),
            OriginType=json_data.get("OriginType"),
            ServerName=json_data.get("ServerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginDefinition = OriginDefinition


@dataclass
class RequestHeaderDefinition(BaseModel):
    Switch: Optional[str]
    HeaderRules: Optional[Sequence["_HeaderRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Switch=json_data.get("Switch"),
            HeaderRules=deserialize_list(json_data.get("HeaderRules"), HeaderRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderDefinition = RequestHeaderDefinition


@dataclass
class HeaderRulesDefinition(BaseModel):
    HeaderMode: Optional[str]
    HeaderName: Optional[str]
    HeaderValue: Optional[str]
    RulePaths: Optional[Sequence[str]]
    RuleType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderMode=json_data.get("HeaderMode"),
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
            RulePaths=json_data.get("RulePaths"),
            RuleType=json_data.get("RuleType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderRulesDefinition = HeaderRulesDefinition


@dataclass
class RuleCacheDefinition(BaseModel):
    CacheTime: Optional[float]
    CompareMaxAge: Optional[str]
    FollowOriginSwitch: Optional[str]
    IgnoreCacheControl: Optional[str]
    IgnoreSetCookie: Optional[str]
    NoCacheSwitch: Optional[str]
    ReValidate: Optional[str]
    RulePaths: Optional[Sequence[str]]
    RuleType: Optional[str]
    Switch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleCacheDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleCacheDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheTime=json_data.get("CacheTime"),
            CompareMaxAge=json_data.get("CompareMaxAge"),
            FollowOriginSwitch=json_data.get("FollowOriginSwitch"),
            IgnoreCacheControl=json_data.get("IgnoreCacheControl"),
            IgnoreSetCookie=json_data.get("IgnoreSetCookie"),
            NoCacheSwitch=json_data.get("NoCacheSwitch"),
            ReValidate=json_data.get("ReValidate"),
            RulePaths=json_data.get("RulePaths"),
            RuleType=json_data.get("RuleType"),
            Switch=json_data.get("Switch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleCacheDefinition = RuleCacheDefinition


