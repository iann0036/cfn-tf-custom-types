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
    Hostname: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryAccessKey: Optional[str]
    PrimaryConnectionString: Optional[str]
    PublicPort: Optional[float]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    SecondaryConnectionString: Optional[str]
    ServerPort: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    Cors: Optional[Sequence["_Cors"]]
    Features: Optional[Sequence["_Features"]]
    Sku: Optional[Sequence["_Sku"]]
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
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PublicPort=json_data.get("PublicPort"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            ServerPort=json_data.get("ServerPort"),
            Tags=json_data.get("Tags"),
            Cors=json_data.get("Cors"),
            Features=json_data.get("Features"),
            Sku=json_data.get("Sku"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class Cors:
    AllowedOrigins: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Cors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cors"]:
        if not json_data:
            return None
        return cls(
            AllowedOrigins=json_data.get("AllowedOrigins"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cors = Cors


@dataclass
class Features:
    Flag: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Features"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Features"]:
        if not json_data:
            return None
        return cls(
            Flag=json_data.get("Flag"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Features = Features


@dataclass
class Sku:
    Capacity: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sku"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sku"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sku = Sku


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


