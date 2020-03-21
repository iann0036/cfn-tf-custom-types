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
    BaseInstanceName: Optional[str]
    Description: Optional[str]
    Fingerprint: Optional[str]
    InstanceGroup: Optional[str]
    InstanceTemplate: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    TargetPools: Optional[Sequence[str]]
    TargetSize: Optional[Sequence["_TargetSize"]]
    UpdateStrategy: Optional[str]
    WaitForInstances: Optional[bool]
    Zone: Optional[str]
    AutoHealingPolicies: Optional[Sequence["_AutoHealingPolicies"]]
    NamedPort: Optional[Sequence["_NamedPort"]]
    Timeouts: Optional["_Timeouts"]
    UpdatePolicy: Optional[Sequence["_UpdatePolicy"]]
    Version: Optional[Sequence["_Version"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BaseInstanceName=json_data.get("BaseInstanceName"),
            Description=json_data.get("Description"),
            Fingerprint=json_data.get("Fingerprint"),
            InstanceGroup=json_data.get("InstanceGroup"),
            InstanceTemplate=json_data.get("InstanceTemplate"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            TargetPools=json_data.get("TargetPools"),
            TargetSize=json_data.get("TargetSize"),
            UpdateStrategy=json_data.get("UpdateStrategy"),
            WaitForInstances=json_data.get("WaitForInstances"),
            Zone=json_data.get("Zone"),
            AutoHealingPolicies=json_data.get("AutoHealingPolicies"),
            NamedPort=json_data.get("NamedPort"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            UpdatePolicy=json_data.get("UpdatePolicy"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TargetSize:
    Fixed: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetSize"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetSize"]:
        if not json_data:
            return None
        return cls(
            Fixed=json_data.get("Fixed"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetSize = TargetSize


@dataclass
class AutoHealingPolicies:
    HealthCheck: Optional[str]
    InitialDelaySec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoHealingPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoHealingPolicies"]:
        if not json_data:
            return None
        return cls(
            HealthCheck=json_data.get("HealthCheck"),
            InitialDelaySec=json_data.get("InitialDelaySec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoHealingPolicies = AutoHealingPolicies


@dataclass
class NamedPort:
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NamedPort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedPort"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedPort = NamedPort


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


@dataclass
class UpdatePolicy:
    MaxSurgeFixed: Optional[float]
    MaxSurgePercent: Optional[float]
    MaxUnavailableFixed: Optional[float]
    MaxUnavailablePercent: Optional[float]
    MinReadySec: Optional[float]
    MinimalAction: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicy"]:
        if not json_data:
            return None
        return cls(
            MaxSurgeFixed=json_data.get("MaxSurgeFixed"),
            MaxSurgePercent=json_data.get("MaxSurgePercent"),
            MaxUnavailableFixed=json_data.get("MaxUnavailableFixed"),
            MaxUnavailablePercent=json_data.get("MaxUnavailablePercent"),
            MinReadySec=json_data.get("MinReadySec"),
            MinimalAction=json_data.get("MinimalAction"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicy = UpdatePolicy


@dataclass
class Version:
    InstanceTemplate: Optional[str]
    Name: Optional[str]
    TargetSize: Optional[Sequence["_TargetSize"]]

    @classmethod
    def _deserialize(
        cls: Type["_Version"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Version"]:
        if not json_data:
            return None
        return cls(
            InstanceTemplate=json_data.get("InstanceTemplate"),
            Name=json_data.get("Name"),
            TargetSize=json_data.get("TargetSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Version = Version


