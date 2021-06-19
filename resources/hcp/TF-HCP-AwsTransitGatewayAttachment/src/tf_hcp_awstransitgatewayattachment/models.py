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
    CreatedAt: Optional[str]
    ExpiresAt: Optional[str]
    HvnId: Optional[str]
    Id: Optional[str]
    OrganizationId: Optional[str]
    ProjectId: Optional[str]
    ProviderTransitGatewayAttachmentId: Optional[str]
    ResourceShareArn: Optional[str]
    SelfLink: Optional[str]
    State: Optional[str]
    TransitGatewayAttachmentId: Optional[str]
    TransitGatewayId: Optional[str]
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
            CreatedAt=json_data.get("CreatedAt"),
            ExpiresAt=json_data.get("ExpiresAt"),
            HvnId=json_data.get("HvnId"),
            Id=json_data.get("Id"),
            OrganizationId=json_data.get("OrganizationId"),
            ProjectId=json_data.get("ProjectId"),
            ProviderTransitGatewayAttachmentId=json_data.get("ProviderTransitGatewayAttachmentId"),
            ResourceShareArn=json_data.get("ResourceShareArn"),
            SelfLink=json_data.get("SelfLink"),
            State=json_data.get("State"),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


