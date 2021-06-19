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
    AccountId: Optional[str]
    AwsAggregateCloudAccountsCount: Optional[float]
    AwsCloudAccountsCount: Optional[float]
    AzureAggregateCloudAccountsCount: Optional[float]
    AzureCloudAccountsCount: Optional[float]
    Created: Optional[str]
    GoogleAggregateCloudAccountsCount: Optional[float]
    GoogleCloudAccountsCount: Optional[float]
    Id: Optional[str]
    IsParentRoot: Optional[bool]
    IsRoot: Optional[bool]
    Name: Optional[str]
    ParentId: Optional[str]
    Path: Optional[str]
    PathStr: Optional[str]
    SubOrganizationalUnitsCount: Optional[float]
    Updated: Optional[str]

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
            AccountId=json_data.get("AccountId"),
            AwsAggregateCloudAccountsCount=json_data.get("AwsAggregateCloudAccountsCount"),
            AwsCloudAccountsCount=json_data.get("AwsCloudAccountsCount"),
            AzureAggregateCloudAccountsCount=json_data.get("AzureAggregateCloudAccountsCount"),
            AzureCloudAccountsCount=json_data.get("AzureCloudAccountsCount"),
            Created=json_data.get("Created"),
            GoogleAggregateCloudAccountsCount=json_data.get("GoogleAggregateCloudAccountsCount"),
            GoogleCloudAccountsCount=json_data.get("GoogleCloudAccountsCount"),
            Id=json_data.get("Id"),
            IsParentRoot=json_data.get("IsParentRoot"),
            IsRoot=json_data.get("IsRoot"),
            Name=json_data.get("Name"),
            ParentId=json_data.get("ParentId"),
            Path=json_data.get("Path"),
            PathStr=json_data.get("PathStr"),
            SubOrganizationalUnitsCount=json_data.get("SubOrganizationalUnitsCount"),
            Updated=json_data.get("Updated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


