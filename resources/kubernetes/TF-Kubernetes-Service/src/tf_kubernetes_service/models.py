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
    Status: Optional[Sequence["_StatusDefinition3"]]
    WaitForLoadBalancer: Optional[bool]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Status=deserialize_list(json_data.get("Status"), StatusDefinition3),
            WaitForLoadBalancer=json_data.get("WaitForLoadBalancer"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StatusDefinition3(BaseModel):
    LoadBalancer: Optional[Sequence["_StatusDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition3"]:
        if not json_data:
            return None
        return cls(
            LoadBalancer=deserialize_list(json_data.get("LoadBalancer"), StatusDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition3 = StatusDefinition3


@dataclass
class StatusDefinition2(BaseModel):
    Ingress: Optional[Sequence["_StatusDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            Ingress=deserialize_list(json_data.get("Ingress"), StatusDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition2 = StatusDefinition2


@dataclass
class StatusDefinition(BaseModel):
    Hostname: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


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
    ClusterIp: Optional[str]
    ExternalIps: Optional[Sequence[str]]
    ExternalName: Optional[str]
    ExternalTrafficPolicy: Optional[str]
    HealthCheckNodePort: Optional[float]
    LoadBalancerIp: Optional[str]
    LoadBalancerSourceRanges: Optional[Sequence[str]]
    PublishNotReadyAddresses: Optional[bool]
    Selector: Optional[Sequence["_SelectorDefinition"]]
    SessionAffinity: Optional[str]
    Type: Optional[str]
    Port: Optional[Sequence["_PortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterIp=json_data.get("ClusterIp"),
            ExternalIps=json_data.get("ExternalIps"),
            ExternalName=json_data.get("ExternalName"),
            ExternalTrafficPolicy=json_data.get("ExternalTrafficPolicy"),
            HealthCheckNodePort=json_data.get("HealthCheckNodePort"),
            LoadBalancerIp=json_data.get("LoadBalancerIp"),
            LoadBalancerSourceRanges=json_data.get("LoadBalancerSourceRanges"),
            PublishNotReadyAddresses=json_data.get("PublishNotReadyAddresses"),
            Selector=deserialize_list(json_data.get("Selector"), SelectorDefinition),
            SessionAffinity=json_data.get("SessionAffinity"),
            Type=json_data.get("Type"),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class SelectorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectorDefinition = SelectorDefinition


@dataclass
class PortDefinition(BaseModel):
    Name: Optional[str]
    NodePort: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    TargetPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
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
_PortDefinition = PortDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


