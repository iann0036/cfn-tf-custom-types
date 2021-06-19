# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
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
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
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
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


