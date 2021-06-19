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
    ConnectionName: Optional[str]
    DeviceBgpAsn: Optional[float]
    DeviceName: Optional[str]
    EnableEventTriggeredHa: Optional[bool]
    EnableGlobalAccelerator: Optional[bool]
    EnableLearnedCidrsApproval: Optional[bool]
    Id: Optional[str]
    LocalTunnelIp: Optional[str]
    ManualBgpAdvertisedCidrs: Optional[Sequence[str]]
    Phase1Authentication: Optional[str]
    Phase1DhGroups: Optional[str]
    Phase1Encryption: Optional[str]
    Phase2Authentication: Optional[str]
    Phase2DhGroups: Optional[str]
    Phase2Encryption: Optional[str]
    PreSharedKey: Optional[str]
    RemoteTunnelIp: Optional[str]
    TransitGatewayBgpAsn: Optional[float]
    TransitGatewayName: Optional[str]
    VpcId: Optional[str]

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
            ConnectionName=json_data.get("ConnectionName"),
            DeviceBgpAsn=json_data.get("DeviceBgpAsn"),
            DeviceName=json_data.get("DeviceName"),
            EnableEventTriggeredHa=json_data.get("EnableEventTriggeredHa"),
            EnableGlobalAccelerator=json_data.get("EnableGlobalAccelerator"),
            EnableLearnedCidrsApproval=json_data.get("EnableLearnedCidrsApproval"),
            Id=json_data.get("Id"),
            LocalTunnelIp=json_data.get("LocalTunnelIp"),
            ManualBgpAdvertisedCidrs=json_data.get("ManualBgpAdvertisedCidrs"),
            Phase1Authentication=json_data.get("Phase1Authentication"),
            Phase1DhGroups=json_data.get("Phase1DhGroups"),
            Phase1Encryption=json_data.get("Phase1Encryption"),
            Phase2Authentication=json_data.get("Phase2Authentication"),
            Phase2DhGroups=json_data.get("Phase2DhGroups"),
            Phase2Encryption=json_data.get("Phase2Encryption"),
            PreSharedKey=json_data.get("PreSharedKey"),
            RemoteTunnelIp=json_data.get("RemoteTunnelIp"),
            TransitGatewayBgpAsn=json_data.get("TransitGatewayBgpAsn"),
            TransitGatewayName=json_data.get("TransitGatewayName"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


