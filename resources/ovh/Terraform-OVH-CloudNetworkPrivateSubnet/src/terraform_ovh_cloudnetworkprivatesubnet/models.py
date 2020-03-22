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
    Cidr: Optional[str]
    Dhcp: Optional[bool]
    End: Optional[str]
    GatewayIp: Optional[str]
    Id: Optional[str]
    IpPools: Optional[Sequence["_IpPools"]]
    Network: Optional[str]
    NetworkId: Optional[str]
    NoGateway: Optional[bool]
    ProjectId: Optional[str]
    Region: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cidr=json_data.get("Cidr"),
            Dhcp=json_data.get("Dhcp"),
            End=json_data.get("End"),
            GatewayIp=json_data.get("GatewayIp"),
            Id=json_data.get("Id"),
            IpPools=json_data.get("IpPools"),
            Network=json_data.get("Network"),
            NetworkId=json_data.get("NetworkId"),
            NoGateway=json_data.get("NoGateway"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpPools:
    Dhcp: Optional[bool]
    End: Optional[str]
    Network: Optional[str]
    Region: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpPools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPools"]:
        if not json_data:
            return None
        return cls(
            Dhcp=json_data.get("Dhcp"),
            End=json_data.get("End"),
            Network=json_data.get("Network"),
            Region=json_data.get("Region"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPools = IpPools


