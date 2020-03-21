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
    ContainerRead: Optional[str]
    ContainerSyncKey: Optional[str]
    ContainerSyncTo: Optional[str]
    ContainerWrite: Optional[str]
    ContentType: Optional[str]
    ForceDestroy: Optional[bool]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Region: Optional[str]
    Versioning: Optional[Sequence["_Versioning"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ContainerRead=json_data.get("ContainerRead"),
            ContainerSyncKey=json_data.get("ContainerSyncKey"),
            ContainerSyncTo=json_data.get("ContainerSyncTo"),
            ContainerWrite=json_data.get("ContainerWrite"),
            ContentType=json_data.get("ContentType"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Versioning=json_data.get("Versioning"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class Versioning:
    Location: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Versioning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Versioning"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Versioning = Versioning


