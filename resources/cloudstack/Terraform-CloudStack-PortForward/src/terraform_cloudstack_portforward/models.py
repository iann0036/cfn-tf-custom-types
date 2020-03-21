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
    IpAddressId: Optional[str]
    Managed: Optional[bool]
    Project: Optional[str]
    Forward: Optional[Sequence["_Forward"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            IpAddressId=json_data.get("IpAddressId"),
            Managed=json_data.get("Managed"),
            Project=json_data.get("Project"),
            Forward=json_data.get("Forward"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Forward:
    PrivatePort: Optional[float]
    Protocol: Optional[str]
    PublicPort: Optional[float]
    VirtualMachineId: Optional[str]
    VmGuestIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Forward"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Forward"]:
        if not json_data:
            return None
        return cls(
            PrivatePort=json_data.get("PrivatePort"),
            Protocol=json_data.get("Protocol"),
            PublicPort=json_data.get("PublicPort"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            VmGuestIp=json_data.get("VmGuestIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Forward = Forward


