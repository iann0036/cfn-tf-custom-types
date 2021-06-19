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
    BastionId: Optional[str]
    BastionName: Optional[str]
    BastionPublicHostKeyInfo: Optional[str]
    BastionUserName: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    KeyType: Optional[str]
    LifecycleDetails: Optional[str]
    SessionTtlInSeconds: Optional[float]
    SshMetadata: Optional[Sequence["_SshMetadataDefinition"]]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    KeyDetails: Optional[Sequence["_KeyDetailsDefinition"]]
    TargetResourceDetails: Optional[Sequence["_TargetResourceDetailsDefinition"]]
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
            BastionId=json_data.get("BastionId"),
            BastionName=json_data.get("BastionName"),
            BastionPublicHostKeyInfo=json_data.get("BastionPublicHostKeyInfo"),
            BastionUserName=json_data.get("BastionUserName"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            KeyType=json_data.get("KeyType"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            SessionTtlInSeconds=json_data.get("SessionTtlInSeconds"),
            SshMetadata=deserialize_list(json_data.get("SshMetadata"), SshMetadataDefinition),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            KeyDetails=deserialize_list(json_data.get("KeyDetails"), KeyDetailsDefinition),
            TargetResourceDetails=deserialize_list(json_data.get("TargetResourceDetails"), TargetResourceDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SshMetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshMetadataDefinition = SshMetadataDefinition


@dataclass
class KeyDetailsDefinition(BaseModel):
    PublicKeyContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            PublicKeyContent=json_data.get("PublicKeyContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDetailsDefinition = KeyDetailsDefinition


@dataclass
class TargetResourceDetailsDefinition(BaseModel):
    SessionType: Optional[str]
    TargetResourceId: Optional[str]
    TargetResourceOperatingSystemUserName: Optional[str]
    TargetResourcePort: Optional[float]
    TargetResourcePrivateIpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetResourceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetResourceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            SessionType=json_data.get("SessionType"),
            TargetResourceId=json_data.get("TargetResourceId"),
            TargetResourceOperatingSystemUserName=json_data.get("TargetResourceOperatingSystemUserName"),
            TargetResourcePort=json_data.get("TargetResourcePort"),
            TargetResourcePrivateIpAddress=json_data.get("TargetResourcePrivateIpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetResourceDetailsDefinition = TargetResourceDetailsDefinition


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


