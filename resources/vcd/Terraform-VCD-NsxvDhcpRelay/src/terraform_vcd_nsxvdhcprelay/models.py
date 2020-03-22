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
    DomainNames: Optional[Sequence[str]]
    EdgeGateway: Optional[str]
    Id: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    IpSets: Optional[Sequence[str]]
    Org: Optional[str]
    Vdc: Optional[str]
    RelayAgent: Optional[Sequence["_RelayAgent"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DomainNames=json_data.get("DomainNames"),
            EdgeGateway=json_data.get("EdgeGateway"),
            Id=json_data.get("Id"),
            IpAddresses=json_data.get("IpAddresses"),
            IpSets=json_data.get("IpSets"),
            Org=json_data.get("Org"),
            Vdc=json_data.get("Vdc"),
            RelayAgent=json_data.get("RelayAgent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelayAgent:
    GatewayIpAddress: Optional[str]
    NetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelayAgent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelayAgent"]:
        if not json_data:
            return None
        return cls(
            GatewayIpAddress=json_data.get("GatewayIpAddress"),
            NetworkName=json_data.get("NetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelayAgent = RelayAgent


