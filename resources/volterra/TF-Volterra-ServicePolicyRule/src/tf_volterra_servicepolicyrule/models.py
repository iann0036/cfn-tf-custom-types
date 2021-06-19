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
    Action: Optional[str]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    AnyAsn: Optional[bool]
    AnyClient: Optional[bool]
    AnyDstAsn: Optional[bool]
    AnyDstIp: Optional[bool]
    AnyIp: Optional[bool]
    ChallengeAction: Optional[str]
    ClientName: Optional[str]
    Description: Optional[str]
    Disable: Optional[bool]
    ExpirationTimestamp: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MaliciousUserMitigationBypass: Optional[bool]
    Name: Optional[str]
    Namespace: Optional[str]
    Scheme: Optional[Sequence[str]]
    ApiGroupMatcher: Optional[Sequence["_ApiGroupMatcherDefinition"]]
    ArgMatchers: Optional[Sequence["_ArgMatchersDefinition"]]
    AsnList: Optional[Sequence["_AsnListDefinition"]]
    AsnMatcher: Optional[Sequence["_AsnMatcherDefinition"]]
    BodyMatcher: Optional[Sequence["_BodyMatcherDefinition"]]
    ClientNameMatcher: Optional[Sequence["_ClientNameMatcherDefinition"]]
    ClientRole: Optional[Sequence["_ClientRoleDefinition"]]
    ClientSelector: Optional[Sequence["_ClientSelectorDefinition"]]
    CookieMatchers: Optional[Sequence["_CookieMatchersDefinition"]]
    DomainMatcher: Optional[Sequence["_DomainMatcherDefinition"]]
    DstAsnList: Optional[Sequence["_DstAsnListDefinition"]]
    DstAsnMatcher: Optional[Sequence["_DstAsnMatcherDefinition"]]
    DstIpMatcher: Optional[Sequence["_DstIpMatcherDefinition"]]
    DstIpPrefixList: Optional[Sequence["_DstIpPrefixListDefinition"]]
    GotoPolicy: Optional[Sequence["_GotoPolicyDefinition"]]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HttpMethod: Optional[Sequence["_HttpMethodDefinition"]]
    IpMatcher: Optional[Sequence["_IpMatcherDefinition"]]
    IpPrefixList: Optional[Sequence["_IpPrefixListDefinition"]]
    L4DestMatcher: Optional[Sequence["_L4DestMatcherDefinition"]]
    LabelMatcher: Optional[Sequence["_LabelMatcherDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]
    PortMatcher: Optional[Sequence["_PortMatcherDefinition"]]
    QueryParams: Optional[Sequence["_QueryParamsDefinition"]]
    RateLimiter: Optional[Sequence["_RateLimiterDefinition"]]
    ServerSelector: Optional[Sequence["_ServerSelectorDefinition"]]
    TlsFingerprintMatcher: Optional[Sequence["_TlsFingerprintMatcherDefinition"]]
    UrlMatcher: Optional[Sequence["_UrlMatcherDefinition"]]
    VirtualHostMatcher: Optional[Sequence["_VirtualHostMatcherDefinition"]]
    WafAction: Optional[Sequence["_WafActionDefinition"]]

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
            Action=json_data.get("Action"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            AnyAsn=json_data.get("AnyAsn"),
            AnyClient=json_data.get("AnyClient"),
            AnyDstAsn=json_data.get("AnyDstAsn"),
            AnyDstIp=json_data.get("AnyDstIp"),
            AnyIp=json_data.get("AnyIp"),
            ChallengeAction=json_data.get("ChallengeAction"),
            ClientName=json_data.get("ClientName"),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            ExpirationTimestamp=json_data.get("ExpirationTimestamp"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MaliciousUserMitigationBypass=json_data.get("MaliciousUserMitigationBypass"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Scheme=json_data.get("Scheme"),
            ApiGroupMatcher=deserialize_list(json_data.get("ApiGroupMatcher"), ApiGroupMatcherDefinition),
            ArgMatchers=deserialize_list(json_data.get("ArgMatchers"), ArgMatchersDefinition),
            AsnList=deserialize_list(json_data.get("AsnList"), AsnListDefinition),
            AsnMatcher=deserialize_list(json_data.get("AsnMatcher"), AsnMatcherDefinition),
            BodyMatcher=deserialize_list(json_data.get("BodyMatcher"), BodyMatcherDefinition),
            ClientNameMatcher=deserialize_list(json_data.get("ClientNameMatcher"), ClientNameMatcherDefinition),
            ClientRole=deserialize_list(json_data.get("ClientRole"), ClientRoleDefinition),
            ClientSelector=deserialize_list(json_data.get("ClientSelector"), ClientSelectorDefinition),
            CookieMatchers=deserialize_list(json_data.get("CookieMatchers"), CookieMatchersDefinition),
            DomainMatcher=deserialize_list(json_data.get("DomainMatcher"), DomainMatcherDefinition),
            DstAsnList=deserialize_list(json_data.get("DstAsnList"), DstAsnListDefinition),
            DstAsnMatcher=deserialize_list(json_data.get("DstAsnMatcher"), DstAsnMatcherDefinition),
            DstIpMatcher=deserialize_list(json_data.get("DstIpMatcher"), DstIpMatcherDefinition),
            DstIpPrefixList=deserialize_list(json_data.get("DstIpPrefixList"), DstIpPrefixListDefinition),
            GotoPolicy=deserialize_list(json_data.get("GotoPolicy"), GotoPolicyDefinition),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HttpMethod=deserialize_list(json_data.get("HttpMethod"), HttpMethodDefinition),
            IpMatcher=deserialize_list(json_data.get("IpMatcher"), IpMatcherDefinition),
            IpPrefixList=deserialize_list(json_data.get("IpPrefixList"), IpPrefixListDefinition),
            L4DestMatcher=deserialize_list(json_data.get("L4DestMatcher"), L4DestMatcherDefinition),
            LabelMatcher=deserialize_list(json_data.get("LabelMatcher"), LabelMatcherDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
            PortMatcher=deserialize_list(json_data.get("PortMatcher"), PortMatcherDefinition),
            QueryParams=deserialize_list(json_data.get("QueryParams"), QueryParamsDefinition),
            RateLimiter=deserialize_list(json_data.get("RateLimiter"), RateLimiterDefinition),
            ServerSelector=deserialize_list(json_data.get("ServerSelector"), ServerSelectorDefinition),
            TlsFingerprintMatcher=deserialize_list(json_data.get("TlsFingerprintMatcher"), TlsFingerprintMatcherDefinition),
            UrlMatcher=deserialize_list(json_data.get("UrlMatcher"), UrlMatcherDefinition),
            VirtualHostMatcher=deserialize_list(json_data.get("VirtualHostMatcher"), VirtualHostMatcherDefinition),
            WafAction=deserialize_list(json_data.get("WafAction"), WafActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ApiGroupMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    Match: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ApiGroupMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiGroupMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiGroupMatcherDefinition = ApiGroupMatcherDefinition


@dataclass
class ArgMatchersDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArgMatchersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArgMatchersDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArgMatchersDefinition = ArgMatchersDefinition


@dataclass
class ItemDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemDefinition = ItemDefinition


@dataclass
class AsnListDefinition(BaseModel):
    AsNumbers: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_AsnListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsnListDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumbers=json_data.get("AsNumbers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsnListDefinition = AsnListDefinition


@dataclass
class AsnMatcherDefinition(BaseModel):
    AsnSets: Optional[Sequence["_AsnSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AsnMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsnMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            AsnSets=deserialize_list(json_data.get("AsnSets"), AsnSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsnMatcherDefinition = AsnMatcherDefinition


@dataclass
class AsnSetsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AsnSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsnSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsnSetsDefinition = AsnSetsDefinition


@dataclass
class BodyMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BodyMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyMatcherDefinition = BodyMatcherDefinition


@dataclass
class ClientNameMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientNameMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientNameMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientNameMatcherDefinition = ClientNameMatcherDefinition


@dataclass
class ClientRoleDefinition(BaseModel):
    Match: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientRoleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientRoleDefinition"]:
        if not json_data:
            return None
        return cls(
            Match=json_data.get("Match"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientRoleDefinition = ClientRoleDefinition


@dataclass
class ClientSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSelectorDefinition = ClientSelectorDefinition


@dataclass
class CookieMatchersDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CookieMatchersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieMatchersDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieMatchersDefinition = CookieMatchersDefinition


@dataclass
class DomainMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DomainMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainMatcherDefinition = DomainMatcherDefinition


@dataclass
class DstAsnListDefinition(BaseModel):
    AsNumbers: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_DstAsnListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstAsnListDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumbers=json_data.get("AsNumbers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstAsnListDefinition = DstAsnListDefinition


@dataclass
class DstAsnMatcherDefinition(BaseModel):
    AsnSets: Optional[Sequence["_AsnSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DstAsnMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstAsnMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            AsnSets=deserialize_list(json_data.get("AsnSets"), AsnSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstAsnMatcherDefinition = DstAsnMatcherDefinition


@dataclass
class DstIpMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    PrefixSets: Optional[Sequence["_PrefixSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DstIpMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstIpMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            PrefixSets=deserialize_list(json_data.get("PrefixSets"), PrefixSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstIpMatcherDefinition = DstIpMatcherDefinition


@dataclass
class PrefixSetsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixSetsDefinition = PrefixSetsDefinition


@dataclass
class DstIpPrefixListDefinition(BaseModel):
    InvertMatch: Optional[bool]
    IpPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DstIpPrefixListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstIpPrefixListDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatch=json_data.get("InvertMatch"),
            IpPrefixes=json_data.get("IpPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstIpPrefixListDefinition = DstIpPrefixListDefinition


@dataclass
class GotoPolicyDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GotoPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GotoPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GotoPolicyDefinition = GotoPolicyDefinition


@dataclass
class HeadersDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Name: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Name=json_data.get("Name"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class HttpMethodDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    Methods: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpMethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpMethodDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            Methods=json_data.get("Methods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpMethodDefinition = HttpMethodDefinition


@dataclass
class IpMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    PrefixSets: Optional[Sequence["_PrefixSetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            PrefixSets=deserialize_list(json_data.get("PrefixSets"), PrefixSetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpMatcherDefinition = IpMatcherDefinition


@dataclass
class IpPrefixListDefinition(BaseModel):
    InvertMatch: Optional[bool]
    IpPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixListDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatch=json_data.get("InvertMatch"),
            IpPrefixes=json_data.get("IpPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixListDefinition = IpPrefixListDefinition


@dataclass
class L4DestMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    L4Dests: Optional[Sequence["_L4DestsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_L4DestMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_L4DestMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            L4Dests=deserialize_list(json_data.get("L4Dests"), L4DestsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_L4DestMatcherDefinition = L4DestMatcherDefinition


@dataclass
class L4DestsDefinition(BaseModel):
    PortRanges: Optional[str]
    Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_L4DestsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_L4DestsDefinition"]:
        if not json_data:
            return None
        return cls(
            PortRanges=json_data.get("PortRanges"),
            Prefixes=json_data.get("Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_L4DestsDefinition = L4DestsDefinition


@dataclass
class LabelMatcherDefinition(BaseModel):
    Keys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LabelMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            Keys=json_data.get("Keys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelMatcherDefinition = LabelMatcherDefinition


@dataclass
class PathDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    PrefixValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]
    Transformers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            PrefixValues=json_data.get("PrefixValues"),
            RegexValues=json_data.get("RegexValues"),
            Transformers=json_data.get("Transformers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class PortMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PortMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMatcherDefinition = PortMatcherDefinition


@dataclass
class QueryParamsDefinition(BaseModel):
    CheckNotPresent: Optional[bool]
    CheckPresent: Optional[bool]
    InvertMatcher: Optional[bool]
    Key: Optional[str]
    Presence: Optional[bool]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckNotPresent=json_data.get("CheckNotPresent"),
            CheckPresent=json_data.get("CheckPresent"),
            InvertMatcher=json_data.get("InvertMatcher"),
            Key=json_data.get("Key"),
            Presence=json_data.get("Presence"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParamsDefinition = QueryParamsDefinition


@dataclass
class RateLimiterDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimiterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimiterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimiterDefinition = RateLimiterDefinition


@dataclass
class ServerSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSelectorDefinition = ServerSelectorDefinition


@dataclass
class TlsFingerprintMatcherDefinition(BaseModel):
    Classes: Optional[Sequence[str]]
    ExactValues: Optional[Sequence[str]]
    ExcludedValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsFingerprintMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsFingerprintMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            Classes=json_data.get("Classes"),
            ExactValues=json_data.get("ExactValues"),
            ExcludedValues=json_data.get("ExcludedValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsFingerprintMatcherDefinition = TlsFingerprintMatcherDefinition


@dataclass
class UrlMatcherDefinition(BaseModel):
    InvertMatcher: Optional[bool]
    UrlItems: Optional[Sequence["_UrlItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            InvertMatcher=json_data.get("InvertMatcher"),
            UrlItems=deserialize_list(json_data.get("UrlItems"), UrlItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlMatcherDefinition = UrlMatcherDefinition


@dataclass
class UrlItemsDefinition(BaseModel):
    DomainRegex: Optional[str]
    DomainValue: Optional[str]
    PathPrefix: Optional[str]
    PathRegex: Optional[str]
    PathValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlItemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlItemsDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainRegex=json_data.get("DomainRegex"),
            DomainValue=json_data.get("DomainValue"),
            PathPrefix=json_data.get("PathPrefix"),
            PathRegex=json_data.get("PathRegex"),
            PathValue=json_data.get("PathValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlItemsDefinition = UrlItemsDefinition


@dataclass
class VirtualHostMatcherDefinition(BaseModel):
    ExactValues: Optional[Sequence[str]]
    RegexValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualHostMatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualHostMatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValues=json_data.get("ExactValues"),
            RegexValues=json_data.get("RegexValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualHostMatcherDefinition = VirtualHostMatcherDefinition


@dataclass
class WafActionDefinition(BaseModel):
    None: Optional[bool]
    WafInMonitoringMode: Optional[bool]
    WafSkipProcessing: Optional[bool]
    WafInlineRuleControl: Optional[Sequence["_WafInlineRuleControlDefinition"]]
    WafRuleControl: Optional[Sequence["_WafRuleControlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafActionDefinition"]:
        if not json_data:
            return None
        return cls(
            None=json_data.get("None"),
            WafInMonitoringMode=json_data.get("WafInMonitoringMode"),
            WafSkipProcessing=json_data.get("WafSkipProcessing"),
            WafInlineRuleControl=deserialize_list(json_data.get("WafInlineRuleControl"), WafInlineRuleControlDefinition),
            WafRuleControl=deserialize_list(json_data.get("WafRuleControl"), WafRuleControlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafActionDefinition = WafActionDefinition


@dataclass
class WafInlineRuleControlDefinition(BaseModel):
    ExcludeRuleIds: Optional[Sequence[str]]
    MonitoringMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WafInlineRuleControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafInlineRuleControlDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludeRuleIds=json_data.get("ExcludeRuleIds"),
            MonitoringMode=json_data.get("MonitoringMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafInlineRuleControlDefinition = WafInlineRuleControlDefinition


@dataclass
class WafRuleControlDefinition(BaseModel):
    MonitoringMode: Optional[bool]
    ExcludeRuleIds: Optional[Sequence["_ExcludeRuleIdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafRuleControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafRuleControlDefinition"]:
        if not json_data:
            return None
        return cls(
            MonitoringMode=json_data.get("MonitoringMode"),
            ExcludeRuleIds=deserialize_list(json_data.get("ExcludeRuleIds"), ExcludeRuleIdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafRuleControlDefinition = WafRuleControlDefinition


@dataclass
class ExcludeRuleIdsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeRuleIdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeRuleIdsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeRuleIdsDefinition = ExcludeRuleIdsDefinition


