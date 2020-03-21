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
    ActiveUplinks: Optional[Sequence[str]]
    AllowForgedTransmits: Optional[bool]
    AllowMacChanges: Optional[bool]
    AllowPromiscuous: Optional[bool]
    AutoExpand: Optional[bool]
    BlockAllPorts: Optional[bool]
    BlockOverrideAllowed: Optional[bool]
    CheckBeacon: Optional[bool]
    ConfigVersion: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    Description: Optional[str]
    DirectpathGen2Allowed: Optional[bool]
    DistributedVirtualSwitchUuid: Optional[str]
    EgressShapingAverageBandwidth: Optional[float]
    EgressShapingBurstSize: Optional[float]
    EgressShapingEnabled: Optional[bool]
    EgressShapingPeakBandwidth: Optional[float]
    Failback: Optional[bool]
    IngressShapingAverageBandwidth: Optional[float]
    IngressShapingBurstSize: Optional[float]
    IngressShapingEnabled: Optional[bool]
    IngressShapingPeakBandwidth: Optional[float]
    Key: Optional[str]
    LacpEnabled: Optional[bool]
    LacpMode: Optional[str]
    LivePortMovingAllowed: Optional[bool]
    Name: Optional[str]
    NetflowEnabled: Optional[bool]
    NetflowOverrideAllowed: Optional[bool]
    NetworkResourcePoolKey: Optional[str]
    NetworkResourcePoolOverrideAllowed: Optional[bool]
    NotifySwitches: Optional[bool]
    NumberOfPorts: Optional[float]
    PortConfigResetAtDisconnect: Optional[bool]
    PortNameFormat: Optional[str]
    PortPrivateSecondaryVlanId: Optional[float]
    SecurityPolicyOverrideAllowed: Optional[bool]
    ShapingOverrideAllowed: Optional[bool]
    StandbyUplinks: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    TeamingPolicy: Optional[str]
    TrafficFilterOverrideAllowed: Optional[bool]
    TxUplink: Optional[bool]
    Type: Optional[str]
    UplinkTeamingOverrideAllowed: Optional[bool]
    VlanId: Optional[float]
    VlanOverrideAllowed: Optional[bool]
    VlanRange: Optional[Sequence["_VlanRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActiveUplinks=json_data.get("ActiveUplinks"),
            AllowForgedTransmits=json_data.get("AllowForgedTransmits"),
            AllowMacChanges=json_data.get("AllowMacChanges"),
            AllowPromiscuous=json_data.get("AllowPromiscuous"),
            AutoExpand=json_data.get("AutoExpand"),
            BlockAllPorts=json_data.get("BlockAllPorts"),
            BlockOverrideAllowed=json_data.get("BlockOverrideAllowed"),
            CheckBeacon=json_data.get("CheckBeacon"),
            ConfigVersion=json_data.get("ConfigVersion"),
            CustomAttributes=json_data.get("CustomAttributes"),
            Description=json_data.get("Description"),
            DirectpathGen2Allowed=json_data.get("DirectpathGen2Allowed"),
            DistributedVirtualSwitchUuid=json_data.get("DistributedVirtualSwitchUuid"),
            EgressShapingAverageBandwidth=json_data.get("EgressShapingAverageBandwidth"),
            EgressShapingBurstSize=json_data.get("EgressShapingBurstSize"),
            EgressShapingEnabled=json_data.get("EgressShapingEnabled"),
            EgressShapingPeakBandwidth=json_data.get("EgressShapingPeakBandwidth"),
            Failback=json_data.get("Failback"),
            IngressShapingAverageBandwidth=json_data.get("IngressShapingAverageBandwidth"),
            IngressShapingBurstSize=json_data.get("IngressShapingBurstSize"),
            IngressShapingEnabled=json_data.get("IngressShapingEnabled"),
            IngressShapingPeakBandwidth=json_data.get("IngressShapingPeakBandwidth"),
            Key=json_data.get("Key"),
            LacpEnabled=json_data.get("LacpEnabled"),
            LacpMode=json_data.get("LacpMode"),
            LivePortMovingAllowed=json_data.get("LivePortMovingAllowed"),
            Name=json_data.get("Name"),
            NetflowEnabled=json_data.get("NetflowEnabled"),
            NetflowOverrideAllowed=json_data.get("NetflowOverrideAllowed"),
            NetworkResourcePoolKey=json_data.get("NetworkResourcePoolKey"),
            NetworkResourcePoolOverrideAllowed=json_data.get("NetworkResourcePoolOverrideAllowed"),
            NotifySwitches=json_data.get("NotifySwitches"),
            NumberOfPorts=json_data.get("NumberOfPorts"),
            PortConfigResetAtDisconnect=json_data.get("PortConfigResetAtDisconnect"),
            PortNameFormat=json_data.get("PortNameFormat"),
            PortPrivateSecondaryVlanId=json_data.get("PortPrivateSecondaryVlanId"),
            SecurityPolicyOverrideAllowed=json_data.get("SecurityPolicyOverrideAllowed"),
            ShapingOverrideAllowed=json_data.get("ShapingOverrideAllowed"),
            StandbyUplinks=json_data.get("StandbyUplinks"),
            Tags=json_data.get("Tags"),
            TeamingPolicy=json_data.get("TeamingPolicy"),
            TrafficFilterOverrideAllowed=json_data.get("TrafficFilterOverrideAllowed"),
            TxUplink=json_data.get("TxUplink"),
            Type=json_data.get("Type"),
            UplinkTeamingOverrideAllowed=json_data.get("UplinkTeamingOverrideAllowed"),
            VlanId=json_data.get("VlanId"),
            VlanOverrideAllowed=json_data.get("VlanOverrideAllowed"),
            VlanRange=json_data.get("VlanRange"),
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
class VlanRange:
    MaxVlan: Optional[float]
    MinVlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VlanRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VlanRange"]:
        if not json_data:
            return None
        return cls(
            MaxVlan=json_data.get("MaxVlan"),
            MinVlan=json_data.get("MinVlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VlanRange = VlanRange


