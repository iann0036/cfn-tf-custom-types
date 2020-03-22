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
    Bandwidth: Optional[float]
    ChargeType: Optional[str]
    Description: Optional[str]
    ExpiredTime: Optional[str]
    GeographicRegionIds: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bandwidth=json_data.get("Bandwidth"),
            ChargeType=json_data.get("ChargeType"),
            Description=json_data.get("Description"),
            ExpiredTime=json_data.get("ExpiredTime"),
            GeographicRegionIds=json_data.get("GeographicRegionIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


