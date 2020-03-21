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
    Description: Optional[str]
    DisplayName: Optional[str]
    MatchStrategy: Optional[str]
    Revision: Optional[float]
    BodyCondition: Optional[Sequence["_BodyCondition"]]
    CookieCondition: Optional[Sequence["_CookieCondition"]]
    HeaderCondition: Optional[Sequence["_HeaderCondition"]]
    HttpRedirectAction: Optional[Sequence["_HttpRedirectAction"]]
    HttpRejectAction: Optional[Sequence["_HttpRejectAction"]]
    IpCondition: Optional[Sequence["_IpCondition"]]
    MethodCondition: Optional[Sequence["_MethodCondition"]]
    SelectPoolAction: Optional[Sequence["_SelectPoolAction"]]
    Tag: Optional[Sequence["_Tag"]]
    TcpCondition: Optional[Sequence["_TcpCondition"]]
    UriCondition: Optional[Sequence["_UriCondition"]]
    VersionCondition: Optional[Sequence["_VersionCondition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            MatchStrategy=json_data.get("MatchStrategy"),
            Revision=json_data.get("Revision"),
            BodyCondition=json_data.get("BodyCondition"),
            CookieCondition=json_data.get("CookieCondition"),
            HeaderCondition=json_data.get("HeaderCondition"),
            HttpRedirectAction=json_data.get("HttpRedirectAction"),
            HttpRejectAction=json_data.get("HttpRejectAction"),
            IpCondition=json_data.get("IpCondition"),
            MethodCondition=json_data.get("MethodCondition"),
            SelectPoolAction=json_data.get("SelectPoolAction"),
            Tag=json_data.get("Tag"),
            TcpCondition=json_data.get("TcpCondition"),
            UriCondition=json_data.get("UriCondition"),
            VersionCondition=json_data.get("VersionCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BodyCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BodyCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyCondition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyCondition = BodyCondition


@dataclass
class CookieCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CookieCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieCondition"]:
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
_CookieCondition = CookieCondition


@dataclass
class HeaderCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderCondition"]:
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
_HeaderCondition = HeaderCondition


@dataclass
class HttpRedirectAction:
    RedirectStatus: Optional[str]
    RedirectUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRedirectAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRedirectAction"]:
        if not json_data:
            return None
        return cls(
            RedirectStatus=json_data.get("RedirectStatus"),
            RedirectUrl=json_data.get("RedirectUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRedirectAction = HttpRedirectAction


@dataclass
class HttpRejectAction:
    ReplyMessage: Optional[str]
    ReplyStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRejectAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRejectAction"]:
        if not json_data:
            return None
        return cls(
            ReplyMessage=json_data.get("ReplyMessage"),
            ReplyStatus=json_data.get("ReplyStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRejectAction = HttpRejectAction


@dataclass
class IpCondition:
    Inverse: Optional[bool]
    SourceAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpCondition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            SourceAddress=json_data.get("SourceAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpCondition = IpCondition


@dataclass
class MethodCondition:
    Inverse: Optional[bool]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodCondition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodCondition = MethodCondition


@dataclass
class SelectPoolAction:
    PoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectPoolAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectPoolAction"]:
        if not json_data:
            return None
        return cls(
            PoolId=json_data.get("PoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectPoolAction = SelectPoolAction


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class TcpCondition:
    Inverse: Optional[bool]
    SourcePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpCondition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpCondition = TcpCondition


@dataclass
class UriCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UriCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriCondition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriCondition = UriCondition


@dataclass
class VersionCondition:
    Inverse: Optional[bool]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionCondition"]:
        if not json_data:
            return None
        return cls(
            Inverse=json_data.get("Inverse"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionCondition = VersionCondition


