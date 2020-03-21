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
    Name: Optional[str]
    ProjectId: Optional[str]
    Regions: Optional[Sequence[str]]
    RegionsStatus: Optional[Sequence["_RegionsStatus"]]
    Status: Optional[str]
    Type: Optional[str]
    VlanId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            Regions=json_data.get("Regions"),
            RegionsStatus=json_data.get("RegionsStatus"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RegionsStatus:
    Region: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionsStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionsStatus"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionsStatus = RegionsStatus


