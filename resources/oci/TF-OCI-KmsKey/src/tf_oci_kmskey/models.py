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
    CompartmentId: Optional[str]
    CurrentKeyVersion: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DesiredState: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsPrimary: Optional[bool]
    ManagementEndpoint: Optional[str]
    ProtectionMode: Optional[str]
    ReplicaDetails: Optional[Sequence["_ReplicaDetailsDefinition"]]
    RestoreTrigger: Optional[bool]
    RestoredFromKeyId: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeOfDeletion: Optional[str]
    VaultId: Optional[str]
    KeyShape: Optional[Sequence["_KeyShapeDefinition"]]
    RestoreFromFile: Optional[Sequence["_RestoreFromFileDefinition"]]
    RestoreFromObjectStore: Optional[Sequence["_RestoreFromObjectStoreDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            CurrentKeyVersion=json_data.get("CurrentKeyVersion"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DesiredState=json_data.get("DesiredState"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsPrimary=json_data.get("IsPrimary"),
            ManagementEndpoint=json_data.get("ManagementEndpoint"),
            ProtectionMode=json_data.get("ProtectionMode"),
            ReplicaDetails=deserialize_list(json_data.get("ReplicaDetails"), ReplicaDetailsDefinition),
            RestoreTrigger=json_data.get("RestoreTrigger"),
            RestoredFromKeyId=json_data.get("RestoredFromKeyId"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeOfDeletion=json_data.get("TimeOfDeletion"),
            VaultId=json_data.get("VaultId"),
            KeyShape=deserialize_list(json_data.get("KeyShape"), KeyShapeDefinition),
            RestoreFromFile=deserialize_list(json_data.get("RestoreFromFile"), RestoreFromFileDefinition),
            RestoreFromObjectStore=deserialize_list(json_data.get("RestoreFromObjectStore"), RestoreFromObjectStoreDefinition),
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
class ReplicaDetailsDefinition(BaseModel):
    ReplicationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            ReplicationId=json_data.get("ReplicationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaDetailsDefinition = ReplicaDetailsDefinition


@dataclass
class KeyShapeDefinition(BaseModel):
    Algorithm: Optional[str]
    CurveId: Optional[str]
    Length: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_KeyShapeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyShapeDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            CurveId=json_data.get("CurveId"),
            Length=json_data.get("Length"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyShapeDefinition = KeyShapeDefinition


@dataclass
class RestoreFromFileDefinition(BaseModel):
    ContentLength: Optional[str]
    ContentMd5: Optional[str]
    RestoreKeyFromFileDetails: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestoreFromFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestoreFromFileDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentLength=json_data.get("ContentLength"),
            ContentMd5=json_data.get("ContentMd5"),
            RestoreKeyFromFileDetails=json_data.get("RestoreKeyFromFileDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestoreFromFileDefinition = RestoreFromFileDefinition


@dataclass
class RestoreFromObjectStoreDefinition(BaseModel):
    Bucket: Optional[str]
    Destination: Optional[str]
    Namespace: Optional[str]
    Object: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestoreFromObjectStoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestoreFromObjectStoreDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Destination=json_data.get("Destination"),
            Namespace=json_data.get("Namespace"),
            Object=json_data.get("Object"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestoreFromObjectStoreDefinition = RestoreFromObjectStoreDefinition


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


