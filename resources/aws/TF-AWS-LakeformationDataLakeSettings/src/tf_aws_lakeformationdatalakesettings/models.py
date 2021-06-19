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
    Admins: Optional[Sequence[str]]
    CatalogId: Optional[str]
    Id: Optional[str]
    TrustedResourceOwners: Optional[Sequence[str]]
    CreateDatabaseDefaultPermissions: Optional[Sequence["_CreateDatabaseDefaultPermissionsDefinition"]]
    CreateTableDefaultPermissions: Optional[Sequence["_CreateTableDefaultPermissionsDefinition"]]

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
            Admins=json_data.get("Admins"),
            CatalogId=json_data.get("CatalogId"),
            Id=json_data.get("Id"),
            TrustedResourceOwners=json_data.get("TrustedResourceOwners"),
            CreateDatabaseDefaultPermissions=deserialize_list(json_data.get("CreateDatabaseDefaultPermissions"), CreateDatabaseDefaultPermissionsDefinition),
            CreateTableDefaultPermissions=deserialize_list(json_data.get("CreateTableDefaultPermissions"), CreateTableDefaultPermissionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CreateDatabaseDefaultPermissionsDefinition(BaseModel):
    Permissions: Optional[Sequence[str]]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreateDatabaseDefaultPermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateDatabaseDefaultPermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Permissions=json_data.get("Permissions"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateDatabaseDefaultPermissionsDefinition = CreateDatabaseDefaultPermissionsDefinition


@dataclass
class CreateTableDefaultPermissionsDefinition(BaseModel):
    Permissions: Optional[Sequence[str]]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreateTableDefaultPermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateTableDefaultPermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Permissions=json_data.get("Permissions"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateTableDefaultPermissionsDefinition = CreateTableDefaultPermissionsDefinition


