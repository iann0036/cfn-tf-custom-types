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
    100ContWaitForReqComplete: Optional[float]
    BypassSg: Optional[str]
    ClientIpHdrReplace: Optional[float]
    ClientPortHdrReplace: Optional[float]
    CompressionAutoDisableOnHighCpu: Optional[float]
    CompressionEnable: Optional[float]
    CompressionKeepAcceptEncoding: Optional[float]
    CompressionKeepAcceptEncodingEnable: Optional[float]
    CompressionLevel: Optional[float]
    CompressionMinimumContentLength: Optional[float]
    CookieFormat: Optional[str]
    FailoverUrl: Optional[str]
    Id: Optional[str]
    InsertClientIp: Optional[float]
    InsertClientIpHeaderName: Optional[str]
    InsertClientPort: Optional[float]
    InsertClientPortHeaderName: Optional[str]
    KeepClientAlive: Optional[float]
    LogRetry: Optional[float]
    MaxConcurrentStreams: Optional[float]
    Name: Optional[str]
    NonHttpBypass: Optional[float]
    PersistOn401: Optional[float]
    RdPort: Optional[float]
    RdRespCode: Optional[str]
    RdSecure: Optional[float]
    RdSimpleLoc: Optional[str]
    Redirect: Optional[float]
    ReqHdrWaitTime: Optional[float]
    ReqHdrWaitTimeVal: Optional[float]
    RequestLineCaseInsensitive: Optional[float]
    RequestTimeout: Optional[float]
    RetryOn5xx: Optional[float]
    RetryOn5xxPerReq: Optional[float]
    RetryOn5xxPerReqVal: Optional[float]
    RetryOn5xxVal: Optional[float]
    StrictTransactionSwitch: Optional[float]
    Term11clientHdrConnClose: Optional[float]
    UrlHashFirst: Optional[float]
    UrlHashLast: Optional[float]
    UrlHashOffset: Optional[float]
    UrlHashPersist: Optional[float]
    UseServerStatus: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    CompressionContentType: Optional[Sequence["_CompressionContentTypeDefinition"]]
    CompressionExcludeContentType: Optional[Sequence["_CompressionExcludeContentTypeDefinition"]]
    CompressionExcludeUri: Optional[Sequence["_CompressionExcludeUriDefinition"]]
    HostSwitching: Optional[Sequence["_HostSwitchingDefinition"]]
    RedirectRewrite: Optional[Sequence["_RedirectRewriteDefinition"]]
    RequestHeaderEraseList: Optional[Sequence["_RequestHeaderEraseListDefinition"]]
    RequestHeaderInsertList: Optional[Sequence["_RequestHeaderInsertListDefinition"]]
    ResponseContentReplaceList: Optional[Sequence["_ResponseContentReplaceListDefinition"]]
    ResponseHeaderEraseList: Optional[Sequence["_ResponseHeaderEraseListDefinition"]]
    ResponseHeaderInsertList: Optional[Sequence["_ResponseHeaderInsertListDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]
    UrlSwitching: Optional[Sequence["_UrlSwitchingDefinition"]]

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
            100ContWaitForReqComplete=json_data.get("100ContWaitForReqComplete"),
            BypassSg=json_data.get("BypassSg"),
            ClientIpHdrReplace=json_data.get("ClientIpHdrReplace"),
            ClientPortHdrReplace=json_data.get("ClientPortHdrReplace"),
            CompressionAutoDisableOnHighCpu=json_data.get("CompressionAutoDisableOnHighCpu"),
            CompressionEnable=json_data.get("CompressionEnable"),
            CompressionKeepAcceptEncoding=json_data.get("CompressionKeepAcceptEncoding"),
            CompressionKeepAcceptEncodingEnable=json_data.get("CompressionKeepAcceptEncodingEnable"),
            CompressionLevel=json_data.get("CompressionLevel"),
            CompressionMinimumContentLength=json_data.get("CompressionMinimumContentLength"),
            CookieFormat=json_data.get("CookieFormat"),
            FailoverUrl=json_data.get("FailoverUrl"),
            Id=json_data.get("Id"),
            InsertClientIp=json_data.get("InsertClientIp"),
            InsertClientIpHeaderName=json_data.get("InsertClientIpHeaderName"),
            InsertClientPort=json_data.get("InsertClientPort"),
            InsertClientPortHeaderName=json_data.get("InsertClientPortHeaderName"),
            KeepClientAlive=json_data.get("KeepClientAlive"),
            LogRetry=json_data.get("LogRetry"),
            MaxConcurrentStreams=json_data.get("MaxConcurrentStreams"),
            Name=json_data.get("Name"),
            NonHttpBypass=json_data.get("NonHttpBypass"),
            PersistOn401=json_data.get("PersistOn401"),
            RdPort=json_data.get("RdPort"),
            RdRespCode=json_data.get("RdRespCode"),
            RdSecure=json_data.get("RdSecure"),
            RdSimpleLoc=json_data.get("RdSimpleLoc"),
            Redirect=json_data.get("Redirect"),
            ReqHdrWaitTime=json_data.get("ReqHdrWaitTime"),
            ReqHdrWaitTimeVal=json_data.get("ReqHdrWaitTimeVal"),
            RequestLineCaseInsensitive=json_data.get("RequestLineCaseInsensitive"),
            RequestTimeout=json_data.get("RequestTimeout"),
            RetryOn5xx=json_data.get("RetryOn5xx"),
            RetryOn5xxPerReq=json_data.get("RetryOn5xxPerReq"),
            RetryOn5xxPerReqVal=json_data.get("RetryOn5xxPerReqVal"),
            RetryOn5xxVal=json_data.get("RetryOn5xxVal"),
            StrictTransactionSwitch=json_data.get("StrictTransactionSwitch"),
            Term11clientHdrConnClose=json_data.get("Term11clientHdrConnClose"),
            UrlHashFirst=json_data.get("UrlHashFirst"),
            UrlHashLast=json_data.get("UrlHashLast"),
            UrlHashOffset=json_data.get("UrlHashOffset"),
            UrlHashPersist=json_data.get("UrlHashPersist"),
            UseServerStatus=json_data.get("UseServerStatus"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            CompressionContentType=deserialize_list(json_data.get("CompressionContentType"), CompressionContentTypeDefinition),
            CompressionExcludeContentType=deserialize_list(json_data.get("CompressionExcludeContentType"), CompressionExcludeContentTypeDefinition),
            CompressionExcludeUri=deserialize_list(json_data.get("CompressionExcludeUri"), CompressionExcludeUriDefinition),
            HostSwitching=deserialize_list(json_data.get("HostSwitching"), HostSwitchingDefinition),
            RedirectRewrite=deserialize_list(json_data.get("RedirectRewrite"), RedirectRewriteDefinition),
            RequestHeaderEraseList=deserialize_list(json_data.get("RequestHeaderEraseList"), RequestHeaderEraseListDefinition),
            RequestHeaderInsertList=deserialize_list(json_data.get("RequestHeaderInsertList"), RequestHeaderInsertListDefinition),
            ResponseContentReplaceList=deserialize_list(json_data.get("ResponseContentReplaceList"), ResponseContentReplaceListDefinition),
            ResponseHeaderEraseList=deserialize_list(json_data.get("ResponseHeaderEraseList"), ResponseHeaderEraseListDefinition),
            ResponseHeaderInsertList=deserialize_list(json_data.get("ResponseHeaderInsertList"), ResponseHeaderInsertListDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
            UrlSwitching=deserialize_list(json_data.get("UrlSwitching"), UrlSwitchingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CompressionContentTypeDefinition(BaseModel):
    ContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CompressionContentTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompressionContentTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompressionContentTypeDefinition = CompressionContentTypeDefinition


@dataclass
class CompressionExcludeContentTypeDefinition(BaseModel):
    ExcludeContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CompressionExcludeContentTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompressionExcludeContentTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludeContentType=json_data.get("ExcludeContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompressionExcludeContentTypeDefinition = CompressionExcludeContentTypeDefinition


@dataclass
class CompressionExcludeUriDefinition(BaseModel):
    ExcludeUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CompressionExcludeUriDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompressionExcludeUriDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludeUri=json_data.get("ExcludeUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompressionExcludeUriDefinition = CompressionExcludeUriDefinition


@dataclass
class HostSwitchingDefinition(BaseModel):
    HostMatchString: Optional[str]
    HostServiceGroup: Optional[str]
    HostSwitchingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostSwitchingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostSwitchingDefinition"]:
        if not json_data:
            return None
        return cls(
            HostMatchString=json_data.get("HostMatchString"),
            HostServiceGroup=json_data.get("HostServiceGroup"),
            HostSwitchingType=json_data.get("HostSwitchingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostSwitchingDefinition = HostSwitchingDefinition


@dataclass
class RedirectRewriteDefinition(BaseModel):
    RedirectSecure: Optional[float]
    RedirectSecurePort: Optional[float]
    MatchList: Optional[Sequence["_MatchListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectRewriteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectRewriteDefinition"]:
        if not json_data:
            return None
        return cls(
            RedirectSecure=json_data.get("RedirectSecure"),
            RedirectSecurePort=json_data.get("RedirectSecurePort"),
            MatchList=deserialize_list(json_data.get("MatchList"), MatchListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectRewriteDefinition = RedirectRewriteDefinition


@dataclass
class MatchListDefinition(BaseModel):
    RedirectMatch: Optional[str]
    RewriteTo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchListDefinition"]:
        if not json_data:
            return None
        return cls(
            RedirectMatch=json_data.get("RedirectMatch"),
            RewriteTo=json_data.get("RewriteTo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchListDefinition = MatchListDefinition


@dataclass
class RequestHeaderEraseListDefinition(BaseModel):
    RequestHeaderErase: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderEraseListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderEraseListDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestHeaderErase=json_data.get("RequestHeaderErase"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderEraseListDefinition = RequestHeaderEraseListDefinition


@dataclass
class RequestHeaderInsertListDefinition(BaseModel):
    RequestHeaderInsert: Optional[str]
    RequestHeaderInsertType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderInsertListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderInsertListDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestHeaderInsert=json_data.get("RequestHeaderInsert"),
            RequestHeaderInsertType=json_data.get("RequestHeaderInsertType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderInsertListDefinition = RequestHeaderInsertListDefinition


@dataclass
class ResponseContentReplaceListDefinition(BaseModel):
    ResponseContentReplace: Optional[str]
    ResponseNewString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseContentReplaceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseContentReplaceListDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseContentReplace=json_data.get("ResponseContentReplace"),
            ResponseNewString=json_data.get("ResponseNewString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseContentReplaceListDefinition = ResponseContentReplaceListDefinition


@dataclass
class ResponseHeaderEraseListDefinition(BaseModel):
    ResponseHeaderErase: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeaderEraseListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeaderEraseListDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseHeaderErase=json_data.get("ResponseHeaderErase"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeaderEraseListDefinition = ResponseHeaderEraseListDefinition


@dataclass
class ResponseHeaderInsertListDefinition(BaseModel):
    ResponseHeaderInsert: Optional[str]
    ResponseHeaderInsertType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeaderInsertListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeaderInsertListDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponseHeaderInsert=json_data.get("ResponseHeaderInsert"),
            ResponseHeaderInsertType=json_data.get("ResponseHeaderInsertType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeaderInsertListDefinition = ResponseHeaderInsertListDefinition


@dataclass
class TemplateDefinition(BaseModel):
    Logging: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Logging=json_data.get("Logging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


@dataclass
class UrlSwitchingDefinition(BaseModel):
    UrlMatchString: Optional[str]
    UrlServiceGroup: Optional[str]
    UrlSwitchingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlSwitchingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlSwitchingDefinition"]:
        if not json_data:
            return None
        return cls(
            UrlMatchString=json_data.get("UrlMatchString"),
            UrlServiceGroup=json_data.get("UrlServiceGroup"),
            UrlSwitchingType=json_data.get("UrlSwitchingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlSwitchingDefinition = UrlSwitchingDefinition


