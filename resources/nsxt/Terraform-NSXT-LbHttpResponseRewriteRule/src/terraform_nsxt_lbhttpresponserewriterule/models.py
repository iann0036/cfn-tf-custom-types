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
    CookieCondition: Optional[Sequence["_CookieCondition"]]
    HeaderRewriteAction: Optional[Sequence["_HeaderRewriteAction"]]
    IpCondition: Optional[Sequence["_IpCondition"]]
    MethodCondition: Optional[Sequence["_MethodCondition"]]
    RequestHeaderCondition: Optional[Sequence["_RequestHeaderCondition"]]
    ResponseHeaderCondition: Optional[Sequence["_ResponseHeaderCondition"]]
    Tag: Optional[Sequence["_Tag"]]
    TcpCondition: Optional[Sequence["_TcpCondition"]]
    UriArgumentsCondition: Optional[Sequence["_UriArgumentsCondition"]]
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
            CookieCondition=json_data.get("CookieCondition"),
            HeaderRewriteAction=json_data.get("HeaderRewriteAction"),
            IpCondition=json_data.get("IpCondition"),
            MethodCondition=json_data.get("MethodCondition"),
            RequestHeaderCondition=json_data.get("RequestHeaderCondition"),
            ResponseHeaderCondition=json_data.get("ResponseHeaderCondition"),
            Tag=json_data.get("Tag"),
            TcpCondition=json_data.get("TcpCondition"),
            UriArgumentsCondition=json_data.get("UriArgumentsCondition"),
            UriCondition=json_data.get("UriCondition"),
            VersionCondition=json_data.get("VersionCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class HeaderRewriteAction:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderRewriteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderRewriteAction"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderRewriteAction = HeaderRewriteAction


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
class RequestHeaderCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderCondition"]:
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
_RequestHeaderCondition = RequestHeaderCondition


@dataclass
class ResponseHeaderCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeaderCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeaderCondition"]:
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
_ResponseHeaderCondition = ResponseHeaderCondition


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
class UriArgumentsCondition:
    CaseSensitive: Optional[bool]
    Inverse: Optional[bool]
    MatchType: Optional[str]
    UriArguments: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UriArgumentsCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriArgumentsCondition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            Inverse=json_data.get("Inverse"),
            MatchType=json_data.get("MatchType"),
            UriArguments=json_data.get("UriArguments"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriArgumentsCondition = UriArgumentsCondition


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


