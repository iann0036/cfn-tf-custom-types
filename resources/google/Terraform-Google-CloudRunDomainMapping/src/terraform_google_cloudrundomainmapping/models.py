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
    Spec: Optional[Sequence["_Spec"]]
    Timeouts: Optional["_Timeouts"]

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
            Spec=json_data.get("Spec"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Status:
    Conditions: Optional[Sequence["_Conditions"]]
    MappedRouteName: Optional[str]
    ObservedGeneration: Optional[float]
    ResourceRecords: Optional[Sequence["_ResourceRecords"]]

    @classmethod
    def _deserialize(
        cls: Type["_Status"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Status"]:
        if not json_data:
            return None
        return cls(
            Conditions=json_data.get("Conditions"),
            MappedRouteName=json_data.get("MappedRouteName"),
            ObservedGeneration=json_data.get("ObservedGeneration"),
            ResourceRecords=json_data.get("ResourceRecords"),
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
class ResourceRecords:
    Name: Optional[str]
    Rrdata: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceRecords"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceRecords"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Rrdata=json_data.get("Rrdata"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceRecords = ResourceRecords


@dataclass
class Metadata:
    Annotations: Optional[Sequence["_Annotations"]]
    Labels: Optional[Sequence["_Labels"]]
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
    CertificateMode: Optional[str]
    ForceOverride: Optional[bool]
    RouteName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            CertificateMode=json_data.get("CertificateMode"),
            ForceOverride=json_data.get("ForceOverride"),
            RouteName=json_data.get("RouteName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


