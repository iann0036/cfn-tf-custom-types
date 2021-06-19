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
    GuestFlush: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SourceInstance: Optional[str]
    StorageLocations: Optional[Sequence[str]]
    MachineImageEncryptionKey: Optional[Sequence["_MachineImageEncryptionKeyDefinition"]]
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
            GuestFlush=json_data.get("GuestFlush"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SourceInstance=json_data.get("SourceInstance"),
            StorageLocations=json_data.get("StorageLocations"),
            MachineImageEncryptionKey=deserialize_list(json_data.get("MachineImageEncryptionKey"), MachineImageEncryptionKeyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MachineImageEncryptionKeyDefinition(BaseModel):
    KmsKeyName: Optional[str]
    KmsKeyServiceAccount: Optional[str]
    RawKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineImageEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineImageEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
            KmsKeyServiceAccount=json_data.get("KmsKeyServiceAccount"),
            RawKey=json_data.get("RawKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineImageEncryptionKeyDefinition = MachineImageEncryptionKeyDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


