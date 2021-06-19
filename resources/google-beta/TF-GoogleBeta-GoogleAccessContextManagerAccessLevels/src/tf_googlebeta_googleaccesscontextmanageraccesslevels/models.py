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
    Id: Optional[str]
    Parent: Optional[str]
    AccessLevels: Optional[Sequence["_AccessLevelsDefinition"]]
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
            Id=json_data.get("Id"),
            Parent=json_data.get("Parent"),
            AccessLevels=deserialize_list(json_data.get("AccessLevels"), AccessLevelsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessLevelsDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    Title: Optional[str]
    Basic: Optional[Sequence["_BasicDefinition"]]
    Custom: Optional[Sequence["_CustomDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLevelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLevelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Title=json_data.get("Title"),
            Basic=deserialize_list(json_data.get("Basic"), BasicDefinition),
            Custom=deserialize_list(json_data.get("Custom"), CustomDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLevelsDefinition = AccessLevelsDefinition


@dataclass
class BasicDefinition(BaseModel):
    CombiningFunction: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BasicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicDefinition"]:
        if not json_data:
            return None
        return cls(
            CombiningFunction=json_data.get("CombiningFunction"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicDefinition = BasicDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    IpSubnetworks: Optional[Sequence[str]]
    Members: Optional[Sequence[str]]
    Negate: Optional[bool]
    Regions: Optional[Sequence[str]]
    RequiredAccessLevels: Optional[Sequence[str]]
    DevicePolicy: Optional[Sequence["_DevicePolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpSubnetworks=json_data.get("IpSubnetworks"),
            Members=json_data.get("Members"),
            Negate=json_data.get("Negate"),
            Regions=json_data.get("Regions"),
            RequiredAccessLevels=json_data.get("RequiredAccessLevels"),
            DevicePolicy=deserialize_list(json_data.get("DevicePolicy"), DevicePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


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
class CustomDefinition(BaseModel):
    Expr: Optional[Sequence["_ExprDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDefinition"]:
        if not json_data:
            return None
        return cls(
            Expr=deserialize_list(json_data.get("Expr"), ExprDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDefinition = CustomDefinition


@dataclass
class ExprDefinition(BaseModel):
    Description: Optional[str]
    Expression: Optional[str]
    Location: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExprDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExprDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Expression=json_data.get("Expression"),
            Location=json_data.get("Location"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExprDefinition = ExprDefinition


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


