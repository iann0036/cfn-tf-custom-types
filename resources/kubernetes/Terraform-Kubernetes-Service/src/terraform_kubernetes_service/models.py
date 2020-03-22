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
    Timeouts: Optional["_Timeouts"]
    Port: Optional[Sequence["_Port"]]

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
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Port=json_data.get("Port"),
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
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Spec:
    ClusterIp: Optional[str]
    ExternalIps: Optional[Sequence[str]]
    ExternalName: Optional[str]
    ExternalTrafficPolicy: Optional[str]
    LoadBalancerIp: Optional[str]
    LoadBalancerSourceRanges: Optional[Sequence[str]]
    PublishNotReadyAddresses: Optional[bool]
    Selector: Optional[Sequence["_Selector"]]
    SessionAffinity: Optional[str]
    Type: Optional[str]
    Port: Optional[Sequence["_Port"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            ClusterIp=json_data.get("ClusterIp"),
            ExternalIps=json_data.get("ExternalIps"),
            ExternalName=json_data.get("ExternalName"),
            ExternalTrafficPolicy=json_data.get("ExternalTrafficPolicy"),
            LoadBalancerIp=json_data.get("LoadBalancerIp"),
            LoadBalancerSourceRanges=json_data.get("LoadBalancerSourceRanges"),
            PublishNotReadyAddresses=json_data.get("PublishNotReadyAddresses"),
            Selector=json_data.get("Selector"),
            SessionAffinity=json_data.get("SessionAffinity"),
            Type=json_data.get("Type"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Selector:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Selector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Selector"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Selector = Selector


@dataclass
class Port:
    Name: Optional[str]
    NodePort: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    TargetPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Port"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Port"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            NodePort=json_data.get("NodePort"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TargetPort=json_data.get("TargetPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Port = Port


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


