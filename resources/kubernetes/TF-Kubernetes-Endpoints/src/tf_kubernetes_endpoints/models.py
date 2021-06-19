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
    Subset: Optional[Sequence["_SubsetDefinition"]]

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
            Subset=deserialize_list(json_data.get("Subset"), SubsetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class SubsetDefinition(BaseModel):
    Address: Optional[Sequence["_AddressDefinition"]]
    NotReadyAddress: Optional[Sequence["_NotReadyAddressDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubsetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubsetDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=deserialize_list(json_data.get("Address"), AddressDefinition),
            NotReadyAddress=deserialize_list(json_data.get("NotReadyAddress"), NotReadyAddressDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubsetDefinition = SubsetDefinition


@dataclass
class AddressDefinition(BaseModel):
    Hostname: Optional[str]
    Ip: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressDefinition = AddressDefinition


@dataclass
class NotReadyAddressDefinition(BaseModel):
    Hostname: Optional[str]
    Ip: Optional[str]
    NodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotReadyAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotReadyAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
            NodeName=json_data.get("NodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotReadyAddressDefinition = NotReadyAddressDefinition


@dataclass
class PortDefinition(BaseModel):
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


