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
    AdminConsentDescription: Optional[str]
    AdminConsentDisplayName: Optional[str]
    ApplicationObjectId: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    PermissionId: Optional[str]
    ScopeId: Optional[str]
    Type: Optional[str]
    UserConsentDescription: Optional[str]
    UserConsentDisplayName: Optional[str]
    Value: Optional[str]

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
            AdminConsentDescription=json_data.get("AdminConsentDescription"),
            AdminConsentDisplayName=json_data.get("AdminConsentDisplayName"),
            ApplicationObjectId=json_data.get("ApplicationObjectId"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            PermissionId=json_data.get("PermissionId"),
            ScopeId=json_data.get("ScopeId"),
            Type=json_data.get("Type"),
            UserConsentDescription=json_data.get("UserConsentDescription"),
            UserConsentDisplayName=json_data.get("UserConsentDisplayName"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


