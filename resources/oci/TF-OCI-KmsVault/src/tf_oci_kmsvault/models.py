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
    CryptoEndpoint: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IsPrimary: Optional[bool]
    ManagementEndpoint: Optional[str]
    ReplicaDetails: Optional[Sequence["_ReplicaDetailsDefinition"]]
    RestoreTrigger: Optional[bool]
    RestoredFromVaultId: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeOfDeletion: Optional[str]
    VaultType: Optional[str]
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
            CryptoEndpoint=json_data.get("CryptoEndpoint"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IsPrimary=json_data.get("IsPrimary"),
            ManagementEndpoint=json_data.get("ManagementEndpoint"),
            ReplicaDetails=deserialize_list(json_data.get("ReplicaDetails"), ReplicaDetailsDefinition),
            RestoreTrigger=json_data.get("RestoreTrigger"),
            RestoredFromVaultId=json_data.get("RestoredFromVaultId"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeOfDeletion=json_data.get("TimeOfDeletion"),
            VaultType=json_data.get("VaultType"),
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
class RestoreFromFileDefinition(BaseModel):
    ContentLength: Optional[str]
    ContentMd5: Optional[str]
    RestoreVaultFromFileDetails: Optional[str]

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
            RestoreVaultFromFileDetails=json_data.get("RestoreVaultFromFileDetails"),
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


