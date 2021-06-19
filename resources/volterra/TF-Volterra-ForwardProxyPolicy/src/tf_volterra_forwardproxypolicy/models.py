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
    AllowAll: Optional[bool]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    AnyProxy: Optional[bool]
    Description: Optional[str]
    Disable: Optional[bool]
    DrpHttpConnect: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    AllowList: Optional[Sequence["_AllowListDefinition"]]
    DenyList: Optional[Sequence["_DenyListDefinition"]]
    NetworkConnector: Optional[Sequence["_NetworkConnectorDefinition"]]
    ProxyLabelSelector: Optional[Sequence["_ProxyLabelSelectorDefinition"]]
    RuleList: Optional[Sequence["_RuleListDefinition"]]

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
            AllowAll=json_data.get("AllowAll"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            AnyProxy=json_data.get("AnyProxy"),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DrpHttpConnect=json_data.get("DrpHttpConnect"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            AllowList=deserialize_list(json_data.get("AllowList"), AllowListDefinition),
            DenyList=deserialize_list(json_data.get("DenyList"), DenyListDefinition),
            NetworkConnector=deserialize_list(json_data.get("NetworkConnector"), NetworkConnectorDefinition),
            ProxyLabelSelector=deserialize_list(json_data.get("ProxyLabelSelector"), ProxyLabelSelectorDefinition),
            RuleList=deserialize_list(json_data.get("RuleList"), RuleListDefinition),
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
class AllowListDefinition(BaseModel):
    DefaultActionAllow: Optional[bool]
    DefaultActionDeny: Optional[bool]
    DefaultActionNextPolicy: Optional[bool]
    DestList: Optional[Sequence["_DestListDefinition"]]
    HttpList: Optional[Sequence["_HttpListDefinition"]]
    TlsList: Optional[Sequence["_TlsListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowListDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultActionAllow=json_data.get("DefaultActionAllow"),
            DefaultActionDeny=json_data.get("DefaultActionDeny"),
            DefaultActionNextPolicy=json_data.get("DefaultActionNextPolicy"),
            DestList=deserialize_list(json_data.get("DestList"), DestListDefinition),
            HttpList=deserialize_list(json_data.get("HttpList"), HttpListDefinition),
            TlsList=deserialize_list(json_data.get("TlsList"), TlsListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowListDefinition = AllowListDefinition


@dataclass
class DestListDefinition(BaseModel):
    PortRanges: Optional[str]
    Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DestListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestListDefinition"]:
        if not json_data:
            return None
        return cls(
            PortRanges=json_data.get("PortRanges"),
            Prefixes=json_data.get("Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestListDefinition = DestListDefinition


@dataclass
class HttpListDefinition(BaseModel):
    AnyPath: Optional[bool]
    ExactValue: Optional[str]
    PathExactValue: Optional[str]
    PathPrefixValue: Optional[str]
    PathRegexValue: Optional[str]
    RegexValue: Optional[str]
    SuffixValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpListDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyPath=json_data.get("AnyPath"),
            ExactValue=json_data.get("ExactValue"),
            PathExactValue=json_data.get("PathExactValue"),
            PathPrefixValue=json_data.get("PathPrefixValue"),
            PathRegexValue=json_data.get("PathRegexValue"),
            RegexValue=json_data.get("RegexValue"),
            SuffixValue=json_data.get("SuffixValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpListDefinition = HttpListDefinition


@dataclass
class TlsListDefinition(BaseModel):
    ExactValue: Optional[str]
    RegexValue: Optional[str]
    SuffixValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsListDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValue=json_data.get("ExactValue"),
            RegexValue=json_data.get("RegexValue"),
            SuffixValue=json_data.get("SuffixValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsListDefinition = TlsListDefinition


@dataclass
class DenyListDefinition(BaseModel):
    DefaultActionAllow: Optional[bool]
    DefaultActionDeny: Optional[bool]
    DefaultActionNextPolicy: Optional[bool]
    DestList: Optional[Sequence["_DestListDefinition"]]
    HttpList: Optional[Sequence["_HttpListDefinition"]]
    TlsList: Optional[Sequence["_TlsListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DenyListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DenyListDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultActionAllow=json_data.get("DefaultActionAllow"),
            DefaultActionDeny=json_data.get("DefaultActionDeny"),
            DefaultActionNextPolicy=json_data.get("DefaultActionNextPolicy"),
            DestList=deserialize_list(json_data.get("DestList"), DestListDefinition),
            HttpList=deserialize_list(json_data.get("HttpList"), HttpListDefinition),
            TlsList=deserialize_list(json_data.get("TlsList"), TlsListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DenyListDefinition = DenyListDefinition


@dataclass
class NetworkConnectorDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConnectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConnectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConnectorDefinition = NetworkConnectorDefinition


@dataclass
class ProxyLabelSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyLabelSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyLabelSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyLabelSelectorDefinition = ProxyLabelSelectorDefinition


@dataclass
class RuleListDefinition(BaseModel):
    Rules: Optional[Sequence["_RulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleListDefinition"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleListDefinition = RuleListDefinition


@dataclass
class RulesDefinition(BaseModel):
    Action: Optional[str]
    AllDestinations: Optional[bool]
    AllSources: Optional[bool]
    InsideSources: Optional[bool]
    Namespace: Optional[str]
    NoHttpConnectPort: Optional[bool]
    RuleDescription: Optional[str]
    RuleName: Optional[str]
    DstAsnList: Optional[Sequence["_DstAsnListDefinition"]]
    DstAsnSet: Optional[Sequence["_DstAsnSetDefinition"]]
    DstIpPrefixSet: Optional[Sequence["_DstIpPrefixSetDefinition"]]
    DstLabelSelector: Optional[Sequence["_DstLabelSelectorDefinition"]]
    DstPrefixList: Optional[Sequence["_DstPrefixListDefinition"]]
    HttpList: Optional[Sequence["_HttpListDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    IpPrefixSet: Optional[Sequence["_IpPrefixSetDefinition"]]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    PortMatcher: Optional[Sequence["_PortMatcherDefinition"]]
    PrefixList: Optional[Sequence["_PrefixListDefinition"]]
    TlsList: Optional[Sequence["_TlsListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AllDestinations=json_data.get("AllDestinations"),
            AllSources=json_data.get("AllSources"),
            InsideSources=json_data.get("InsideSources"),
            Namespace=json_data.get("Namespace"),
            NoHttpConnectPort=json_data.get("NoHttpConnectPort"),
            RuleDescription=json_data.get("RuleDescription"),
            RuleName=json_data.get("RuleName"),
            DstAsnList=deserialize_list(json_data.get("DstAsnList"), DstAsnListDefinition),
            DstAsnSet=deserialize_list(json_data.get("DstAsnSet"), DstAsnSetDefinition),
            DstIpPrefixSet=deserialize_list(json_data.get("DstIpPrefixSet"), DstIpPrefixSetDefinition),
            DstLabelSelector=deserialize_list(json_data.get("DstLabelSelector"), DstLabelSelectorDefinition),
            DstPrefixList=deserialize_list(json_data.get("DstPrefixList"), DstPrefixListDefinition),
            HttpList=deserialize_list(json_data.get("HttpList"), HttpListDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            IpPrefixSet=deserialize_list(json_data.get("IpPrefixSet"), IpPrefixSetDefinition),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            PortMatcher=deserialize_list(json_data.get("PortMatcher"), PortMatcherDefinition),
            PrefixList=deserialize_list(json_data.get("PrefixList"), PrefixListDefinition),
            TlsList=deserialize_list(json_data.get("TlsList"), TlsListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


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
class DstAsnSetDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstAsnSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstAsnSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstAsnSetDefinition = DstAsnSetDefinition


@dataclass
class DstIpPrefixSetDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstIpPrefixSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstIpPrefixSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstIpPrefixSetDefinition = DstIpPrefixSetDefinition


@dataclass
class DstLabelSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DstLabelSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstLabelSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstLabelSelectorDefinition = DstLabelSelectorDefinition


@dataclass
class DstPrefixListDefinition(BaseModel):
    Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DstPrefixListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstPrefixListDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefixes=json_data.get("Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstPrefixListDefinition = DstPrefixListDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class IpPrefixSetDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixSetDefinition = IpPrefixSetDefinition


@dataclass
class LabelSelectorDefinition(BaseModel):
    Expressions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LabelSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Expressions=json_data.get("Expressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelSelectorDefinition = LabelSelectorDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Description: Optional[str]
    Disable: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


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
class PrefixListDefinition(BaseModel):
    Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixListDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefixes=json_data.get("Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixListDefinition = PrefixListDefinition


