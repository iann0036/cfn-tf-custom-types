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
    CgwId: Optional[str]
    Cnps: Optional[str]
    Id: Optional[str]
    RouterId: Optional[str]
    TfId: Optional[str]
    TgwId: Optional[str]
    Tunnel1AwsEndpointIp: Optional[str]
    Tunnel1AwsOverlayIp: Optional[str]
    Tunnel1BgpAsn: Optional[str]
    Tunnel1BgpHoldtime: Optional[str]
    Tunnel1PresharedKey: Optional[str]
    Tunnel1RouterOverlayIp: Optional[str]
    Tunnel2AwsEndpointIp: Optional[str]
    Tunnel2AwsOverlayIp: Optional[str]
    Tunnel2BgpAsn: Optional[str]
    Tunnel2BgpHoldtime: Optional[str]
    Tunnel2PresharedKey: Optional[str]
    Tunnel2RouterOverlayIp: Optional[str]
    VpcId: Optional[str]
    VpnConnectionId: Optional[str]
    VpnGatewayId: Optional[str]
    VpnTgwAttachmentId: Optional[str]

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
            CgwId=json_data.get("CgwId"),
            Cnps=json_data.get("Cnps"),
            Id=json_data.get("Id"),
            RouterId=json_data.get("RouterId"),
            TfId=json_data.get("TfId"),
            TgwId=json_data.get("TgwId"),
            Tunnel1AwsEndpointIp=json_data.get("Tunnel1AwsEndpointIp"),
            Tunnel1AwsOverlayIp=json_data.get("Tunnel1AwsOverlayIp"),
            Tunnel1BgpAsn=json_data.get("Tunnel1BgpAsn"),
            Tunnel1BgpHoldtime=json_data.get("Tunnel1BgpHoldtime"),
            Tunnel1PresharedKey=json_data.get("Tunnel1PresharedKey"),
            Tunnel1RouterOverlayIp=json_data.get("Tunnel1RouterOverlayIp"),
            Tunnel2AwsEndpointIp=json_data.get("Tunnel2AwsEndpointIp"),
            Tunnel2AwsOverlayIp=json_data.get("Tunnel2AwsOverlayIp"),
            Tunnel2BgpAsn=json_data.get("Tunnel2BgpAsn"),
            Tunnel2BgpHoldtime=json_data.get("Tunnel2BgpHoldtime"),
            Tunnel2PresharedKey=json_data.get("Tunnel2PresharedKey"),
            Tunnel2RouterOverlayIp=json_data.get("Tunnel2RouterOverlayIp"),
            VpcId=json_data.get("VpcId"),
            VpnConnectionId=json_data.get("VpnConnectionId"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            VpnTgwAttachmentId=json_data.get("VpnTgwAttachmentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


