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
    ArpSuppFlag: Optional[bool]
    Deploy: Optional[bool]
    DeployTimeout: Optional[float]
    Description: Optional[str]
    Dhcp1: Optional[str]
    Dhcp2: Optional[str]
    DhcpVrf: Optional[str]
    DisplayName: Optional[str]
    ExtensionTemplate: Optional[str]
    FabricName: Optional[str]
    Id: Optional[str]
    Ipv4Gateway: Optional[str]
    Ipv6Gateway: Optional[str]
    IrEnableFlag: Optional[bool]
    L2OnlyFlag: Optional[bool]
    L3GatewayFlag: Optional[bool]
    LoopbackId: Optional[float]
    McastGroup: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    NetworkId: Optional[str]
    RtBothFlag: Optional[bool]
    SecondaryGw1: Optional[str]
    SecondaryGw2: Optional[str]
    ServiceTemplate: Optional[str]
    Source: Optional[str]
    Tag: Optional[str]
    Template: Optional[str]
    TrmEnableFlag: Optional[bool]
    VlanId: Optional[float]
    VlanName: Optional[str]
    VrfName: Optional[str]
    Attachments: Optional[Sequence["_AttachmentsDefinition"]]

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
            ArpSuppFlag=json_data.get("ArpSuppFlag"),
            Deploy=json_data.get("Deploy"),
            DeployTimeout=json_data.get("DeployTimeout"),
            Description=json_data.get("Description"),
            Dhcp1=json_data.get("Dhcp1"),
            Dhcp2=json_data.get("Dhcp2"),
            DhcpVrf=json_data.get("DhcpVrf"),
            DisplayName=json_data.get("DisplayName"),
            ExtensionTemplate=json_data.get("ExtensionTemplate"),
            FabricName=json_data.get("FabricName"),
            Id=json_data.get("Id"),
            Ipv4Gateway=json_data.get("Ipv4Gateway"),
            Ipv6Gateway=json_data.get("Ipv6Gateway"),
            IrEnableFlag=json_data.get("IrEnableFlag"),
            L2OnlyFlag=json_data.get("L2OnlyFlag"),
            L3GatewayFlag=json_data.get("L3GatewayFlag"),
            LoopbackId=json_data.get("LoopbackId"),
            McastGroup=json_data.get("McastGroup"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            RtBothFlag=json_data.get("RtBothFlag"),
            SecondaryGw1=json_data.get("SecondaryGw1"),
            SecondaryGw2=json_data.get("SecondaryGw2"),
            ServiceTemplate=json_data.get("ServiceTemplate"),
            Source=json_data.get("Source"),
            Tag=json_data.get("Tag"),
            Template=json_data.get("Template"),
            TrmEnableFlag=json_data.get("TrmEnableFlag"),
            VlanId=json_data.get("VlanId"),
            VlanName=json_data.get("VlanName"),
            VrfName=json_data.get("VrfName"),
            Attachments=deserialize_list(json_data.get("Attachments"), AttachmentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttachmentsDefinition(BaseModel):
    Attach: Optional[bool]
    Dot1Qvlan: Optional[float]
    ExtensionValues: Optional[str]
    FreeFromConfig: Optional[str]
    InstanceValues: Optional[str]
    SerialNumber: Optional[str]
    SwitchPorts: Optional[Sequence[str]]
    Untagged: Optional[bool]
    VlanId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Attach=json_data.get("Attach"),
            Dot1Qvlan=json_data.get("Dot1Qvlan"),
            ExtensionValues=json_data.get("ExtensionValues"),
            FreeFromConfig=json_data.get("FreeFromConfig"),
            InstanceValues=json_data.get("InstanceValues"),
            SerialNumber=json_data.get("SerialNumber"),
            SwitchPorts=json_data.get("SwitchPorts"),
            Untagged=json_data.get("Untagged"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentsDefinition = AttachmentsDefinition


