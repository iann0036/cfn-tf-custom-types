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
    Bandwidth: Optional[str]
    BaseBandwidth: Optional[str]
    DomainCount: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    PortCount: Optional[str]
    ServiceBandwidth: Optional[str]

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
            BaseBandwidth=json_data.get("BaseBandwidth"),
            DomainCount=json_data.get("DomainCount"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            PortCount=json_data.get("PortCount"),
            ServiceBandwidth=json_data.get("ServiceBandwidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


