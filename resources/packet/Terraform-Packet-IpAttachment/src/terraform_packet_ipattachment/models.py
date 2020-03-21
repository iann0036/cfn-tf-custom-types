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
    Address: Optional[str]
    AddressFamily: Optional[float]
    Cidr: Optional[float]
    CidrNotation: Optional[str]
    DeviceId: Optional[str]
    Gateway: Optional[str]
    Global: Optional[bool]
    Id: Optional[str]
    Manageable: Optional[bool]
    Management: Optional[bool]
    Netmask: Optional[str]
    Network: Optional[str]
    Public: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Address=json_data.get("Address"),
            AddressFamily=json_data.get("AddressFamily"),
            Cidr=json_data.get("Cidr"),
            CidrNotation=json_data.get("CidrNotation"),
            DeviceId=json_data.get("DeviceId"),
            Gateway=json_data.get("Gateway"),
            Global=json_data.get("Global"),
            Id=json_data.get("Id"),
            Manageable=json_data.get("Manageable"),
            Management=json_data.get("Management"),
            Netmask=json_data.get("Netmask"),
            Network=json_data.get("Network"),
            Public=json_data.get("Public"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


