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
    DisplayName: Optional[str]
    Id: Optional[str]
    MatchStrategy: Optional[str]
    Revision: Optional[float]
    BodyCondition: Optional[Sequence["_BodyConditionDefinition"]]
    CookieCondition: Optional[Sequence["_CookieConditionDefinition"]]
    HeaderCondition: Optional[Sequence["_HeaderConditionDefinition"]]
    HttpRedirectAction: Optional[Sequence["_HttpRedirectActionDefinition"]]
    HttpRejectAction: Optional[Sequence["_HttpRejectActionDefinition"]]
    IpCondition: Optional[Sequence["_IpConditionDefinition"]]
    MethodCondition: Optional[Sequence["_MethodConditionDefinition"]]
    SelectPoolAction: Optional[Sequence["_SelectPoolActionDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    TcpCondition: Optional[Sequence["_TcpConditionDefinition"]]
    UriCondition: Optional[Sequence["_UriConditionDefinition"]]
    VersionCondition: Optional[Sequence["_VersionConditionDefinition"]]

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
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MatchStrategy=json_data.get("MatchStrategy"),
            Revision=json_data.get("Revision"),
            BodyCondition=deserialize_list(json_data.get("BodyCondition"), BodyConditionDefinition),
            CookieCondition=deserialize_list(json_data.get("CookieCondition"), CookieConditionDefinition),
            HeaderCondition=deserialize_list(json_data.get("HeaderCondition"), HeaderConditionDefinition),
            HttpRedirectAction=deserialize_list(json_data.get("HttpRedirectAction"), HttpRedirectActionDefinition),
            HttpRejectAction=deserialize_list(json_data.get("HttpRejectAction"), HttpRejectActionDefinition),
            IpCondition=deserialize_list(json_data.get("IpCondition"), IpConditionDefinition),
            MethodCondition=deserialize_list(json_data.get("MethodCondition"), MethodConditionDefinition),
            SelectPoolAction=deserialize_list(json_data.get("SelectPoolAction"), SelectPoolActionDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            TcpCondition=deserialize_list(json_data.get("TcpCondition"), TcpConditionDefinition),
            UriCondition=deserialize_list(json_data.get("UriCondition"), UriConditionDefinition),
            VersionCondition=deserialize_list(json_data.get("VersionCondition"), VersionConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BodyConditionDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BodyConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyConditionDefinition = BodyConditionDefinition


@dataclass
class CookieConditionDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CookieConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieConditionDefinition = CookieConditionDefinition


@dataclass
class HeaderConditionDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderConditionDefinition = HeaderConditionDefinition


@dataclass
class HttpRedirectActionDefinition(BaseModel):
    RedirectStatus: Optional[str]
    RedirectUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRedirectActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRedirectActionDefinition"]:
        if not json_data:
            return None
        return cls(
            RedirectStatus=json_data.get("RedirectStatus"),
            RedirectUrl=json_data.get("RedirectUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRedirectActionDefinition = HttpRedirectActionDefinition


@dataclass
class HttpRejectActionDefinition(BaseModel):
    ReplyMessage: Optional[str]
    ReplyStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRejectActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRejectActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ReplyMessage=json_data.get("ReplyMessage"),
            ReplyStatus=json_data.get("ReplyStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRejectActionDefinition = HttpRejectActionDefinition


@dataclass
class IpConditionDefinition(BaseModel):
    Inverse: Optional[bool]
    SourceAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            SourceAddress=json_data.get("SourceAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConditionDefinition = IpConditionDefinition


@dataclass
class MethodConditionDefinition(BaseModel):
    Inverse: Optional[bool]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodConditionDefinition = MethodConditionDefinition


@dataclass
class SelectPoolActionDefinition(BaseModel):
    PoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectPoolActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectPoolActionDefinition"]:
        if not json_data:
            return None
        return cls(
            PoolId=json_data.get("PoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectPoolActionDefinition = SelectPoolActionDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class TcpConditionDefinition(BaseModel):
    Inverse: Optional[bool]
    SourcePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpConditionDefinition = TcpConditionDefinition


@dataclass
class UriConditionDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UriConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriConditionDefinition = UriConditionDefinition


@dataclass
class VersionConditionDefinition(BaseModel):
    Inverse: Optional[bool]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionConditionDefinition = VersionConditionDefinition


