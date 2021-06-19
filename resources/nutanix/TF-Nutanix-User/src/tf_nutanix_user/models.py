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
    AccessControlPolicyReferenceList: Optional[Sequence["_AccessControlPolicyReferenceListDefinition"]]
    ApiVersion: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    ProjectReferenceList: Optional[Sequence["_ProjectReferenceListDefinition"]]
    State: Optional[str]
    UserType: Optional[str]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    DirectoryServiceUser: Optional[Sequence["_DirectoryServiceUserDefinition"]]
    IdentityProviderUser: Optional[Sequence["_IdentityProviderUserDefinition"]]

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
            AccessControlPolicyReferenceList=deserialize_list(json_data.get("AccessControlPolicyReferenceList"), AccessControlPolicyReferenceListDefinition),
            ApiVersion=json_data.get("ApiVersion"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            ProjectReferenceList=deserialize_list(json_data.get("ProjectReferenceList"), ProjectReferenceListDefinition),
            State=json_data.get("State"),
            UserType=json_data.get("UserType"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            DirectoryServiceUser=deserialize_list(json_data.get("DirectoryServiceUser"), DirectoryServiceUserDefinition),
            IdentityProviderUser=deserialize_list(json_data.get("IdentityProviderUser"), IdentityProviderUserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessControlPolicyReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlPolicyReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlPolicyReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlPolicyReferenceListDefinition = AccessControlPolicyReferenceListDefinition


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
class ProjectReferenceListDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceListDefinition = ProjectReferenceListDefinition


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
class DirectoryServiceUserDefinition(BaseModel):
    UserPrincipalName: Optional[str]
    DirectoryServiceReference: Optional[Sequence["_DirectoryServiceReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DirectoryServiceUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectoryServiceUserDefinition"]:
        if not json_data:
            return None
        return cls(
            UserPrincipalName=json_data.get("UserPrincipalName"),
            DirectoryServiceReference=deserialize_list(json_data.get("DirectoryServiceReference"), DirectoryServiceReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectoryServiceUserDefinition = DirectoryServiceUserDefinition


@dataclass
class DirectoryServiceReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DirectoryServiceReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectoryServiceReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectoryServiceReferenceDefinition = DirectoryServiceReferenceDefinition


@dataclass
class IdentityProviderUserDefinition(BaseModel):
    Username: Optional[str]
    IdentityProviderReference: Optional[Sequence["_IdentityProviderReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityProviderUserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityProviderUserDefinition"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            IdentityProviderReference=deserialize_list(json_data.get("IdentityProviderReference"), IdentityProviderReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityProviderUserDefinition = IdentityProviderUserDefinition


@dataclass
class IdentityProviderReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityProviderReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityProviderReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityProviderReferenceDefinition = IdentityProviderReferenceDefinition


