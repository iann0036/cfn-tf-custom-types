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
    AcceptAllEulas: Optional[bool]
    CatalogName: Optional[str]
    Cpus: Optional[float]
    Description: Optional[str]
    GuestProperties: Optional[Sequence["_GuestProperties"]]
    Href: Optional[str]
    Initscript: Optional[str]
    Ip: Optional[str]
    Memory: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    NetworkName: Optional[str]
    Org: Optional[str]
    Ovf: Optional[Sequence["_Ovf"]]
    PowerOn: Optional[bool]
    Status: Optional[float]
    StatusText: Optional[str]
    StorageProfile: Optional[str]
    TemplateName: Optional[str]
    Vdc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptAllEulas=json_data.get("AcceptAllEulas"),
            CatalogName=json_data.get("CatalogName"),
            Cpus=json_data.get("Cpus"),
            Description=json_data.get("Description"),
            GuestProperties=json_data.get("GuestProperties"),
            Href=json_data.get("Href"),
            Initscript=json_data.get("Initscript"),
            Ip=json_data.get("Ip"),
            Memory=json_data.get("Memory"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NetworkName=json_data.get("NetworkName"),
            Org=json_data.get("Org"),
            Ovf=json_data.get("Ovf"),
            PowerOn=json_data.get("PowerOn"),
            Status=json_data.get("Status"),
            StatusText=json_data.get("StatusText"),
            StorageProfile=json_data.get("StorageProfile"),
            TemplateName=json_data.get("TemplateName"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuestProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestProperties = GuestProperties


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Ovf:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ovf"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ovf"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ovf = Ovf


