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
    AllowedPrefixes: Optional[Sequence[str]]
    AssociatedGatewayId: Optional[str]
    AssociatedGatewayOwnerAccountId: Optional[str]
    AssociatedGatewayType: Optional[str]
    DxGatewayAssociationId: Optional[str]
    DxGatewayId: Optional[str]
    DxGatewayOwnerAccountId: Optional[str]
    Id: Optional[str]
    ProposalId: Optional[str]
    VpnGatewayId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedPrefixes=json_data.get("AllowedPrefixes"),
            AssociatedGatewayId=json_data.get("AssociatedGatewayId"),
            AssociatedGatewayOwnerAccountId=json_data.get("AssociatedGatewayOwnerAccountId"),
            AssociatedGatewayType=json_data.get("AssociatedGatewayType"),
            DxGatewayAssociationId=json_data.get("DxGatewayAssociationId"),
            DxGatewayId=json_data.get("DxGatewayId"),
            DxGatewayOwnerAccountId=json_data.get("DxGatewayOwnerAccountId"),
            Id=json_data.get("Id"),
            ProposalId=json_data.get("ProposalId"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


