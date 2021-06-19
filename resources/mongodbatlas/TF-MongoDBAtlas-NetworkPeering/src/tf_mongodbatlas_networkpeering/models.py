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
    AccepterRegionName: Optional[str]
    AtlasCidrBlock: Optional[str]
    AtlasGcpProjectId: Optional[str]
    AtlasId: Optional[str]
    AtlasVpcName: Optional[str]
    AwsAccountId: Optional[str]
    AzureDirectoryId: Optional[str]
    AzureSubscriptionId: Optional[str]
    ConnectionId: Optional[str]
    ContainerId: Optional[str]
    ErrorMessage: Optional[str]
    ErrorState: Optional[str]
    ErrorStateName: Optional[str]
    GcpProjectId: Optional[str]
    Id: Optional[str]
    NetworkName: Optional[str]
    PeerId: Optional[str]
    ProjectId: Optional[str]
    ProviderName: Optional[str]
    ResourceGroupName: Optional[str]
    RouteTableCidrBlock: Optional[str]
    Status: Optional[str]
    StatusName: Optional[str]
    VnetName: Optional[str]
    VpcId: Optional[str]

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
            AccepterRegionName=json_data.get("AccepterRegionName"),
            AtlasCidrBlock=json_data.get("AtlasCidrBlock"),
            AtlasGcpProjectId=json_data.get("AtlasGcpProjectId"),
            AtlasId=json_data.get("AtlasId"),
            AtlasVpcName=json_data.get("AtlasVpcName"),
            AwsAccountId=json_data.get("AwsAccountId"),
            AzureDirectoryId=json_data.get("AzureDirectoryId"),
            AzureSubscriptionId=json_data.get("AzureSubscriptionId"),
            ConnectionId=json_data.get("ConnectionId"),
            ContainerId=json_data.get("ContainerId"),
            ErrorMessage=json_data.get("ErrorMessage"),
            ErrorState=json_data.get("ErrorState"),
            ErrorStateName=json_data.get("ErrorStateName"),
            GcpProjectId=json_data.get("GcpProjectId"),
            Id=json_data.get("Id"),
            NetworkName=json_data.get("NetworkName"),
            PeerId=json_data.get("PeerId"),
            ProjectId=json_data.get("ProjectId"),
            ProviderName=json_data.get("ProviderName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RouteTableCidrBlock=json_data.get("RouteTableCidrBlock"),
            Status=json_data.get("Status"),
            StatusName=json_data.get("StatusName"),
            VnetName=json_data.get("VnetName"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


