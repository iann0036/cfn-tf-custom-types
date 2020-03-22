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
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Status: Optional[Sequence["_Status"]]
    Metadata: Optional[Sequence["_Metadata"]]
    Template: Optional[Sequence["_Template"]]
    Timeouts: Optional["_Timeouts"]
    Traffic: Optional[Sequence["_Traffic"]]
    Spec: Optional[Sequence["_Spec"]]
    Containers: Optional[Sequence["_Containers"]]
    Env: Optional[Sequence["_Env"]]
    EnvFrom: Optional[Sequence["_EnvFrom"]]
    Resources: Optional[Sequence["_Resources"]]
    ConfigMapRef: Optional[Sequence["_ConfigMapRef"]]
    SecretRef: Optional[Sequence["_SecretRef"]]
    LocalObjectReference: Optional[Sequence["_LocalObjectReference"]]

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
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Status=json_data.get("Status"),
            Metadata=json_data.get("Metadata"),
            Template=json_data.get("Template"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Traffic=json_data.get("Traffic"),
            Spec=json_data.get("Spec"),
            Containers=json_data.get("Containers"),
            Env=json_data.get("Env"),
            EnvFrom=json_data.get("EnvFrom"),
            Resources=json_data.get("Resources"),
            ConfigMapRef=json_data.get("ConfigMapRef"),
            SecretRef=json_data.get("SecretRef"),
            LocalObjectReference=json_data.get("LocalObjectReference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Status:
    Conditions: Optional[Sequence["_Conditions"]]
    LatestCreatedRevisionName: Optional[str]
    LatestReadyRevisionName: Optional[str]
    ObservedGeneration: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Status"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Status"]:
        if not json_data:
            return None
        return cls(
            Conditions=json_data.get("Conditions"),
            LatestCreatedRevisionName=json_data.get("LatestCreatedRevisionName"),
            LatestReadyRevisionName=json_data.get("LatestReadyRevisionName"),
            ObservedGeneration=json_data.get("ObservedGeneration"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Status = Status


@dataclass
class Conditions:
    Message: Optional[str]
    Reason: Optional[str]
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            Reason=json_data.get("Reason"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class Metadata:
    Annotations: Optional[Sequence["_Annotations"]]
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
class Template:
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]

    @classmethod
    def _deserialize(
        cls: Type["_Template"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Template"]:
        if not json_data:
            return None
        return cls(
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Template = Template


@dataclass
class Spec:
    ContainerConcurrency: Optional[float]
    ServiceAccountName: Optional[str]
    Containers: Optional[Sequence["_Containers"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            ContainerConcurrency=json_data.get("ContainerConcurrency"),
            ServiceAccountName=json_data.get("ServiceAccountName"),
            Containers=json_data.get("Containers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Containers:
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Image: Optional[str]
    WorkingDir: Optional[str]
    Env: Optional[Sequence["_Env"]]
    EnvFrom: Optional[Sequence["_EnvFrom"]]
    Resources: Optional[Sequence["_Resources"]]

    @classmethod
    def _deserialize(
        cls: Type["_Containers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Containers"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Command=json_data.get("Command"),
            Image=json_data.get("Image"),
            WorkingDir=json_data.get("WorkingDir"),
            Env=json_data.get("Env"),
            EnvFrom=json_data.get("EnvFrom"),
            Resources=json_data.get("Resources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Containers = Containers


@dataclass
class Env:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Env"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Env"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Env = Env


@dataclass
class EnvFrom:
    Prefix: Optional[str]
    ConfigMapRef: Optional[Sequence["_ConfigMapRef"]]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvFrom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvFrom"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            ConfigMapRef=json_data.get("ConfigMapRef"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvFrom = EnvFrom


@dataclass
class ConfigMapRef:
    Optional: Optional[bool]
    LocalObjectReference: Optional[Sequence["_LocalObjectReference"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigMapRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigMapRef"]:
        if not json_data:
            return None
        return cls(
            Optional=json_data.get("Optional"),
            LocalObjectReference=json_data.get("LocalObjectReference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigMapRef = ConfigMapRef


@dataclass
class LocalObjectReference:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalObjectReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalObjectReference"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalObjectReference = LocalObjectReference


@dataclass
class SecretRef:
    Optional: Optional[bool]
    LocalObjectReference: Optional[Sequence["_LocalObjectReference"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRef"]:
        if not json_data:
            return None
        return cls(
            Optional=json_data.get("Optional"),
            LocalObjectReference=json_data.get("LocalObjectReference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRef = SecretRef


@dataclass
class Resources:
    Limits: Optional[Sequence["_Limits"]]
    Requests: Optional[Sequence["_Requests"]]

    @classmethod
    def _deserialize(
        cls: Type["_Resources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resources"]:
        if not json_data:
            return None
        return cls(
            Limits=json_data.get("Limits"),
            Requests=json_data.get("Requests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resources = Resources


@dataclass
class Limits:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class Requests:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Requests"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Requests"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Requests = Requests


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class Traffic:
    LatestRevision: Optional[bool]
    Percent: Optional[float]
    RevisionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Traffic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Traffic"]:
        if not json_data:
            return None
        return cls(
            LatestRevision=json_data.get("LatestRevision"),
            Percent=json_data.get("Percent"),
            RevisionName=json_data.get("RevisionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Traffic = Traffic


