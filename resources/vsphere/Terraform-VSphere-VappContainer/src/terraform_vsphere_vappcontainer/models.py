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
    CpuExpandable: Optional[bool]
    CpuLimit: Optional[float]
    CpuReservation: Optional[float]
    CpuShareLevel: Optional[str]
    CpuShares: Optional[float]
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    Id: Optional[str]
    MemoryExpandable: Optional[bool]
    MemoryLimit: Optional[float]
    MemoryReservation: Optional[float]
    MemoryShareLevel: Optional[str]
    MemoryShares: Optional[float]
    Name: Optional[str]
    ParentFolderId: Optional[str]
    ParentResourcePoolId: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CpuExpandable=json_data.get("CpuExpandable"),
            CpuLimit=json_data.get("CpuLimit"),
            CpuReservation=json_data.get("CpuReservation"),
            CpuShareLevel=json_data.get("CpuShareLevel"),
            CpuShares=json_data.get("CpuShares"),
            CustomAttributes=json_data.get("CustomAttributes"),
            Id=json_data.get("Id"),
            MemoryExpandable=json_data.get("MemoryExpandable"),
            MemoryLimit=json_data.get("MemoryLimit"),
            MemoryReservation=json_data.get("MemoryReservation"),
            MemoryShareLevel=json_data.get("MemoryShareLevel"),
            MemoryShares=json_data.get("MemoryShares"),
            Name=json_data.get("Name"),
            ParentFolderId=json_data.get("ParentFolderId"),
            ParentResourcePoolId=json_data.get("ParentResourcePoolId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributes = CustomAttributes


