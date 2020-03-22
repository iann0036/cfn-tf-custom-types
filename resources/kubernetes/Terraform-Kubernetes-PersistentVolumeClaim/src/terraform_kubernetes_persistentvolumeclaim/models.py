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
    WaitUntilBound: Optional[bool]
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]
    Timeouts: Optional["_Timeouts"]
    Resources: Optional[Sequence["_Resources"]]
    Selector: Optional[Sequence["_Selector"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]

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
            WaitUntilBound=json_data.get("WaitUntilBound"),
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Resources=json_data.get("Resources"),
            Selector=json_data.get("Selector"),
            MatchExpressions=json_data.get("MatchExpressions"),
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
    AccessModes: Optional[Sequence[str]]
    StorageClassName: Optional[str]
    VolumeName: Optional[str]
    Resources: Optional[Sequence["_Resources"]]
    Selector: Optional[Sequence["_Selector"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            AccessModes=json_data.get("AccessModes"),
            StorageClassName=json_data.get("StorageClassName"),
            VolumeName=json_data.get("VolumeName"),
            Resources=json_data.get("Resources"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


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
class Selector:
    MatchLabels: Optional[Sequence["_MatchLabels"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Selector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Selector"]:
        if not json_data:
            return None
        return cls(
            MatchLabels=json_data.get("MatchLabels"),
            MatchExpressions=json_data.get("MatchExpressions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Selector = Selector


@dataclass
class MatchLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
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


