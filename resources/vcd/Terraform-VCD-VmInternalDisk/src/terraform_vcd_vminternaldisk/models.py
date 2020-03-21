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
    AllowVmReboot: Optional[bool]
    BusNumber: Optional[float]
    BusType: Optional[str]
    Iops: Optional[float]
    Org: Optional[str]
    SizeInMb: Optional[float]
    StorageProfile: Optional[str]
    ThinProvisioned: Optional[bool]
    UnitNumber: Optional[float]
    VappName: Optional[str]
    Vdc: Optional[str]
    VmName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowVmReboot=json_data.get("AllowVmReboot"),
            BusNumber=json_data.get("BusNumber"),
            BusType=json_data.get("BusType"),
            Iops=json_data.get("Iops"),
            Org=json_data.get("Org"),
            SizeInMb=json_data.get("SizeInMb"),
            StorageProfile=json_data.get("StorageProfile"),
            ThinProvisioned=json_data.get("ThinProvisioned"),
            UnitNumber=json_data.get("UnitNumber"),
            VappName=json_data.get("VappName"),
            Vdc=json_data.get("Vdc"),
            VmName=json_data.get("VmName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


