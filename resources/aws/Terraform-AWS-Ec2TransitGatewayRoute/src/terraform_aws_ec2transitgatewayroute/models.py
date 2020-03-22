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
    Blackhole: Optional[bool]
    DestinationCidrBlock: Optional[str]
    Id: Optional[str]
    TransitGatewayAttachmentId: Optional[str]
    TransitGatewayRouteTableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Blackhole=json_data.get("Blackhole"),
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            Id=json_data.get("Id"),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransitGatewayRouteTableId=json_data.get("TransitGatewayRouteTableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


