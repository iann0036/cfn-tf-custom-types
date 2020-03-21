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
    Cidr: Optional[str]
    DataCidr: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Organization: Optional[str]
    OutboundIps: Optional[Sequence[str]]
    Region: Optional[str]
    Shield: Optional[bool]
    TrustedIpRanges: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cidr=json_data.get("Cidr"),
            DataCidr=json_data.get("DataCidr"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Organization=json_data.get("Organization"),
            OutboundIps=json_data.get("OutboundIps"),
            Region=json_data.get("Region"),
            Shield=json_data.get("Shield"),
            TrustedIpRanges=json_data.get("TrustedIpRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


