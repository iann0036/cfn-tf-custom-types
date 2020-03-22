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
    Metadata: Optional[Sequence["_Metadata"]]
    Subset: Optional[Sequence["_Subset"]]
    Address: Optional[Sequence["_Address"]]
    NotReadyAddress: Optional[Sequence["_NotReadyAddress"]]
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
            Metadata=json_data.get("Metadata"),
            Subset=json_data.get("Subset"),
            Address=json_data.get("Address"),
            NotReadyAddress=json_data.get("NotReadyAddress"),
            Port=json_data.get("Port"),
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
class Subset:
    Address: Optional[Sequence["_Address"]]
    NotReadyAddress: Optional[Sequence["_NotReadyAddress"]]
    Port: Optional[Sequence["_Port"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subset"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            NotReadyAddress=json_data.get("NotReadyAddress"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subset = Subset


@dataclass
class Address:
    Hostname: Optional[str]
    Ip: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Address"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Address"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Address = Address


@dataclass
class NotReadyAddress:
    Hostname: Optional[str]
    Ip: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotReadyAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotReadyAddress"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotReadyAddress = NotReadyAddress


@dataclass
class Port:
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Port"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Port"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Port = Port


