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
    ConnectionConnectTimeout: Optional[float]
    ConnectionRetryCountLimit: Optional[float]
    ConnectionRetrySleepInterval: Optional[float]
    ConnectionRetryTimeLimit: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    IsDefault: Optional[bool]
    Name: Optional[str]
    PollingRequestMaximumMessageProcessingTimeout: Optional[float]
    PollingRequestQueueTimeout: Optional[float]
    SpaceId: Optional[str]
    MachineCleanupPolicy: Optional[Sequence["_MachineCleanupPolicyDefinition"]]
    MachineConnectivityPolicy: Optional[Sequence["_MachineConnectivityPolicyDefinition"]]
    MachineHealthCheckPolicy: Optional[Sequence["_MachineHealthCheckPolicyDefinition"]]
    MachineUpdatePolicy: Optional[Sequence["_MachineUpdatePolicyDefinition"]]

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
            ConnectionConnectTimeout=json_data.get("ConnectionConnectTimeout"),
            ConnectionRetryCountLimit=json_data.get("ConnectionRetryCountLimit"),
            ConnectionRetrySleepInterval=json_data.get("ConnectionRetrySleepInterval"),
            ConnectionRetryTimeLimit=json_data.get("ConnectionRetryTimeLimit"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
            PollingRequestMaximumMessageProcessingTimeout=json_data.get("PollingRequestMaximumMessageProcessingTimeout"),
            PollingRequestQueueTimeout=json_data.get("PollingRequestQueueTimeout"),
            SpaceId=json_data.get("SpaceId"),
            MachineCleanupPolicy=deserialize_list(json_data.get("MachineCleanupPolicy"), MachineCleanupPolicyDefinition),
            MachineConnectivityPolicy=deserialize_list(json_data.get("MachineConnectivityPolicy"), MachineConnectivityPolicyDefinition),
            MachineHealthCheckPolicy=deserialize_list(json_data.get("MachineHealthCheckPolicy"), MachineHealthCheckPolicyDefinition),
            MachineUpdatePolicy=deserialize_list(json_data.get("MachineUpdatePolicy"), MachineUpdatePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MachineCleanupPolicyDefinition(BaseModel):
    DeleteMachinesBehavior: Optional[str]
    DeleteMachinesElapsedTimespan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MachineCleanupPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineCleanupPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteMachinesBehavior=json_data.get("DeleteMachinesBehavior"),
            DeleteMachinesElapsedTimespan=json_data.get("DeleteMachinesElapsedTimespan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineCleanupPolicyDefinition = MachineCleanupPolicyDefinition


@dataclass
class MachineConnectivityPolicyDefinition(BaseModel):
    MachineConnectivityBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineConnectivityPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineConnectivityPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MachineConnectivityBehavior=json_data.get("MachineConnectivityBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineConnectivityPolicyDefinition = MachineConnectivityPolicyDefinition


@dataclass
class MachineHealthCheckPolicyDefinition(BaseModel):
    HealthCheckCron: Optional[str]
    HealthCheckCronTimezone: Optional[str]
    HealthCheckInterval: Optional[float]
    HealthCheckType: Optional[str]
    BashHealthCheckPolicy: Optional[Sequence["_BashHealthCheckPolicyDefinition"]]
    PowershellHealthCheckPolicy: Optional[Sequence["_PowershellHealthCheckPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MachineHealthCheckPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineHealthCheckPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthCheckCron=json_data.get("HealthCheckCron"),
            HealthCheckCronTimezone=json_data.get("HealthCheckCronTimezone"),
            HealthCheckInterval=json_data.get("HealthCheckInterval"),
            HealthCheckType=json_data.get("HealthCheckType"),
            BashHealthCheckPolicy=deserialize_list(json_data.get("BashHealthCheckPolicy"), BashHealthCheckPolicyDefinition),
            PowershellHealthCheckPolicy=deserialize_list(json_data.get("PowershellHealthCheckPolicy"), PowershellHealthCheckPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineHealthCheckPolicyDefinition = MachineHealthCheckPolicyDefinition


@dataclass
class BashHealthCheckPolicyDefinition(BaseModel):
    RunType: Optional[str]
    ScriptBody: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BashHealthCheckPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BashHealthCheckPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            RunType=json_data.get("RunType"),
            ScriptBody=json_data.get("ScriptBody"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BashHealthCheckPolicyDefinition = BashHealthCheckPolicyDefinition


@dataclass
class PowershellHealthCheckPolicyDefinition(BaseModel):
    RunType: Optional[str]
    ScriptBody: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PowershellHealthCheckPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PowershellHealthCheckPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            RunType=json_data.get("RunType"),
            ScriptBody=json_data.get("ScriptBody"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PowershellHealthCheckPolicyDefinition = PowershellHealthCheckPolicyDefinition


@dataclass
class MachineUpdatePolicyDefinition(BaseModel):
    CalamariUpdateBehavior: Optional[str]
    TentacleUpdateAccountId: Optional[str]
    TentacleUpdateBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineUpdatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineUpdatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CalamariUpdateBehavior=json_data.get("CalamariUpdateBehavior"),
            TentacleUpdateAccountId=json_data.get("TentacleUpdateAccountId"),
            TentacleUpdateBehavior=json_data.get("TentacleUpdateBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineUpdatePolicyDefinition = MachineUpdatePolicyDefinition


