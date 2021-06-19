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
    AccessLevel: Optional[str]
    Id: Optional[str]
    IpSubnetworks: Optional[Sequence[str]]
    Members: Optional[Sequence[str]]
    Negate: Optional[bool]
    Regions: Optional[Sequence[str]]
    RequiredAccessLevels: Optional[Sequence[str]]
    DevicePolicy: Optional[Sequence["_DevicePolicyDefinition"]]
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
            AccessLevel=json_data.get("AccessLevel"),
            Id=json_data.get("Id"),
            IpSubnetworks=json_data.get("IpSubnetworks"),
            Members=json_data.get("Members"),
            Negate=json_data.get("Negate"),
            Regions=json_data.get("Regions"),
            RequiredAccessLevels=json_data.get("RequiredAccessLevels"),
            DevicePolicy=deserialize_list(json_data.get("DevicePolicy"), DevicePolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DevicePolicyDefinition(BaseModel):
    AllowedDeviceManagementLevels: Optional[Sequence[str]]
    AllowedEncryptionStatuses: Optional[Sequence[str]]
    RequireAdminApproval: Optional[bool]
    RequireCorpOwned: Optional[bool]
    RequireScreenLock: Optional[bool]
    OsConstraints: Optional[Sequence["_OsConstraintsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DevicePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedDeviceManagementLevels=json_data.get("AllowedDeviceManagementLevels"),
            AllowedEncryptionStatuses=json_data.get("AllowedEncryptionStatuses"),
            RequireAdminApproval=json_data.get("RequireAdminApproval"),
            RequireCorpOwned=json_data.get("RequireCorpOwned"),
            RequireScreenLock=json_data.get("RequireScreenLock"),
            OsConstraints=deserialize_list(json_data.get("OsConstraints"), OsConstraintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicePolicyDefinition = DevicePolicyDefinition


@dataclass
class OsConstraintsDefinition(BaseModel):
    MinimumVersion: Optional[str]
    OsType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            MinimumVersion=json_data.get("MinimumVersion"),
            OsType=json_data.get("OsType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsConstraintsDefinition = OsConstraintsDefinition


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


