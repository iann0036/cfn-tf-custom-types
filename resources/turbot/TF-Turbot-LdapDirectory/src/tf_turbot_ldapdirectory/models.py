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
    Base: Optional[str]
    ConnectivityTestFilter: Optional[str]
    Description: Optional[str]
    DisabledGroupFilter: Optional[str]
    DisabledUserFilter: Optional[str]
    DistinguishedName: Optional[str]
    GroupMemberOfAttribute: Optional[str]
    GroupMembershipAttribute: Optional[str]
    GroupObjectFilter: Optional[str]
    GroupProfileIdTemplate: Optional[str]
    GroupSearchFilter: Optional[str]
    GroupSyncFilter: Optional[str]
    Id: Optional[str]
    Parent: Optional[str]
    ParentAkas: Optional[Sequence[str]]
    Password: Optional[str]
    ProfileIdTemplate: Optional[str]
    RejectUnauthorized: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Title: Optional[str]
    TlsEnabled: Optional[bool]
    TlsServerCertificate: Optional[str]
    Url: Optional[str]
    UserCanonicalNameAttribute: Optional[str]
    UserDisplayNameAttribute: Optional[str]
    UserEmailAttribute: Optional[str]
    UserFamilyNameAttribute: Optional[str]
    UserGivenNameAttribute: Optional[str]
    UserMatchFilter: Optional[str]
    UserObjectFilter: Optional[str]
    UserSearchAttributes: Optional[Sequence[str]]
    UserSearchFilter: Optional[str]

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
            Base=json_data.get("Base"),
            ConnectivityTestFilter=json_data.get("ConnectivityTestFilter"),
            Description=json_data.get("Description"),
            DisabledGroupFilter=json_data.get("DisabledGroupFilter"),
            DisabledUserFilter=json_data.get("DisabledUserFilter"),
            DistinguishedName=json_data.get("DistinguishedName"),
            GroupMemberOfAttribute=json_data.get("GroupMemberOfAttribute"),
            GroupMembershipAttribute=json_data.get("GroupMembershipAttribute"),
            GroupObjectFilter=json_data.get("GroupObjectFilter"),
            GroupProfileIdTemplate=json_data.get("GroupProfileIdTemplate"),
            GroupSearchFilter=json_data.get("GroupSearchFilter"),
            GroupSyncFilter=json_data.get("GroupSyncFilter"),
            Id=json_data.get("Id"),
            Parent=json_data.get("Parent"),
            ParentAkas=json_data.get("ParentAkas"),
            Password=json_data.get("Password"),
            ProfileIdTemplate=json_data.get("ProfileIdTemplate"),
            RejectUnauthorized=json_data.get("RejectUnauthorized"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Title=json_data.get("Title"),
            TlsEnabled=json_data.get("TlsEnabled"),
            TlsServerCertificate=json_data.get("TlsServerCertificate"),
            Url=json_data.get("Url"),
            UserCanonicalNameAttribute=json_data.get("UserCanonicalNameAttribute"),
            UserDisplayNameAttribute=json_data.get("UserDisplayNameAttribute"),
            UserEmailAttribute=json_data.get("UserEmailAttribute"),
            UserFamilyNameAttribute=json_data.get("UserFamilyNameAttribute"),
            UserGivenNameAttribute=json_data.get("UserGivenNameAttribute"),
            UserMatchFilter=json_data.get("UserMatchFilter"),
            UserObjectFilter=json_data.get("UserObjectFilter"),
            UserSearchAttributes=json_data.get("UserSearchAttributes"),
            UserSearchFilter=json_data.get("UserSearchFilter"),
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


