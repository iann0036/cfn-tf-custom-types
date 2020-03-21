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
    Description: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    Title: Optional[str]
    Basic: Optional[Sequence["_Basic"]]
    Timeouts: Optional["_Timeouts"]
    Conditions: Optional[Sequence["_Conditions"]]
    DevicePolicy: Optional[Sequence["_DevicePolicy"]]
    OsConstraints: Optional[Sequence["_OsConstraints"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            Title=json_data.get("Title"),
            Basic=json_data.get("Basic"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Conditions=json_data.get("Conditions"),
            DevicePolicy=json_data.get("DevicePolicy"),
            OsConstraints=json_data.get("OsConstraints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Basic:
    CombiningFunction: Optional[str]
    Conditions: Optional[Sequence["_Conditions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Basic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Basic"]:
        if not json_data:
            return None
        return cls(
            CombiningFunction=json_data.get("CombiningFunction"),
            Conditions=json_data.get("Conditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Basic = Basic


@dataclass
class Conditions:
    IpSubnetworks: Optional[Sequence[str]]
    Members: Optional[Sequence[str]]
    Negate: Optional[bool]
    RequiredAccessLevels: Optional[Sequence[str]]
    DevicePolicy: Optional[Sequence["_DevicePolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            IpSubnetworks=json_data.get("IpSubnetworks"),
            Members=json_data.get("Members"),
            Negate=json_data.get("Negate"),
            RequiredAccessLevels=json_data.get("RequiredAccessLevels"),
            DevicePolicy=json_data.get("DevicePolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class DevicePolicy:
    AllowedDeviceManagementLevels: Optional[Sequence[str]]
    AllowedEncryptionStatuses: Optional[Sequence[str]]
    RequireAdminApproval: Optional[bool]
    RequireCorpOwned: Optional[bool]
    RequireScreenLock: Optional[bool]
    OsConstraints: Optional[Sequence["_OsConstraints"]]

    @classmethod
    def _deserialize(
        cls: Type["_DevicePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicePolicy"]:
        if not json_data:
            return None
        return cls(
            AllowedDeviceManagementLevels=json_data.get("AllowedDeviceManagementLevels"),
            AllowedEncryptionStatuses=json_data.get("AllowedEncryptionStatuses"),
            RequireAdminApproval=json_data.get("RequireAdminApproval"),
            RequireCorpOwned=json_data.get("RequireCorpOwned"),
            RequireScreenLock=json_data.get("RequireScreenLock"),
            OsConstraints=json_data.get("OsConstraints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicePolicy = DevicePolicy


@dataclass
class OsConstraints:
    MinimumVersion: Optional[str]
    OsType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsConstraints"]:
        if not json_data:
            return None
        return cls(
            MinimumVersion=json_data.get("MinimumVersion"),
            OsType=json_data.get("OsType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsConstraints = OsConstraints


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


