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
    Address: Optional[str]
    AddressFamily: Optional[float]
    Cidr: Optional[float]
    CidrNotation: Optional[str]
    Description: Optional[str]
    Facility: Optional[str]
    Gateway: Optional[str]
    Global: Optional[bool]
    Id: Optional[str]
    Manageable: Optional[bool]
    Management: Optional[bool]
    Metro: Optional[str]
    Netmask: Optional[str]
    Network: Optional[str]
    ProjectId: Optional[str]
    Public: Optional[bool]
    Quantity: Optional[float]
    Type: Optional[str]

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
            Address=json_data.get("Address"),
            AddressFamily=json_data.get("AddressFamily"),
            Cidr=json_data.get("Cidr"),
            CidrNotation=json_data.get("CidrNotation"),
            Description=json_data.get("Description"),
            Facility=json_data.get("Facility"),
            Gateway=json_data.get("Gateway"),
            Global=json_data.get("Global"),
            Id=json_data.get("Id"),
            Manageable=json_data.get("Manageable"),
            Management=json_data.get("Management"),
            Metro=json_data.get("Metro"),
            Netmask=json_data.get("Netmask"),
            Network=json_data.get("Network"),
            ProjectId=json_data.get("ProjectId"),
            Public=json_data.get("Public"),
            Quantity=json_data.get("Quantity"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


