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
    AccessMode: Optional[str]
    AllowedPrincipalIds: Optional[Sequence[str]]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Certificate: Optional[str]
    ConnectionTimeout: Optional[float]
    DefaultLoginDomain: Optional[str]
    Enabled: Optional[bool]
    GroupDnAttribute: Optional[str]
    GroupMemberMappingAttribute: Optional[str]
    GroupMemberUserAttribute: Optional[str]
    GroupNameAttribute: Optional[str]
    GroupObjectClass: Optional[str]
    GroupSearchAttribute: Optional[str]
    GroupSearchBase: Optional[str]
    GroupSearchFilter: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    NestedGroupMembershipEnabled: Optional[bool]
    Port: Optional[float]
    Servers: Optional[Sequence[str]]
    ServiceAccountPassword: Optional[str]
    ServiceAccountUsername: Optional[str]
    TestPassword: Optional[str]
    TestUsername: Optional[str]
    Tls: Optional[bool]
    Type: Optional[str]
    UserDisabledBitMask: Optional[float]
    UserEnabledAttribute: Optional[str]
    UserLoginAttribute: Optional[str]
    UserNameAttribute: Optional[str]
    UserObjectClass: Optional[str]
    UserSearchAttribute: Optional[str]
    UserSearchBase: Optional[str]
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
            AccessMode=json_data.get("AccessMode"),
            AllowedPrincipalIds=json_data.get("AllowedPrincipalIds"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Certificate=json_data.get("Certificate"),
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            DefaultLoginDomain=json_data.get("DefaultLoginDomain"),
            Enabled=json_data.get("Enabled"),
            GroupDnAttribute=json_data.get("GroupDnAttribute"),
            GroupMemberMappingAttribute=json_data.get("GroupMemberMappingAttribute"),
            GroupMemberUserAttribute=json_data.get("GroupMemberUserAttribute"),
            GroupNameAttribute=json_data.get("GroupNameAttribute"),
            GroupObjectClass=json_data.get("GroupObjectClass"),
            GroupSearchAttribute=json_data.get("GroupSearchAttribute"),
            GroupSearchBase=json_data.get("GroupSearchBase"),
            GroupSearchFilter=json_data.get("GroupSearchFilter"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            NestedGroupMembershipEnabled=json_data.get("NestedGroupMembershipEnabled"),
            Port=json_data.get("Port"),
            Servers=json_data.get("Servers"),
            ServiceAccountPassword=json_data.get("ServiceAccountPassword"),
            ServiceAccountUsername=json_data.get("ServiceAccountUsername"),
            TestPassword=json_data.get("TestPassword"),
            TestUsername=json_data.get("TestUsername"),
            Tls=json_data.get("Tls"),
            Type=json_data.get("Type"),
            UserDisabledBitMask=json_data.get("UserDisabledBitMask"),
            UserEnabledAttribute=json_data.get("UserEnabledAttribute"),
            UserLoginAttribute=json_data.get("UserLoginAttribute"),
            UserNameAttribute=json_data.get("UserNameAttribute"),
            UserObjectClass=json_data.get("UserObjectClass"),
            UserSearchAttribute=json_data.get("UserSearchAttribute"),
            UserSearchBase=json_data.get("UserSearchBase"),
            UserSearchFilter=json_data.get("UserSearchFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


