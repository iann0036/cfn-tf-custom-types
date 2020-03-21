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
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]
    Egress: Optional[Sequence["_Egress"]]
    Ingress: Optional[Sequence["_Ingress"]]
    PodSelector: Optional[Sequence["_PodSelector"]]
    Ports: Optional[Sequence["_Ports"]]
    To: Optional[Sequence["_To"]]
    From: Optional[Sequence["_From"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]
    IpBlock: Optional[Sequence["_IpBlock"]]
    NamespaceSelector: Optional[Sequence["_NamespaceSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
            Egress=json_data.get("Egress"),
            Ingress=json_data.get("Ingress"),
            PodSelector=json_data.get("PodSelector"),
            Ports=json_data.get("Ports"),
            To=json_data.get("To"),
            From=json_data.get("From"),
            MatchExpressions=json_data.get("MatchExpressions"),
            IpBlock=json_data.get("IpBlock"),
            NamespaceSelector=json_data.get("NamespaceSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Annotations: Optional[Sequence["_Annotations"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Annotations=json_data.get("Annotations"),
            GenerateName=json_data.get("GenerateName"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Annotations:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Spec:
    PolicyTypes: Optional[Sequence[str]]
    Egress: Optional[Sequence["_Egress"]]
    Ingress: Optional[Sequence["_Ingress"]]
    PodSelector: Optional[Sequence["_PodSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            PolicyTypes=json_data.get("PolicyTypes"),
            Egress=json_data.get("Egress"),
            Ingress=json_data.get("Ingress"),
            PodSelector=json_data.get("PodSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Egress:
    Ports: Optional[Sequence["_Ports"]]
    To: Optional[Sequence["_To"]]

    @classmethod
    def _deserialize(
        cls: Type["_Egress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Egress"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Egress = Egress


@dataclass
class Ports:
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


@dataclass
class To:
    IpBlock: Optional[Sequence["_IpBlock"]]
    NamespaceSelector: Optional[Sequence["_NamespaceSelector"]]
    PodSelector: Optional[Sequence["_PodSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_To"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_To"]:
        if not json_data:
            return None
        return cls(
            IpBlock=json_data.get("IpBlock"),
            NamespaceSelector=json_data.get("NamespaceSelector"),
            PodSelector=json_data.get("PodSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_To = To


@dataclass
class IpBlock:
    Cidr: Optional[str]
    Except: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpBlock"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpBlock"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Except=json_data.get("Except"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpBlock = IpBlock


@dataclass
class NamespaceSelector:
    MatchLabels: Optional[Sequence["_MatchLabels"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]

    @classmethod
    def _deserialize(
        cls: Type["_NamespaceSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespaceSelector"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=json_data.get("MatchLabels"),
            MatchExpressions=json_data.get("MatchExpressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespaceSelector = NamespaceSelector


@dataclass
class MatchLabels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabels = MatchLabels


@dataclass
class MatchExpressions:
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressions = MatchExpressions


@dataclass
class PodSelector:
    MatchLabels: Optional[Sequence["_MatchLabels2"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]

    @classmethod
    def _deserialize(
        cls: Type["_PodSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodSelector"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=json_data.get("MatchLabels"),
            MatchExpressions=json_data.get("MatchExpressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodSelector = PodSelector


@dataclass
class MatchLabels2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabels2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabels2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabels2 = MatchLabels2


@dataclass
class Ingress:
    From: Optional[Sequence["_From"]]
    Ports: Optional[Sequence["_Ports"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
        if not json_data:
            return None
        return cls(
            From=json_data.get("From"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ingress = Ingress


@dataclass
class From:
    IpBlock: Optional[Sequence["_IpBlock"]]
    NamespaceSelector: Optional[Sequence["_NamespaceSelector"]]
    PodSelector: Optional[Sequence["_PodSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_From"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_From"]:
        if not json_data:
            return None
        return cls(
            IpBlock=json_data.get("IpBlock"),
            NamespaceSelector=json_data.get("NamespaceSelector"),
            PodSelector=json_data.get("PodSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_From = From


