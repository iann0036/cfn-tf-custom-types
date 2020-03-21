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
    Cipher: Optional[str]
    ClientIpPool: Optional[str]
    Compress: Optional[bool]
    Connections: Optional[float]
    Id: Optional[str]
    InternetIp: Optional[str]
    LocalSubnet: Optional[str]
    MaxConnections: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    VpnGatewayId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cipher=json_data.get("Cipher"),
            ClientIpPool=json_data.get("ClientIpPool"),
            Compress=json_data.get("Compress"),
            Connections=json_data.get("Connections"),
            Id=json_data.get("Id"),
            InternetIp=json_data.get("InternetIp"),
            LocalSubnet=json_data.get("LocalSubnet"),
            MaxConnections=json_data.get("MaxConnections"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


