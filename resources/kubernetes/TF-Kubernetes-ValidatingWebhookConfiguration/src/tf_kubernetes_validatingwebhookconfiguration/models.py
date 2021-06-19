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
    Webhook: Optional[Sequence["_WebhookDefinition"]]

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
            Webhook=deserialize_list(json_data.get("Webhook"), WebhookDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    GenerateName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]

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
class WebhookDefinition(BaseModel):
    AdmissionReviewVersions: Optional[Sequence[str]]
    FailurePolicy: Optional[str]
    MatchPolicy: Optional[str]
    Name: Optional[str]
    SideEffects: Optional[str]
    TimeoutSeconds: Optional[float]
    ClientConfig: Optional[Sequence["_ClientConfigDefinition"]]
    NamespaceSelector: Optional[Sequence["_NamespaceSelectorDefinition"]]
    ObjectSelector: Optional[Sequence["_ObjectSelectorDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookDefinition"]:
        if not json_data:
            return None
        return cls(
            AdmissionReviewVersions=json_data.get("AdmissionReviewVersions"),
            FailurePolicy=json_data.get("FailurePolicy"),
            MatchPolicy=json_data.get("MatchPolicy"),
            Name=json_data.get("Name"),
            SideEffects=json_data.get("SideEffects"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            ClientConfig=deserialize_list(json_data.get("ClientConfig"), ClientConfigDefinition),
            NamespaceSelector=deserialize_list(json_data.get("NamespaceSelector"), NamespaceSelectorDefinition),
            ObjectSelector=deserialize_list(json_data.get("ObjectSelector"), ObjectSelectorDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookDefinition = WebhookDefinition


@dataclass
class ClientConfigDefinition(BaseModel):
    CaBundle: Optional[str]
    Url: Optional[str]
    Service: Optional[Sequence["_ServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CaBundle=json_data.get("CaBundle"),
            Url=json_data.get("Url"),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientConfigDefinition = ClientConfigDefinition


@dataclass
class ServiceDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Path: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class NamespaceSelectorDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NamespaceSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespaceSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespaceSelectorDefinition = NamespaceSelectorDefinition


@dataclass
class MatchLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabelsDefinition = MatchLabelsDefinition


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
class ObjectSelectorDefinition(BaseModel):
    MatchLabels: Optional[Sequence["_MatchLabelsDefinition2"]]
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=deserialize_list(json_data.get("MatchLabels"), MatchLabelsDefinition2),
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectSelectorDefinition = ObjectSelectorDefinition


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
class RuleDefinition(BaseModel):
    ApiGroups: Optional[Sequence[str]]
    ApiVersions: Optional[Sequence[str]]
    Operations: Optional[Sequence[str]]
    Resources: Optional[Sequence[str]]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiGroups=json_data.get("ApiGroups"),
            ApiVersions=json_data.get("ApiVersions"),
            Operations=json_data.get("Operations"),
            Resources=json_data.get("Resources"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


