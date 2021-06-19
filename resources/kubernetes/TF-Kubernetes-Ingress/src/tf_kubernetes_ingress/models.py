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
    IngressClassName: Optional[str]
    Backend: Optional[Sequence["_BackendDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]
    Tls: Optional[Sequence["_TlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            IngressClassName=json_data.get("IngressClassName"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Tls=deserialize_list(json_data.get("Tls"), TlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class BackendDefinition(BaseModel):
    ServiceName: Optional[str]
    ServicePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
            ServicePort=json_data.get("ServicePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefinition = BackendDefinition


@dataclass
class RuleDefinition(BaseModel):
    Host: Optional[str]
    Http: Optional[Sequence["_HttpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class HttpDefinition(BaseModel):
    Path: Optional[Sequence["_PathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class PathDefinition(BaseModel):
    Path: Optional[str]
    Backend: Optional[Sequence["_BackendDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class TlsDefinition(BaseModel):
    Hosts: Optional[Sequence[str]]
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsDefinition"]:
        if not json_data:
            return None
        return cls(
            Hosts=json_data.get("Hosts"),
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsDefinition = TlsDefinition


