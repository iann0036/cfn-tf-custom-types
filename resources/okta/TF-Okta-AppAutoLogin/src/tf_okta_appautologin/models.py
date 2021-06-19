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
    AccessibilityErrorRedirectUrl: Optional[str]
    AccessibilitySelfService: Optional[bool]
    AutoSubmitToolbar: Optional[bool]
    CredentialsScheme: Optional[str]
    Groups: Optional[Sequence[str]]
    HideIos: Optional[bool]
    HideWeb: Optional[bool]
    Id: Optional[str]
    Label: Optional[str]
    Name: Optional[str]
    PreconfiguredApp: Optional[str]
    RevealPassword: Optional[bool]
    SharedPassword: Optional[str]
    SharedUsername: Optional[str]
    SignOnMode: Optional[str]
    SignOnRedirectUrl: Optional[str]
    SignOnUrl: Optional[str]
    Status: Optional[str]
    UserNameTemplate: Optional[str]
    UserNameTemplateSuffix: Optional[str]
    UserNameTemplateType: Optional[str]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            AccessibilityErrorRedirectUrl=json_data.get("AccessibilityErrorRedirectUrl"),
            AccessibilitySelfService=json_data.get("AccessibilitySelfService"),
            AutoSubmitToolbar=json_data.get("AutoSubmitToolbar"),
            CredentialsScheme=json_data.get("CredentialsScheme"),
            Groups=json_data.get("Groups"),
            HideIos=json_data.get("HideIos"),
            HideWeb=json_data.get("HideWeb"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Name=json_data.get("Name"),
            PreconfiguredApp=json_data.get("PreconfiguredApp"),
            RevealPassword=json_data.get("RevealPassword"),
            SharedPassword=json_data.get("SharedPassword"),
            SharedUsername=json_data.get("SharedUsername"),
            SignOnMode=json_data.get("SignOnMode"),
            SignOnRedirectUrl=json_data.get("SignOnRedirectUrl"),
            SignOnUrl=json_data.get("SignOnUrl"),
            Status=json_data.get("Status"),
            UserNameTemplate=json_data.get("UserNameTemplate"),
            UserNameTemplateSuffix=json_data.get("UserNameTemplateSuffix"),
            UserNameTemplateType=json_data.get("UserNameTemplateType"),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UsersDefinition(BaseModel):
    Id: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


