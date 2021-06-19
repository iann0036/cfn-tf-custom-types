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
    AzurePolicyId: Optional[float]
    Body: Optional[str]
    CloudProviderId: Optional[float]
    ComplianceCheckTypeId: Optional[float]
    CreatedAt: Optional[str]
    CreatedByUserId: Optional[float]
    CtManaged: Optional[bool]
    Description: Optional[str]
    FrequencyMinutes: Optional[float]
    FrequencyTypeId: Optional[float]
    Id: Optional[str]
    IsAllRegions: Optional[bool]
    IsAutoArchived: Optional[bool]
    LastScanId: Optional[float]
    LastUpdated: Optional[str]
    Name: Optional[str]
    Regions: Optional[Sequence[str]]
    SeverityTypeId: Optional[float]
    OwnerUserGroups: Optional[Sequence["_OwnerUserGroupsDefinition"]]
    OwnerUsers: Optional[Sequence["_OwnerUsersDefinition"]]

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
            AzurePolicyId=json_data.get("AzurePolicyId"),
            Body=json_data.get("Body"),
            CloudProviderId=json_data.get("CloudProviderId"),
            ComplianceCheckTypeId=json_data.get("ComplianceCheckTypeId"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedByUserId=json_data.get("CreatedByUserId"),
            CtManaged=json_data.get("CtManaged"),
            Description=json_data.get("Description"),
            FrequencyMinutes=json_data.get("FrequencyMinutes"),
            FrequencyTypeId=json_data.get("FrequencyTypeId"),
            Id=json_data.get("Id"),
            IsAllRegions=json_data.get("IsAllRegions"),
            IsAutoArchived=json_data.get("IsAutoArchived"),
            LastScanId=json_data.get("LastScanId"),
            LastUpdated=json_data.get("LastUpdated"),
            Name=json_data.get("Name"),
            Regions=json_data.get("Regions"),
            SeverityTypeId=json_data.get("SeverityTypeId"),
            OwnerUserGroups=deserialize_list(json_data.get("OwnerUserGroups"), OwnerUserGroupsDefinition),
            OwnerUsers=deserialize_list(json_data.get("OwnerUsers"), OwnerUsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OwnerUserGroupsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerUserGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerUserGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerUserGroupsDefinition = OwnerUserGroupsDefinition


@dataclass
class OwnerUsersDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerUsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerUsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerUsersDefinition = OwnerUsersDefinition


