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
    Id: Optional[str]
    LoadBalancerIngress: Optional[Sequence["_LoadBalancerIngress"]]
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]
    Backend: Optional[Sequence["_Backend"]]
    Rule: Optional[Sequence["_Rule"]]
    Tls: Optional[Sequence["_Tls"]]
    Http: Optional[Sequence["_Http"]]
    Path: Optional[Sequence["_Path"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            LoadBalancerIngress=json_data.get("LoadBalancerIngress"),
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
            Backend=json_data.get("Backend"),
            Rule=json_data.get("Rule"),
            Tls=json_data.get("Tls"),
            Http=json_data.get("Http"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoadBalancerIngress:
    Hostname: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerIngress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerIngress"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerIngress = LoadBalancerIngress


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
    Backend: Optional[Sequence["_Backend"]]
    Rule: Optional[Sequence["_Rule"]]
    Tls: Optional[Sequence["_Tls"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            Backend=json_data.get("Backend"),
            Rule=json_data.get("Rule"),
            Tls=json_data.get("Tls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Backend:
    ServiceName: Optional[str]
    ServicePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
            ServicePort=json_data.get("ServicePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


@dataclass
class Rule:
    Host: Optional[str]
    Http: Optional[Sequence["_Http"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Http=json_data.get("Http"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Http:
    Path: Optional[Sequence["_Path"]]

    @classmethod
    def _deserialize(
        cls: Type["_Http"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http = Http


@dataclass
class Path:
    Path: Optional[str]
    Backend: Optional[Sequence["_Backend"]]

    @classmethod
    def _deserialize(
        cls: Type["_Path"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Path"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Backend=json_data.get("Backend"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Path = Path


@dataclass
class Tls:
    Hosts: Optional[Sequence[str]]
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tls"]:
        if not json_data:
            return None
        return cls(
            Hosts=json_data.get("Hosts"),
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tls = Tls


