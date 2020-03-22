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
    Arn: Optional[str]
    CreatedDate: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Spec: Optional[Sequence["_Spec"]]
    Listener: Optional[Sequence["_Listener"]]
    PortMapping: Optional[Sequence["_PortMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CreatedDate=json_data.get("CreatedDate"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Spec=json_data.get("Spec"),
            Listener=json_data.get("Listener"),
            PortMapping=json_data.get("PortMapping"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Spec:
    ServiceNames: Optional[Sequence[str]]
    Listener: Optional[Sequence["_Listener"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            ServiceNames=json_data.get("ServiceNames"),
            Listener=json_data.get("Listener"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Listener:
    PortMapping: Optional[Sequence["_PortMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listener"]:
        if not json_data:
            return None
        return cls(
            PortMapping=json_data.get("PortMapping"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listener = Listener


@dataclass
class PortMapping:
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMapping"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMapping = PortMapping


