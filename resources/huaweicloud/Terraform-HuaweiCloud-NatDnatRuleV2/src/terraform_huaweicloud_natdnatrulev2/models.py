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
    CreatedAt: Optional[str]
    ExternalServicePort: Optional[float]
    FloatingIpAddress: Optional[str]
    FloatingIpId: Optional[str]
    Id: Optional[str]
    InternalServicePort: Optional[float]
    NatGatewayId: Optional[str]
    PortId: Optional[str]
    PrivateIp: Optional[str]
    Protocol: Optional[str]
    Status: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreatedAt=json_data.get("CreatedAt"),
            ExternalServicePort=json_data.get("ExternalServicePort"),
            FloatingIpAddress=json_data.get("FloatingIpAddress"),
            FloatingIpId=json_data.get("FloatingIpId"),
            Id=json_data.get("Id"),
            InternalServicePort=json_data.get("InternalServicePort"),
            NatGatewayId=json_data.get("NatGatewayId"),
            PortId=json_data.get("PortId"),
            PrivateIp=json_data.get("PrivateIp"),
            Protocol=json_data.get("Protocol"),
            Status=json_data.get("Status"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


