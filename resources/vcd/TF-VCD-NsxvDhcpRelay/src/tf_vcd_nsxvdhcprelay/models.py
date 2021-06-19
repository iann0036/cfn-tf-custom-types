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
    DomainNames: Optional[Sequence[str]]
    EdgeGateway: Optional[str]
    Id: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    IpSets: Optional[Sequence[str]]
    Org: Optional[str]
    Vdc: Optional[str]
    RelayAgent: Optional[Sequence["_RelayAgentDefinition"]]

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
            DomainNames=json_data.get("DomainNames"),
            EdgeGateway=json_data.get("EdgeGateway"),
            Id=json_data.get("Id"),
            IpAddresses=json_data.get("IpAddresses"),
            IpSets=json_data.get("IpSets"),
            Org=json_data.get("Org"),
            Vdc=json_data.get("Vdc"),
            RelayAgent=deserialize_list(json_data.get("RelayAgent"), RelayAgentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelayAgentDefinition(BaseModel):
    GatewayIpAddress: Optional[str]
    NetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelayAgentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelayAgentDefinition"]:
        if not json_data:
            return None
        return cls(
            GatewayIpAddress=json_data.get("GatewayIpAddress"),
            NetworkName=json_data.get("NetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelayAgentDefinition = RelayAgentDefinition


