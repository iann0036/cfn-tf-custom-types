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
    AdvertizeRoute: Optional[bool]
    Arp: Optional[bool]
    AutoDelete: Optional[bool]
    ConnLimit: Optional[float]
    Enabled: Optional[bool]
    IcmpEcho: Optional[bool]
    Name: Optional[str]
    TrafficGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdvertizeRoute=json_data.get("AdvertizeRoute"),
            Arp=json_data.get("Arp"),
            AutoDelete=json_data.get("AutoDelete"),
            ConnLimit=json_data.get("ConnLimit"),
            Enabled=json_data.get("Enabled"),
            IcmpEcho=json_data.get("IcmpEcho"),
            Name=json_data.get("Name"),
            TrafficGroup=json_data.get("TrafficGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


