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
    CloudRef: Optional[str]
    Dhcp6Ranges: Optional[Sequence[str]]
    DhcpEnabled: Optional[bool]
    DhcpRanges: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    NwName: Optional[str]
    NwRef: Optional[str]
    OpaqueNetworkId: Optional[str]
    SegmentGw: Optional[str]
    SegmentGw6: Optional[str]
    SegmentId: Optional[str]
    Segname: Optional[str]
    Subnet: Optional[str]
    Subnet6: Optional[str]
    TenantRef: Optional[str]
    Tier1Id: Optional[str]
    Uuid: Optional[str]
    VlanIds: Optional[Sequence[str]]
    VrfContextRef: Optional[str]

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
            CloudRef=json_data.get("CloudRef"),
            Dhcp6Ranges=json_data.get("Dhcp6Ranges"),
            DhcpEnabled=json_data.get("DhcpEnabled"),
            DhcpRanges=json_data.get("DhcpRanges"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NwName=json_data.get("NwName"),
            NwRef=json_data.get("NwRef"),
            OpaqueNetworkId=json_data.get("OpaqueNetworkId"),
            SegmentGw=json_data.get("SegmentGw"),
            SegmentGw6=json_data.get("SegmentGw6"),
            SegmentId=json_data.get("SegmentId"),
            Segname=json_data.get("Segname"),
            Subnet=json_data.get("Subnet"),
            Subnet6=json_data.get("Subnet6"),
            TenantRef=json_data.get("TenantRef"),
            Tier1Id=json_data.get("Tier1Id"),
            Uuid=json_data.get("Uuid"),
            VlanIds=json_data.get("VlanIds"),
            VrfContextRef=json_data.get("VrfContextRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


