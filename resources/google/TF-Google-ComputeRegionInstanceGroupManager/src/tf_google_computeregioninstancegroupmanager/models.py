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
    BaseInstanceName: Optional[str]
    Description: Optional[str]
    DistributionPolicyTargetShape: Optional[str]
    DistributionPolicyZones: Optional[Sequence[str]]
    Fingerprint: Optional[str]
    Id: Optional[str]
    InstanceGroup: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    Status: Optional[Sequence["_StatusDefinition4"]]
    TargetPools: Optional[Sequence[str]]
    TargetSize: Optional[float]
    WaitForInstances: Optional[bool]
    WaitForInstancesStatus: Optional[str]
    AutoHealingPolicies: Optional[Sequence["_AutoHealingPoliciesDefinition"]]
    NamedPort: Optional[Sequence["_NamedPortDefinition"]]
    StatefulDisk: Optional[Sequence["_StatefulDiskDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpdatePolicy: Optional[Sequence["_UpdatePolicyDefinition"]]
    Version: Optional[Sequence["_VersionDefinition"]]

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
            BaseInstanceName=json_data.get("BaseInstanceName"),
            Description=json_data.get("Description"),
            DistributionPolicyTargetShape=json_data.get("DistributionPolicyTargetShape"),
            DistributionPolicyZones=json_data.get("DistributionPolicyZones"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            InstanceGroup=json_data.get("InstanceGroup"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            Status=deserialize_list(json_data.get("Status"), StatusDefinition4),
            TargetPools=json_data.get("TargetPools"),
            TargetSize=json_data.get("TargetSize"),
            WaitForInstances=json_data.get("WaitForInstances"),
            WaitForInstancesStatus=json_data.get("WaitForInstancesStatus"),
            AutoHealingPolicies=deserialize_list(json_data.get("AutoHealingPolicies"), AutoHealingPoliciesDefinition),
            NamedPort=deserialize_list(json_data.get("NamedPort"), NamedPortDefinition),
            StatefulDisk=deserialize_list(json_data.get("StatefulDisk"), StatefulDiskDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpdatePolicy=deserialize_list(json_data.get("UpdatePolicy"), UpdatePolicyDefinition),
            Version=deserialize_list(json_data.get("Version"), VersionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StatusDefinition4(BaseModel):
    IsStable: Optional[bool]
    Stateful: Optional[Sequence["_StatusDefinition2"]]
    VersionTarget: Optional[Sequence["_StatusDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition4"]:
        if not json_data:
            return None
        return cls(
            IsStable=json_data.get("IsStable"),
            Stateful=deserialize_list(json_data.get("Stateful"), StatusDefinition2),
            VersionTarget=deserialize_list(json_data.get("VersionTarget"), StatusDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition4 = StatusDefinition4


@dataclass
class StatusDefinition2(BaseModel):
    HasStatefulConfig: Optional[bool]
    PerInstanceConfigs: Optional[Sequence["_StatusDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            HasStatefulConfig=json_data.get("HasStatefulConfig"),
            PerInstanceConfigs=deserialize_list(json_data.get("PerInstanceConfigs"), StatusDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition2 = StatusDefinition2


@dataclass
class StatusDefinition(BaseModel):
    AllEffective: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            AllEffective=json_data.get("AllEffective"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


@dataclass
class StatusDefinition3(BaseModel):
    IsReached: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition3"]:
        if not json_data:
            return None
        return cls(
            IsReached=json_data.get("IsReached"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition3 = StatusDefinition3


@dataclass
class AutoHealingPoliciesDefinition(BaseModel):
    HealthCheck: Optional[str]
    InitialDelaySec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoHealingPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoHealingPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthCheck=json_data.get("HealthCheck"),
            InitialDelaySec=json_data.get("InitialDelaySec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoHealingPoliciesDefinition = AutoHealingPoliciesDefinition


@dataclass
class NamedPortDefinition(BaseModel):
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NamedPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamedPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamedPortDefinition = NamedPortDefinition


@dataclass
class StatefulDiskDefinition(BaseModel):
    DeleteRule: Optional[str]
    DeviceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteRule=json_data.get("DeleteRule"),
            DeviceName=json_data.get("DeviceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulDiskDefinition = StatefulDiskDefinition


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


@dataclass
class UpdatePolicyDefinition(BaseModel):
    InstanceRedistributionType: Optional[str]
    MaxSurgeFixed: Optional[float]
    MaxSurgePercent: Optional[float]
    MaxUnavailableFixed: Optional[float]
    MaxUnavailablePercent: Optional[float]
    MinReadySec: Optional[float]
    MinimalAction: Optional[str]
    ReplacementMethod: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceRedistributionType=json_data.get("InstanceRedistributionType"),
            MaxSurgeFixed=json_data.get("MaxSurgeFixed"),
            MaxSurgePercent=json_data.get("MaxSurgePercent"),
            MaxUnavailableFixed=json_data.get("MaxUnavailableFixed"),
            MaxUnavailablePercent=json_data.get("MaxUnavailablePercent"),
            MinReadySec=json_data.get("MinReadySec"),
            MinimalAction=json_data.get("MinimalAction"),
            ReplacementMethod=json_data.get("ReplacementMethod"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicyDefinition = UpdatePolicyDefinition


@dataclass
class VersionDefinition(BaseModel):
    InstanceTemplate: Optional[str]
    Name: Optional[str]
    TargetSize: Optional[Sequence["_TargetSizeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceTemplate=json_data.get("InstanceTemplate"),
            Name=json_data.get("Name"),
            TargetSize=deserialize_list(json_data.get("TargetSize"), TargetSizeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionDefinition = VersionDefinition


@dataclass
class TargetSizeDefinition(BaseModel):
    Fixed: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetSizeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetSizeDefinition"]:
        if not json_data:
            return None
        return cls(
            Fixed=json_data.get("Fixed"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetSizeDefinition = TargetSizeDefinition


