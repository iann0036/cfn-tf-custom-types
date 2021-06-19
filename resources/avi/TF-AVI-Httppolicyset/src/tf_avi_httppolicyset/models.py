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
    CloudConfigCksum: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpReputationDbRef: Optional[str]
    IsInternalPolicy: Optional[bool]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    HttpRequestPolicy: Optional[Sequence["_HttpRequestPolicyDefinition"]]
    HttpResponsePolicy: Optional[Sequence["_HttpResponsePolicyDefinition"]]
    HttpSecurityPolicy: Optional[Sequence["_HttpSecurityPolicyDefinition"]]
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
            CloudConfigCksum=json_data.get("CloudConfigCksum"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpReputationDbRef=json_data.get("IpReputationDbRef"),
            IsInternalPolicy=json_data.get("IsInternalPolicy"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            HttpRequestPolicy=deserialize_list(json_data.get("HttpRequestPolicy"), HttpRequestPolicyDefinition),
            HttpResponsePolicy=deserialize_list(json_data.get("HttpResponsePolicy"), HttpResponsePolicyDefinition),
            HttpSecurityPolicy=deserialize_list(json_data.get("HttpSecurityPolicy"), HttpSecurityPolicyDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HttpRequestPolicyDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRequestPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRequestPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRequestPolicyDefinition = HttpRequestPolicyDefinition


@dataclass
class RulesDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Log: Optional[bool]
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ActionDefinition(BaseModel):
    StatusCode: Optional[str]
    Type: Optional[str]
    File: Optional[Sequence["_FileDefinition"]]
    Redirect: Optional[Sequence["_RedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            Type=json_data.get("Type"),
            File=deserialize_list(json_data.get("File"), FileDefinition),
            Redirect=deserialize_list(json_data.get("Redirect"), RedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class FileDefinition(BaseModel):
    ContentType: Optional[str]
    FileContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            FileContent=json_data.get("FileContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileDefinition = FileDefinition


@dataclass
class RedirectDefinition(BaseModel):
    KeepQuery: Optional[bool]
    Port: Optional[float]
    Protocol: Optional[str]
    StatusCode: Optional[str]
    Host: Optional[Sequence["_HostDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectDefinition"]:
        if not json_data:
            return None
        return cls(
            KeepQuery=json_data.get("KeepQuery"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            StatusCode=json_data.get("StatusCode"),
            Host=deserialize_list(json_data.get("Host"), HostDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectDefinition = RedirectDefinition


@dataclass
class HostDefinition(BaseModel):
    Type: Optional[str]
    Tokens: Optional[Sequence["_TokensDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Tokens=deserialize_list(json_data.get("Tokens"), TokensDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostDefinition = HostDefinition


@dataclass
class TokensDefinition(BaseModel):
    EndIndex: Optional[float]
    StartIndex: Optional[float]
    StrValue: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TokensDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokensDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIndex=json_data.get("EndIndex"),
            StartIndex=json_data.get("StartIndex"),
            StrValue=json_data.get("StrValue"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokensDefinition = TokensDefinition


@dataclass
class PathDefinition(BaseModel):
    Type: Optional[str]
    Tokens: Optional[Sequence["_TokensDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Tokens=deserialize_list(json_data.get("Tokens"), TokensDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class MatchDefinition(BaseModel):
    ClientIp: Optional[Sequence["_ClientIpDefinition"]]
    Cookie: Optional[Sequence["_CookieDefinition"]]
    Hdrs: Optional[Sequence["_HdrsDefinition"]]
    HostHdr: Optional[Sequence["_HostHdrDefinition"]]
    IpReputationType: Optional[Sequence["_IpReputationTypeDefinition"]]
    Method: Optional[Sequence["_MethodDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]
    Protocol: Optional[Sequence["_ProtocolDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]
    Version: Optional[Sequence["_VersionDefinition"]]
    VsPort: Optional[Sequence["_VsPortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIp=deserialize_list(json_data.get("ClientIp"), ClientIpDefinition),
            Cookie=deserialize_list(json_data.get("Cookie"), CookieDefinition),
            Hdrs=deserialize_list(json_data.get("Hdrs"), HdrsDefinition),
            HostHdr=deserialize_list(json_data.get("HostHdr"), HostHdrDefinition),
            IpReputationType=deserialize_list(json_data.get("IpReputationType"), IpReputationTypeDefinition),
            Method=deserialize_list(json_data.get("Method"), MethodDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
            Protocol=deserialize_list(json_data.get("Protocol"), ProtocolDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            Version=deserialize_list(json_data.get("Version"), VersionDefinition),
            VsPort=deserialize_list(json_data.get("VsPort"), VsPortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class ClientIpDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpDefinition = ClientIpDefinition


@dataclass
class AddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddrsDefinition = AddrsDefinition


@dataclass
class PrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixesDefinition = PrefixesDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class RangesDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class BeginDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BeginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BeginDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BeginDefinition = BeginDefinition


@dataclass
class EndDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndDefinition = EndDefinition


@dataclass
class CookieDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CookieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieDefinition = CookieDefinition


@dataclass
class HdrsDefinition(BaseModel):
    Hdr: Optional[str]
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HdrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HdrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Hdr=json_data.get("Hdr"),
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HdrsDefinition = HdrsDefinition


@dataclass
class HostHdrDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HostHdrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostHdrDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostHdrDefinition = HostHdrDefinition


@dataclass
class IpReputationTypeDefinition(BaseModel):
    MatchOperation: Optional[str]
    ReputationTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpReputationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpReputationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchOperation=json_data.get("MatchOperation"),
            ReputationTypes=json_data.get("ReputationTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpReputationTypeDefinition = IpReputationTypeDefinition


@dataclass
class MethodDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Methods: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Methods=json_data.get("Methods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodDefinition = MethodDefinition


@dataclass
class ProtocolDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Protocols: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Protocols=json_data.get("Protocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolDefinition = ProtocolDefinition


@dataclass
class QueryDefinition(BaseModel):
    MatchCase: Optional[str]
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCase=json_data.get("MatchCase"),
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class VersionDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Versions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Versions=json_data.get("Versions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionDefinition = VersionDefinition


@dataclass
class VsPortDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Ports: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_VsPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsPortDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsPortDefinition = VsPortDefinition


@dataclass
class HttpResponsePolicyDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpResponsePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpResponsePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpResponsePolicyDefinition = HttpResponsePolicyDefinition


@dataclass
class HttpSecurityPolicyDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpSecurityPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpSecurityPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpSecurityPolicyDefinition = HttpSecurityPolicyDefinition


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


