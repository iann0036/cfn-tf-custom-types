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
    AutogenerateRevisionName: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Status: Optional[Sequence["_StatusDefinition2"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Traffic: Optional[Sequence["_TrafficDefinition"]]

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
            AutogenerateRevisionName=json_data.get("AutogenerateRevisionName"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Status=deserialize_list(json_data.get("Status"), StatusDefinition2),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Traffic=deserialize_list(json_data.get("Traffic"), TrafficDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StatusDefinition2(BaseModel):
    Conditions: Optional[Sequence["_StatusDefinition"]]
    LatestCreatedRevisionName: Optional[str]
    LatestReadyRevisionName: Optional[str]
    ObservedGeneration: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            Conditions=deserialize_list(json_data.get("Conditions"), StatusDefinition),
            LatestCreatedRevisionName=json_data.get("LatestCreatedRevisionName"),
            LatestReadyRevisionName=json_data.get("LatestReadyRevisionName"),
            ObservedGeneration=json_data.get("ObservedGeneration"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition2 = StatusDefinition2


@dataclass
class StatusDefinition(BaseModel):
    Message: Optional[str]
    Reason: Optional[str]
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            Reason=json_data.get("Reason"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition2"]]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition2),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AnnotationsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition2 = AnnotationsDefinition2


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class TemplateDefinition(BaseModel):
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


@dataclass
class SpecDefinition(BaseModel):
    ContainerConcurrency: Optional[float]
    ServiceAccountName: Optional[str]
    TimeoutSeconds: Optional[float]
    Containers: Optional[Sequence["_ContainersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerConcurrency=json_data.get("ContainerConcurrency"),
            ServiceAccountName=json_data.get("ServiceAccountName"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Containers=deserialize_list(json_data.get("Containers"), ContainersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class ContainersDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    WorkingDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    EnvFrom: Optional[Sequence["_EnvFromDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]
    Resources: Optional[Sequence["_ResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainersDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Command=json_data.get("Command"),
            Image=json_data.get("Image"),
            WorkingDir=json_data.get("WorkingDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            EnvFrom=deserialize_list(json_data.get("EnvFrom"), EnvFromDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainersDefinition = ContainersDefinition


@dataclass
class EnvDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvDefinition = EnvDefinition


@dataclass
class EnvFromDefinition(BaseModel):
    Prefix: Optional[str]
    ConfigMapRef: Optional[Sequence["_ConfigMapRefDefinition"]]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvFromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvFromDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            ConfigMapRef=deserialize_list(json_data.get("ConfigMapRef"), ConfigMapRefDefinition),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvFromDefinition = EnvFromDefinition


@dataclass
class ConfigMapRefDefinition(BaseModel):
    Optional: Optional[bool]
    LocalObjectReference: Optional[Sequence["_LocalObjectReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Optional=json_data.get("Optional"),
            LocalObjectReference=deserialize_list(json_data.get("LocalObjectReference"), LocalObjectReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapRefDefinition = ConfigMapRefDefinition


@dataclass
class LocalObjectReferenceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalObjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalObjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalObjectReferenceDefinition = LocalObjectReferenceDefinition


@dataclass
class SecretRefDefinition(BaseModel):
    Optional: Optional[bool]
    LocalObjectReference: Optional[Sequence["_LocalObjectReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Optional=json_data.get("Optional"),
            LocalObjectReference=deserialize_list(json_data.get("LocalObjectReference"), LocalObjectReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRefDefinition = SecretRefDefinition


@dataclass
class PortsDefinition(BaseModel):
    ContainerPort: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerPort=json_data.get("ContainerPort"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Limits: Optional[Sequence["_LimitsDefinition"]]
    Requests: Optional[Sequence["_RequestsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Limits=deserialize_list(json_data.get("Limits"), LimitsDefinition),
            Requests=deserialize_list(json_data.get("Requests"), RequestsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class LimitsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitsDefinition = LimitsDefinition


@dataclass
class RequestsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestsDefinition = RequestsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TrafficDefinition(BaseModel):
    LatestRevision: Optional[bool]
    Percent: Optional[float]
    RevisionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficDefinition"]:
        if not json_data:
            return None
        return cls(
            LatestRevision=json_data.get("LatestRevision"),
            Percent=json_data.get("Percent"),
            RevisionName=json_data.get("RevisionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficDefinition = TrafficDefinition


