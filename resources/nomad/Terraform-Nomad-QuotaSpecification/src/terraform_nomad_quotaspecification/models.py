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
    Description: Optional[str]
    Name: Optional[str]
    Limits: Optional[Sequence["_Limits"]]
    RegionLimit: Optional[Sequence["_RegionLimit"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Limits=json_data.get("Limits"),
            RegionLimit=json_data.get("RegionLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Limits:
    Region: Optional[str]
    RegionLimit: Optional[Sequence["_RegionLimit"]]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            RegionLimit=json_data.get("RegionLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class RegionLimit:
    Cpu: Optional[float]
    MemoryMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RegionLimit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionLimit"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            MemoryMb=json_data.get("MemoryMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionLimit = RegionLimit


