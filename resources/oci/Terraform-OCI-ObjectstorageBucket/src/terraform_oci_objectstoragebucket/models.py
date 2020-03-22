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
    AccessType: Optional[str]
    ApproximateCount: Optional[str]
    ApproximateSize: Optional[str]
    BucketId: Optional[str]
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    Etag: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Namespace: Optional[str]
    ObjectEventsEnabled: Optional[bool]
    ObjectLifecyclePolicyEtag: Optional[str]
    StorageTier: Optional[str]
    TimeCreated: Optional[str]
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
            AccessType=json_data.get("AccessType"),
            ApproximateCount=json_data.get("ApproximateCount"),
            ApproximateSize=json_data.get("ApproximateSize"),
            BucketId=json_data.get("BucketId"),
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DefinedTags=json_data.get("DefinedTags"),
            Etag=json_data.get("Etag"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            ObjectEventsEnabled=json_data.get("ObjectEventsEnabled"),
            ObjectLifecyclePolicyEtag=json_data.get("ObjectLifecyclePolicyEtag"),
            StorageTier=json_data.get("StorageTier"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


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


