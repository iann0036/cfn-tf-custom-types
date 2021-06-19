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
    Arn: Optional[str]
    Description: Optional[str]
    EnableAutomaticRotation: Optional[bool]
    EncryptionKeyId: Optional[str]
    ForceDeleteWithoutRecovery: Optional[bool]
    Id: Optional[str]
    PlannedDeleteTime: Optional[str]
    RecoveryWindowInDays: Optional[float]
    RotationInterval: Optional[str]
    SecretData: Optional[str]
    SecretDataType: Optional[str]
    SecretName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VersionId: Optional[str]
    VersionStages: Optional[Sequence[str]]
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
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            EnableAutomaticRotation=json_data.get("EnableAutomaticRotation"),
            EncryptionKeyId=json_data.get("EncryptionKeyId"),
            ForceDeleteWithoutRecovery=json_data.get("ForceDeleteWithoutRecovery"),
            Id=json_data.get("Id"),
            PlannedDeleteTime=json_data.get("PlannedDeleteTime"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            RotationInterval=json_data.get("RotationInterval"),
            SecretData=json_data.get("SecretData"),
            SecretDataType=json_data.get("SecretDataType"),
            SecretName=json_data.get("SecretName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VersionId=json_data.get("VersionId"),
            VersionStages=json_data.get("VersionStages"),
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


