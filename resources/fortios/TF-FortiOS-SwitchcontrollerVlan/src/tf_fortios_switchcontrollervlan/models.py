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
    Auth: Optional[str]
    Color: Optional[float]
    Comments: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PortalMessageOverrideGroup: Optional[str]
    RadiusServer: Optional[str]
    Security: Optional[str]
    Usergroup: Optional[str]
    Vdom: Optional[str]
    Vdomparam: Optional[str]
    Vlanid: Optional[float]
    PortalMessageOverrides: Optional[Sequence["_PortalMessageOverridesDefinition"]]
    SelectedUsergroups: Optional[Sequence["_SelectedUsergroupsDefinition"]]

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
            Auth=json_data.get("Auth"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PortalMessageOverrideGroup=json_data.get("PortalMessageOverrideGroup"),
            RadiusServer=json_data.get("RadiusServer"),
            Security=json_data.get("Security"),
            Usergroup=json_data.get("Usergroup"),
            Vdom=json_data.get("Vdom"),
            Vdomparam=json_data.get("Vdomparam"),
            Vlanid=json_data.get("Vlanid"),
            PortalMessageOverrides=deserialize_list(json_data.get("PortalMessageOverrides"), PortalMessageOverridesDefinition),
            SelectedUsergroups=deserialize_list(json_data.get("SelectedUsergroups"), SelectedUsergroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortalMessageOverridesDefinition(BaseModel):
    AuthDisclaimerPage: Optional[str]
    AuthLoginFailedPage: Optional[str]
    AuthLoginPage: Optional[str]
    AuthRejectPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortalMessageOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortalMessageOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthDisclaimerPage=json_data.get("AuthDisclaimerPage"),
            AuthLoginFailedPage=json_data.get("AuthLoginFailedPage"),
            AuthLoginPage=json_data.get("AuthLoginPage"),
            AuthRejectPage=json_data.get("AuthRejectPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortalMessageOverridesDefinition = PortalMessageOverridesDefinition


@dataclass
class SelectedUsergroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectedUsergroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectedUsergroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectedUsergroupsDefinition = SelectedUsergroupsDefinition


