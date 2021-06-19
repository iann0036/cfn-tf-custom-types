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
    AccessType: Optional[str]
    ApproximateCount: Optional[str]
    ApproximateSize: Optional[str]
    AutoTiering: Optional[str]
    BucketId: Optional[str]
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Etag: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsReadOnly: Optional[bool]
    KmsKeyId: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    ObjectEventsEnabled: Optional[bool]
    ObjectLifecyclePolicyEtag: Optional[str]
    ReplicationEnabled: Optional[bool]
    StorageTier: Optional[str]
    TimeCreated: Optional[str]
    Versioning: Optional[str]
    RetentionRules: Optional[Sequence["_RetentionRulesDefinition"]]
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
            AccessType=json_data.get("AccessType"),
            ApproximateCount=json_data.get("ApproximateCount"),
            ApproximateSize=json_data.get("ApproximateSize"),
            AutoTiering=json_data.get("AutoTiering"),
            BucketId=json_data.get("BucketId"),
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Etag=json_data.get("Etag"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsReadOnly=json_data.get("IsReadOnly"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            ObjectEventsEnabled=json_data.get("ObjectEventsEnabled"),
            ObjectLifecyclePolicyEtag=json_data.get("ObjectLifecyclePolicyEtag"),
            ReplicationEnabled=json_data.get("ReplicationEnabled"),
            StorageTier=json_data.get("StorageTier"),
            TimeCreated=json_data.get("TimeCreated"),
            Versioning=json_data.get("Versioning"),
            RetentionRules=deserialize_list(json_data.get("RetentionRules"), RetentionRulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class RetentionRulesDefinition(BaseModel):
    DisplayName: Optional[str]
    TimeRuleLocked: Optional[str]
    Duration: Optional[Sequence["_DurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            TimeRuleLocked=json_data.get("TimeRuleLocked"),
            Duration=deserialize_list(json_data.get("Duration"), DurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionRulesDefinition = RetentionRulesDefinition


@dataclass
class DurationDefinition(BaseModel):
    TimeAmount: Optional[str]
    TimeUnit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DurationDefinition"]:
        if not json_data:
            return None
        return cls(
            TimeAmount=json_data.get("TimeAmount"),
            TimeUnit=json_data.get("TimeUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DurationDefinition = DurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


