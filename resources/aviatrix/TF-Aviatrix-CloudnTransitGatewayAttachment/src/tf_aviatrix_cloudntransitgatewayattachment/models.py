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
    CloudnBgpAsn: Optional[str]
    CloudnLanInterfaceNeighborBgpAsn: Optional[str]
    CloudnLanInterfaceNeighborIp: Optional[str]
    ConnectionName: Optional[str]
    DeviceName: Optional[str]
    EnableDeadPeerDetection: Optional[bool]
    EnableJumboFrame: Optional[bool]
    EnableOverPrivateNetwork: Optional[bool]
    Id: Optional[str]
    TransitGatewayBgpAsn: Optional[str]
    TransitGatewayName: Optional[str]

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
            CloudnBgpAsn=json_data.get("CloudnBgpAsn"),
            CloudnLanInterfaceNeighborBgpAsn=json_data.get("CloudnLanInterfaceNeighborBgpAsn"),
            CloudnLanInterfaceNeighborIp=json_data.get("CloudnLanInterfaceNeighborIp"),
            ConnectionName=json_data.get("ConnectionName"),
            DeviceName=json_data.get("DeviceName"),
            EnableDeadPeerDetection=json_data.get("EnableDeadPeerDetection"),
            EnableJumboFrame=json_data.get("EnableJumboFrame"),
            EnableOverPrivateNetwork=json_data.get("EnableOverPrivateNetwork"),
            Id=json_data.get("Id"),
            TransitGatewayBgpAsn=json_data.get("TransitGatewayBgpAsn"),
            TransitGatewayName=json_data.get("TransitGatewayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


