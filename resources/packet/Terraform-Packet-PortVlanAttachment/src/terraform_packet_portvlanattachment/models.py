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
    DeviceId: Optional[str]
    ForceBond: Optional[bool]
    Native: Optional[bool]
    PortId: Optional[str]
    PortName: Optional[str]
    VlanId: Optional[str]
    VlanVnid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeviceId=json_data.get("DeviceId"),
            ForceBond=json_data.get("ForceBond"),
            Native=json_data.get("Native"),
            PortId=json_data.get("PortId"),
            PortName=json_data.get("PortName"),
            VlanId=json_data.get("VlanId"),
            VlanVnid=json_data.get("VlanVnid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


