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
    AllowEthernetBridging: Optional[bool]
    Authorized: Optional[bool]
    Capabilities: Optional[Sequence[float]]
    Description: Optional[str]
    Hidden: Optional[bool]
    Id: Optional[str]
    IpAssignments: Optional[Sequence[str]]
    MemberId: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    NoAutoAssignIps: Optional[bool]

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
            AllowEthernetBridging=json_data.get("AllowEthernetBridging"),
            Authorized=json_data.get("Authorized"),
            Capabilities=json_data.get("Capabilities"),
            Description=json_data.get("Description"),
            Hidden=json_data.get("Hidden"),
            Id=json_data.get("Id"),
            IpAssignments=json_data.get("IpAssignments"),
            MemberId=json_data.get("MemberId"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NoAutoAssignIps=json_data.get("NoAutoAssignIps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


