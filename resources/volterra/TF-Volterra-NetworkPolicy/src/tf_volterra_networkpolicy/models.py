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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Endpoint: Optional[Sequence["_EndpointDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
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
class EndpointDefinition(BaseModel):
    Any: Optional[bool]
    InsideEndpoints: Optional[bool]
    Namespace: Optional[str]
    OutsideEndpoints: Optional[bool]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]
    PrefixList: Optional[Sequence["_PrefixListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            Any=json_data.get("Any"),
            InsideEndpoints=json_data.get("InsideEndpoints"),
            Namespace=json_data.get("Namespace"),
            OutsideEndpoints=json_data.get("OutsideEndpoints"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
            PrefixList=deserialize_list(json_data.get("PrefixList"), PrefixListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


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


@dataclass
class RulesDefinition(BaseModel):
    EgressRules: Optional[Sequence["_EgressRulesDefinition"]]
    IngressRules: Optional[Sequence["_IngressRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressRules=deserialize_list(json_data.get("EgressRules"), EgressRulesDefinition),
            IngressRules=deserialize_list(json_data.get("IngressRules"), IngressRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class EgressRulesDefinition(BaseModel):
    Action: Optional[str]
    AllTcpTraffic: Optional[bool]
    AllTraffic: Optional[bool]
    AllUdpTraffic: Optional[bool]
    Any: Optional[bool]
    InsideEndpoints: Optional[bool]
    Keys: Optional[Sequence[str]]
    Namespace: Optional[str]
    OutsideEndpoints: Optional[bool]
    RuleDescription: Optional[str]
    RuleName: Optional[str]
    AdvAction: Optional[Sequence["_AdvActionDefinition"]]
    Applications: Optional[Sequence["_ApplicationsDefinition"]]
    IpPrefixSet: Optional[Sequence["_IpPrefixSetDefinition"]]
    LabelMatcher: Optional[Sequence["_LabelMatcherDefinition"]]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    PrefixList: Optional[Sequence["_PrefixListDefinition"]]
    ProtocolPortRange: Optional[Sequence["_ProtocolPortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AllTcpTraffic=json_data.get("AllTcpTraffic"),
            AllTraffic=json_data.get("AllTraffic"),
            AllUdpTraffic=json_data.get("AllUdpTraffic"),
            Any=json_data.get("Any"),
            InsideEndpoints=json_data.get("InsideEndpoints"),
            Keys=json_data.get("Keys"),
            Namespace=json_data.get("Namespace"),
            OutsideEndpoints=json_data.get("OutsideEndpoints"),
            RuleDescription=json_data.get("RuleDescription"),
            RuleName=json_data.get("RuleName"),
            AdvAction=deserialize_list(json_data.get("AdvAction"), AdvActionDefinition),
            Applications=deserialize_list(json_data.get("Applications"), ApplicationsDefinition),
            IpPrefixSet=deserialize_list(json_data.get("IpPrefixSet"), IpPrefixSetDefinition),
            LabelMatcher=deserialize_list(json_data.get("LabelMatcher"), LabelMatcherDefinition),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            PrefixList=deserialize_list(json_data.get("PrefixList"), PrefixListDefinition),
            ProtocolPortRange=deserialize_list(json_data.get("ProtocolPortRange"), ProtocolPortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressRulesDefinition = EgressRulesDefinition


@dataclass
class AdvActionDefinition(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvActionDefinition = AdvActionDefinition


@dataclass
class ApplicationsDefinition(BaseModel):
    Applications: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Applications=json_data.get("Applications"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationsDefinition = ApplicationsDefinition


@dataclass
class IpPrefixSetDefinition(BaseModel):
    Ref: Optional[Sequence["_RefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPrefixSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPrefixSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Ref=deserialize_list(json_data.get("Ref"), RefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPrefixSetDefinition = IpPrefixSetDefinition


@dataclass
class RefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefDefinition = RefDefinition


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
class ProtocolPortRangeDefinition(BaseModel):
    PortRanges: Optional[Sequence[str]]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolPortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolPortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            PortRanges=json_data.get("PortRanges"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolPortRangeDefinition = ProtocolPortRangeDefinition


@dataclass
class IngressRulesDefinition(BaseModel):
    Action: Optional[str]
    AllTcpTraffic: Optional[bool]
    AllTraffic: Optional[bool]
    AllUdpTraffic: Optional[bool]
    Any: Optional[bool]
    InsideEndpoints: Optional[bool]
    Keys: Optional[Sequence[str]]
    Namespace: Optional[str]
    OutsideEndpoints: Optional[bool]
    RuleDescription: Optional[str]
    RuleName: Optional[str]
    AdvAction: Optional[Sequence["_AdvActionDefinition"]]
    Applications: Optional[Sequence["_ApplicationsDefinition"]]
    IpPrefixSet: Optional[Sequence["_IpPrefixSetDefinition"]]
    LabelMatcher: Optional[Sequence["_LabelMatcherDefinition"]]
    LabelSelector: Optional[Sequence["_LabelSelectorDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    PrefixList: Optional[Sequence["_PrefixListDefinition"]]
    ProtocolPortRange: Optional[Sequence["_ProtocolPortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AllTcpTraffic=json_data.get("AllTcpTraffic"),
            AllTraffic=json_data.get("AllTraffic"),
            AllUdpTraffic=json_data.get("AllUdpTraffic"),
            Any=json_data.get("Any"),
            InsideEndpoints=json_data.get("InsideEndpoints"),
            Keys=json_data.get("Keys"),
            Namespace=json_data.get("Namespace"),
            OutsideEndpoints=json_data.get("OutsideEndpoints"),
            RuleDescription=json_data.get("RuleDescription"),
            RuleName=json_data.get("RuleName"),
            AdvAction=deserialize_list(json_data.get("AdvAction"), AdvActionDefinition),
            Applications=deserialize_list(json_data.get("Applications"), ApplicationsDefinition),
            IpPrefixSet=deserialize_list(json_data.get("IpPrefixSet"), IpPrefixSetDefinition),
            LabelMatcher=deserialize_list(json_data.get("LabelMatcher"), LabelMatcherDefinition),
            LabelSelector=deserialize_list(json_data.get("LabelSelector"), LabelSelectorDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            PrefixList=deserialize_list(json_data.get("PrefixList"), PrefixListDefinition),
            ProtocolPortRange=deserialize_list(json_data.get("ProtocolPortRange"), ProtocolPortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressRulesDefinition = IngressRulesDefinition


