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
    AllowGroupSyncing: Optional[bool]
    AllowIdpInitiatedSso: Optional[bool]
    Certificate: Optional[str]
    Description: Optional[str]
    DirectoryType: Optional[str]
    EntryPoint: Optional[str]
    GroupFilter: Optional[str]
    GroupIdTemplate: Optional[str]
    Id: Optional[str]
    Issuer: Optional[str]
    NameIdFormat: Optional[str]
    Parent: Optional[str]
    ParentAkas: Optional[Sequence[str]]
    PoolId: Optional[str]
    ProfileGroupsAttribute: Optional[str]
    ProfileIdTemplate: Optional[str]
    SignRequests: Optional[str]
    SignatureAlgorithm: Optional[str]
    SignaturePrivateKey: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Title: Optional[str]

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
            AllowGroupSyncing=json_data.get("AllowGroupSyncing"),
            AllowIdpInitiatedSso=json_data.get("AllowIdpInitiatedSso"),
            Certificate=json_data.get("Certificate"),
            Description=json_data.get("Description"),
            DirectoryType=json_data.get("DirectoryType"),
            EntryPoint=json_data.get("EntryPoint"),
            GroupFilter=json_data.get("GroupFilter"),
            GroupIdTemplate=json_data.get("GroupIdTemplate"),
            Id=json_data.get("Id"),
            Issuer=json_data.get("Issuer"),
            NameIdFormat=json_data.get("NameIdFormat"),
            Parent=json_data.get("Parent"),
            ParentAkas=json_data.get("ParentAkas"),
            PoolId=json_data.get("PoolId"),
            ProfileGroupsAttribute=json_data.get("ProfileGroupsAttribute"),
            ProfileIdTemplate=json_data.get("ProfileIdTemplate"),
            SignRequests=json_data.get("SignRequests"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
            SignaturePrivateKey=json_data.get("SignaturePrivateKey"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


