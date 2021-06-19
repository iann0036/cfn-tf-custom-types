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
    EnableInsaneModeEncryptionOverInternet: Optional[bool]
    EnablePeeringOverPrivateNetwork: Optional[bool]
    EnableSingleTunnelMode: Optional[bool]
    Gateway1ExcludedNetworkCidrs: Optional[Sequence[str]]
    Gateway1ExcludedTgwConnections: Optional[Sequence[str]]
    Gateway2ExcludedNetworkCidrs: Optional[Sequence[str]]
    Gateway2ExcludedTgwConnections: Optional[Sequence[str]]
    Id: Optional[str]
    PrependAsPath1: Optional[Sequence[str]]
    PrependAsPath2: Optional[Sequence[str]]
    TransitGatewayName1: Optional[str]
    TransitGatewayName2: Optional[str]
    TunnelCount: Optional[float]

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
            EnableInsaneModeEncryptionOverInternet=json_data.get("EnableInsaneModeEncryptionOverInternet"),
            EnablePeeringOverPrivateNetwork=json_data.get("EnablePeeringOverPrivateNetwork"),
            EnableSingleTunnelMode=json_data.get("EnableSingleTunnelMode"),
            Gateway1ExcludedNetworkCidrs=json_data.get("Gateway1ExcludedNetworkCidrs"),
            Gateway1ExcludedTgwConnections=json_data.get("Gateway1ExcludedTgwConnections"),
            Gateway2ExcludedNetworkCidrs=json_data.get("Gateway2ExcludedNetworkCidrs"),
            Gateway2ExcludedTgwConnections=json_data.get("Gateway2ExcludedTgwConnections"),
            Id=json_data.get("Id"),
            PrependAsPath1=json_data.get("PrependAsPath1"),
            PrependAsPath2=json_data.get("PrependAsPath2"),
            TransitGatewayName1=json_data.get("TransitGatewayName1"),
            TransitGatewayName2=json_data.get("TransitGatewayName2"),
            TunnelCount=json_data.get("TunnelCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


