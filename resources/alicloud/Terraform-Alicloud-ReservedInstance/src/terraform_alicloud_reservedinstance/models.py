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
    Id: Optional[str]
    InstanceAmount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    OfferingType: Optional[str]
    Period: Optional[float]
    PeriodUnit: Optional[str]
    Platform: Optional[str]
    ResourceGroupId: Optional[str]
    Scope: Optional[str]
    ZoneId: Optional[str]

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
            Id=json_data.get("Id"),
            InstanceAmount=json_data.get("InstanceAmount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            OfferingType=json_data.get("OfferingType"),
            Period=json_data.get("Period"),
            PeriodUnit=json_data.get("PeriodUnit"),
            Platform=json_data.get("Platform"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Scope=json_data.get("Scope"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


