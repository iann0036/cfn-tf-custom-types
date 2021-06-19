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
    Description: Optional[str]
    Eula: Optional[str]
    GalleryName: Optional[str]
    HyperVGeneration: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    OsType: Optional[str]
    PrivacyStatementUri: Optional[str]
    ReleaseNoteUri: Optional[str]
    ResourceGroupName: Optional[str]
    Specialized: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Identifier: Optional[Sequence["_IdentifierDefinition"]]
    PurchasePlan: Optional[Sequence["_PurchasePlanDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Description=json_data.get("Description"),
            Eula=json_data.get("Eula"),
            GalleryName=json_data.get("GalleryName"),
            HyperVGeneration=json_data.get("HyperVGeneration"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            PrivacyStatementUri=json_data.get("PrivacyStatementUri"),
            ReleaseNoteUri=json_data.get("ReleaseNoteUri"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Specialized=json_data.get("Specialized"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Identifier=deserialize_list(json_data.get("Identifier"), IdentifierDefinition),
            PurchasePlan=deserialize_list(json_data.get("PurchasePlan"), PurchasePlanDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class IdentifierDefinition(BaseModel):
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentifierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentifierDefinition"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentifierDefinition = IdentifierDefinition


@dataclass
class PurchasePlanDefinition(BaseModel):
    Name: Optional[str]
    Product: Optional[str]
    Publisher: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PurchasePlanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PurchasePlanDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Publisher=json_data.get("Publisher"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PurchasePlanDefinition = PurchasePlanDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


