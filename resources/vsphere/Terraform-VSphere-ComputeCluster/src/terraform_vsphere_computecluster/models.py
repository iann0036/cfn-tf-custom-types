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
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    DatacenterId: Optional[str]
    DpmAutomationLevel: Optional[str]
    DpmEnabled: Optional[bool]
    DpmThreshold: Optional[float]
    DrsAdvancedOptions: Optional[Sequence["_DrsAdvancedOptions"]]
    DrsAutomationLevel: Optional[str]
    DrsEnablePredictiveDrs: Optional[bool]
    DrsEnableVmOverrides: Optional[bool]
    DrsEnabled: Optional[bool]
    DrsMigrationThreshold: Optional[float]
    Folder: Optional[str]
    ForceEvacuateOnDestroy: Optional[bool]
    HaAdmissionControlFailoverHostSystemIds: Optional[Sequence[str]]
    HaAdmissionControlHostFailureTolerance: Optional[float]
    HaAdmissionControlPerformanceTolerance: Optional[float]
    HaAdmissionControlPolicy: Optional[str]
    HaAdmissionControlResourcePercentageAutoCompute: Optional[bool]
    HaAdmissionControlResourcePercentageCpu: Optional[float]
    HaAdmissionControlResourcePercentageMemory: Optional[float]
    HaAdmissionControlSlotPolicyExplicitCpu: Optional[float]
    HaAdmissionControlSlotPolicyExplicitMemory: Optional[float]
    HaAdmissionControlSlotPolicyUseExplicitSize: Optional[bool]
    HaAdvancedOptions: Optional[Sequence["_HaAdvancedOptions"]]
    HaDatastoreApdRecoveryAction: Optional[str]
    HaDatastoreApdResponse: Optional[str]
    HaDatastoreApdResponseDelay: Optional[float]
    HaDatastorePdlResponse: Optional[str]
    HaEnabled: Optional[bool]
    HaHeartbeatDatastoreIds: Optional[Sequence[str]]
    HaHeartbeatDatastorePolicy: Optional[str]
    HaHostIsolationResponse: Optional[str]
    HaHostMonitoring: Optional[str]
    HaVmComponentProtection: Optional[str]
    HaVmDependencyRestartCondition: Optional[str]
    HaVmFailureInterval: Optional[float]
    HaVmMaximumFailureWindow: Optional[float]
    HaVmMaximumResets: Optional[float]
    HaVmMinimumUptime: Optional[float]
    HaVmMonitoring: Optional[str]
    HaVmRestartAdditionalDelay: Optional[float]
    HaVmRestartPriority: Optional[str]
    HaVmRestartTimeout: Optional[float]
    HostClusterExitTimeout: Optional[float]
    HostSystemIds: Optional[Sequence[str]]
    Name: Optional[str]
    ProactiveHaAutomationLevel: Optional[str]
    ProactiveHaEnabled: Optional[bool]
    ProactiveHaModerateRemediation: Optional[str]
    ProactiveHaProviderIds: Optional[Sequence[str]]
    ProactiveHaSevereRemediation: Optional[str]
    ResourcePoolId: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomAttributes=json_data.get("CustomAttributes"),
            DatacenterId=json_data.get("DatacenterId"),
            DpmAutomationLevel=json_data.get("DpmAutomationLevel"),
            DpmEnabled=json_data.get("DpmEnabled"),
            DpmThreshold=json_data.get("DpmThreshold"),
            DrsAdvancedOptions=json_data.get("DrsAdvancedOptions"),
            DrsAutomationLevel=json_data.get("DrsAutomationLevel"),
            DrsEnablePredictiveDrs=json_data.get("DrsEnablePredictiveDrs"),
            DrsEnableVmOverrides=json_data.get("DrsEnableVmOverrides"),
            DrsEnabled=json_data.get("DrsEnabled"),
            DrsMigrationThreshold=json_data.get("DrsMigrationThreshold"),
            Folder=json_data.get("Folder"),
            ForceEvacuateOnDestroy=json_data.get("ForceEvacuateOnDestroy"),
            HaAdmissionControlFailoverHostSystemIds=json_data.get("HaAdmissionControlFailoverHostSystemIds"),
            HaAdmissionControlHostFailureTolerance=json_data.get("HaAdmissionControlHostFailureTolerance"),
            HaAdmissionControlPerformanceTolerance=json_data.get("HaAdmissionControlPerformanceTolerance"),
            HaAdmissionControlPolicy=json_data.get("HaAdmissionControlPolicy"),
            HaAdmissionControlResourcePercentageAutoCompute=json_data.get("HaAdmissionControlResourcePercentageAutoCompute"),
            HaAdmissionControlResourcePercentageCpu=json_data.get("HaAdmissionControlResourcePercentageCpu"),
            HaAdmissionControlResourcePercentageMemory=json_data.get("HaAdmissionControlResourcePercentageMemory"),
            HaAdmissionControlSlotPolicyExplicitCpu=json_data.get("HaAdmissionControlSlotPolicyExplicitCpu"),
            HaAdmissionControlSlotPolicyExplicitMemory=json_data.get("HaAdmissionControlSlotPolicyExplicitMemory"),
            HaAdmissionControlSlotPolicyUseExplicitSize=json_data.get("HaAdmissionControlSlotPolicyUseExplicitSize"),
            HaAdvancedOptions=json_data.get("HaAdvancedOptions"),
            HaDatastoreApdRecoveryAction=json_data.get("HaDatastoreApdRecoveryAction"),
            HaDatastoreApdResponse=json_data.get("HaDatastoreApdResponse"),
            HaDatastoreApdResponseDelay=json_data.get("HaDatastoreApdResponseDelay"),
            HaDatastorePdlResponse=json_data.get("HaDatastorePdlResponse"),
            HaEnabled=json_data.get("HaEnabled"),
            HaHeartbeatDatastoreIds=json_data.get("HaHeartbeatDatastoreIds"),
            HaHeartbeatDatastorePolicy=json_data.get("HaHeartbeatDatastorePolicy"),
            HaHostIsolationResponse=json_data.get("HaHostIsolationResponse"),
            HaHostMonitoring=json_data.get("HaHostMonitoring"),
            HaVmComponentProtection=json_data.get("HaVmComponentProtection"),
            HaVmDependencyRestartCondition=json_data.get("HaVmDependencyRestartCondition"),
            HaVmFailureInterval=json_data.get("HaVmFailureInterval"),
            HaVmMaximumFailureWindow=json_data.get("HaVmMaximumFailureWindow"),
            HaVmMaximumResets=json_data.get("HaVmMaximumResets"),
            HaVmMinimumUptime=json_data.get("HaVmMinimumUptime"),
            HaVmMonitoring=json_data.get("HaVmMonitoring"),
            HaVmRestartAdditionalDelay=json_data.get("HaVmRestartAdditionalDelay"),
            HaVmRestartPriority=json_data.get("HaVmRestartPriority"),
            HaVmRestartTimeout=json_data.get("HaVmRestartTimeout"),
            HostClusterExitTimeout=json_data.get("HostClusterExitTimeout"),
            HostSystemIds=json_data.get("HostSystemIds"),
            Name=json_data.get("Name"),
            ProactiveHaAutomationLevel=json_data.get("ProactiveHaAutomationLevel"),
            ProactiveHaEnabled=json_data.get("ProactiveHaEnabled"),
            ProactiveHaModerateRemediation=json_data.get("ProactiveHaModerateRemediation"),
            ProactiveHaProviderIds=json_data.get("ProactiveHaProviderIds"),
            ProactiveHaSevereRemediation=json_data.get("ProactiveHaSevereRemediation"),
            ResourcePoolId=json_data.get("ResourcePoolId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributes = CustomAttributes


@dataclass
class DrsAdvancedOptions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DrsAdvancedOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrsAdvancedOptions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrsAdvancedOptions = DrsAdvancedOptions


@dataclass
class HaAdvancedOptions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HaAdvancedOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HaAdvancedOptions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HaAdvancedOptions = HaAdvancedOptions


