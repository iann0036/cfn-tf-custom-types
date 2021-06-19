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
    Facility: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    IncludeDestFqdn: Optional[float]
    MergedStyle: Optional[float]
    Name: Optional[str]
    Resolution: Optional[str]
    ServiceGroup: Optional[str]
    Severity: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    IncludeHttp: Optional[Sequence["_IncludeHttpDefinition"]]
    IncludeRadiusAttribute: Optional[Sequence["_IncludeRadiusAttributeDefinition"]]
    Log: Optional[Sequence["_LogDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]
    SourceAddress: Optional[Sequence["_SourceAddressDefinition"]]

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
            Facility=json_data.get("Facility"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            IncludeDestFqdn=json_data.get("IncludeDestFqdn"),
            MergedStyle=json_data.get("MergedStyle"),
            Name=json_data.get("Name"),
            Resolution=json_data.get("Resolution"),
            ServiceGroup=json_data.get("ServiceGroup"),
            Severity=json_data.get("Severity"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            IncludeHttp=deserialize_list(json_data.get("IncludeHttp"), IncludeHttpDefinition),
            IncludeRadiusAttribute=deserialize_list(json_data.get("IncludeRadiusAttribute"), IncludeRadiusAttributeDefinition),
            Log=deserialize_list(json_data.get("Log"), LogDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            SourceAddress=deserialize_list(json_data.get("SourceAddress"), SourceAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IncludeHttpDefinition(BaseModel):
    FileExtension: Optional[float]
    L4SessionInfo: Optional[float]
    Method: Optional[float]
    RequestNumber: Optional[float]
    HeaderCfg: Optional[Sequence["_HeaderCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncludeHttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludeHttpDefinition"]:
        if not json_data:
            return None
        return cls(
            FileExtension=json_data.get("FileExtension"),
            L4SessionInfo=json_data.get("L4SessionInfo"),
            Method=json_data.get("Method"),
            RequestNumber=json_data.get("RequestNumber"),
            HeaderCfg=deserialize_list(json_data.get("HeaderCfg"), HeaderCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludeHttpDefinition = IncludeHttpDefinition


@dataclass
class HeaderCfgDefinition(BaseModel):
    CustomHeaderName: Optional[str]
    CustomMaxLength: Optional[float]
    HttpHeader: Optional[str]
    MaxLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomHeaderName=json_data.get("CustomHeaderName"),
            CustomMaxLength=json_data.get("CustomMaxLength"),
            HttpHeader=json_data.get("HttpHeader"),
            MaxLength=json_data.get("MaxLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderCfgDefinition = HeaderCfgDefinition


@dataclass
class IncludeRadiusAttributeDefinition(BaseModel):
    FramedIpv6Prefix: Optional[float]
    InsertIfNotExisting: Optional[float]
    NoQuote: Optional[float]
    PrefixLength: Optional[str]
    ZeroInCustomAttr: Optional[float]
    AttrCfg: Optional[Sequence["_AttrCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncludeRadiusAttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludeRadiusAttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            FramedIpv6Prefix=json_data.get("FramedIpv6Prefix"),
            InsertIfNotExisting=json_data.get("InsertIfNotExisting"),
            NoQuote=json_data.get("NoQuote"),
            PrefixLength=json_data.get("PrefixLength"),
            ZeroInCustomAttr=json_data.get("ZeroInCustomAttr"),
            AttrCfg=deserialize_list(json_data.get("AttrCfg"), AttrCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludeRadiusAttributeDefinition = IncludeRadiusAttributeDefinition


@dataclass
class AttrCfgDefinition(BaseModel):
    Attr: Optional[str]
    AttrEvent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttrCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttrCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Attr=json_data.get("Attr"),
            AttrEvent=json_data.get("AttrEvent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttrCfgDefinition = AttrCfgDefinition


@dataclass
class LogDefinition(BaseModel):
    HttpRequests: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpRequests=json_data.get("HttpRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDefinition = LogDefinition


@dataclass
class RuleDefinition(BaseModel):
    RuleHttpRequests: Optional[Sequence["_RuleHttpRequestsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            RuleHttpRequests=deserialize_list(json_data.get("RuleHttpRequests"), RuleHttpRequestsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class RuleHttpRequestsDefinition(BaseModel):
    DisableSequenceCheck: Optional[float]
    IncludeAllHeaders: Optional[float]
    LogEveryHttpRequest: Optional[float]
    MaxUrlLen: Optional[float]
    DestPort: Optional[Sequence["_DestPortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleHttpRequestsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleHttpRequestsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableSequenceCheck=json_data.get("DisableSequenceCheck"),
            IncludeAllHeaders=json_data.get("IncludeAllHeaders"),
            LogEveryHttpRequest=json_data.get("LogEveryHttpRequest"),
            MaxUrlLen=json_data.get("MaxUrlLen"),
            DestPort=deserialize_list(json_data.get("DestPort"), DestPortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleHttpRequestsDefinition = RuleHttpRequestsDefinition


@dataclass
class DestPortDefinition(BaseModel):
    DestPortNumber: Optional[float]
    IncludeByteCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DestPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestPortDefinition"]:
        if not json_data:
            return None
        return cls(
            DestPortNumber=json_data.get("DestPortNumber"),
            IncludeByteCount=json_data.get("IncludeByteCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestPortDefinition = DestPortDefinition


@dataclass
class SourceAddressDefinition(BaseModel):
    Ip: Optional[str]
    Ipv6: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Ipv6=json_data.get("Ipv6"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAddressDefinition = SourceAddressDefinition


