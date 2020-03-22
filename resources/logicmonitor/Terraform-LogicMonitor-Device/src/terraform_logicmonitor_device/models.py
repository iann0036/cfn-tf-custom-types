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
    Collector: Optional[float]
    Description: Optional[str]
    DisableAlerting: Optional[bool]
    DisplayName: Optional[str]
    HostgroupId: Optional[str]
    Id: Optional[str]
    IpAddr: Optional[str]
    Properties: Optional[Sequence["_Properties"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Collector=json_data.get("Collector"),
            Description=json_data.get("Description"),
            DisableAlerting=json_data.get("DisableAlerting"),
            DisplayName=json_data.get("DisplayName"),
            HostgroupId=json_data.get("HostgroupId"),
            Id=json_data.get("Id"),
            IpAddr=json_data.get("IpAddr"),
            Properties=json_data.get("Properties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Properties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


