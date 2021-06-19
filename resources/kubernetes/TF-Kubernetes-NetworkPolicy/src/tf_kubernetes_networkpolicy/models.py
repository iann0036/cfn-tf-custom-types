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
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            GenerateName=json_data.get("GenerateName"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


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
class SpecDefinition(BaseModel):
    PolicyTypes: Optional[Sequence[str]]
    Egress: Optional[Sequence["_EgressDefinition"]]
    Ingress: Optional[Sequence["_IngressDefinition"]]
    PodSelector: Optional[Sequence["_PodSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyTypes=json_data.get("PolicyTypes"),
            Egress=deserialize_list(json_data.get("Egress"), EgressDefinition),
            Ingress=deserialize_list(json_data.get("Ingress"), IngressDefinition),
            PodSelector=deserialize_list(json_data.get("PodSelector"), PodSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class EgressDefinition(BaseModel):
    Ports: Optional[Sequence["_PortsDefinition"]]
    To: Optional[Sequence["_ToDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressDefinition"]:
        if not json_data:
            return None
        return cls(
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            To=deserialize_list(json_data.get("To"), ToDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressDefinition = EgressDefinition


@dataclass
class PortsDefinition(BaseModel):
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


@dataclass
class ToDefinition(BaseModel):
    IpBlock: Optional[Sequence["_IpBlockDefinition"]]
    NamespaceSelector: Optional[Sequence["_NamespaceSelectorDefinition"]]
    PodSelector: Optional[Sequence["_PodSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ToDefinition"]:
        if not json_data:
            return None
        return cls(
            IpBlock=deserialize_list(json_data.get("IpBlock"), IpBlockDefinition),
            NamespaceSelector=deserialize_list(json_data.get("NamespaceSelector"), NamespaceSelectorDefinition),
            PodSelector=deserialize_list(json_data.get("PodSelector"), PodSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ToDefinition = ToDefinition


@dataclass
class IpBlockDefinition(BaseModel):
    Cidr: Optional[str]
    Except: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpBlockDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpBlockDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Except=json_data.get("Except"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpBlockDefinition = IpBlockDefinition


@dataclass
class NamespaceSelectorDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition2"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NamespaceSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespaceSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition2),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespaceSelectorDefinition = NamespaceSelectorDefinition


@dataclass
class MatchLabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabelsDefinition2 = MatchLabelsDefinition2


@dataclass
class MatchExpressionsDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressionsDefinition = MatchExpressionsDefinition


@dataclass
class PodSelectorDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition3"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition3),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodSelectorDefinition = PodSelectorDefinition


@dataclass
class MatchLabelsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabelsDefinition3 = MatchLabelsDefinition3


@dataclass
class IngressDefinition(BaseModel):
    From: Optional[Sequence["_FromDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
        if not json_data:
            return None
        return cls(
            From=deserialize_list(json_data.get("From"), FromDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressDefinition = IngressDefinition


@dataclass
class FromDefinition(BaseModel):
    IpBlock: Optional[Sequence["_IpBlockDefinition"]]
    NamespaceSelector: Optional[Sequence["_NamespaceSelectorDefinition"]]
    PodSelector: Optional[Sequence["_PodSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FromDefinition"]:
        if not json_data:
            return None
        return cls(
            IpBlock=deserialize_list(json_data.get("IpBlock"), IpBlockDefinition),
            NamespaceSelector=deserialize_list(json_data.get("NamespaceSelector"), NamespaceSelectorDefinition),
            PodSelector=deserialize_list(json_data.get("PodSelector"), PodSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FromDefinition = FromDefinition


