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
    ApiVersion: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsDefault: Optional[bool]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    State: Optional[str]
    AccountReferenceList: Optional[Sequence["_AccountReferenceListDefinition"]]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    DefaultSubnetReference: Optional[Sequence["_DefaultSubnetReferenceDefinition"]]
    EnvironmentReferenceList: Optional[Sequence["_EnvironmentReferenceListDefinition"]]
    ExternalNetworkList: Optional[Sequence["_ExternalNetworkListDefinition"]]
    ExternalUserGroupReferenceList: Optional[Sequence["_ExternalUserGroupReferenceListDefinition"]]
    ResourceDomain: Optional[Sequence["_ResourceDomainDefinition"]]
    SubnetReferenceList: Optional[Sequence["_SubnetReferenceListDefinition"]]
    UserReferenceList: Optional[Sequence["_UserReferenceListDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsDefault=json_data.get("IsDefault"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            State=json_data.get("State"),
            AccountReferenceList=deserialize_list(json_data.get("AccountReferenceList"), AccountReferenceListDefinition),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            DefaultSubnetReference=deserialize_list(json_data.get("DefaultSubnetReference"), DefaultSubnetReferenceDefinition),
            EnvironmentReferenceList=deserialize_list(json_data.get("EnvironmentReferenceList"), EnvironmentReferenceListDefinition),
            ExternalNetworkList=deserialize_list(json_data.get("ExternalNetworkList"), ExternalNetworkListDefinition),
            ExternalUserGroupReferenceList=deserialize_list(json_data.get("ExternalUserGroupReferenceList"), ExternalUserGroupReferenceListDefinition),
            ResourceDomain=deserialize_list(json_data.get("ResourceDomain"), ResourceDomainDefinition),
            SubnetReferenceList=deserialize_list(json_data.get("SubnetReferenceList"), SubnetReferenceListDefinition),
            UserReferenceList=deserialize_list(json_data.get("UserReferenceList"), UserReferenceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class OwnerReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class ProjectReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceDefinition = ProjectReferenceDefinition


@dataclass
class AccountReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountReferenceListDefinition = AccountReferenceListDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


@dataclass
class DefaultSubnetReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSubnetReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSubnetReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSubnetReferenceDefinition = DefaultSubnetReferenceDefinition


@dataclass
class EnvironmentReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentReferenceListDefinition = EnvironmentReferenceListDefinition


@dataclass
class ExternalNetworkListDefinition(BaseModel):
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalNetworkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalNetworkListDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalNetworkListDefinition = ExternalNetworkListDefinition


@dataclass
class ExternalUserGroupReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalUserGroupReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalUserGroupReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalUserGroupReferenceListDefinition = ExternalUserGroupReferenceListDefinition


@dataclass
class ResourceDomainDefinition(BaseModel):
    Resources: Optional[Sequence["_ResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceDomainDefinition = ResourceDomainDefinition


@dataclass
class ResourcesDefinition(BaseModel):
    Limit: Optional[float]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Limit=json_data.get("Limit"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


@dataclass
class SubnetReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetReferenceListDefinition = SubnetReferenceListDefinition


@dataclass
class UserReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserReferenceListDefinition = UserReferenceListDefinition


