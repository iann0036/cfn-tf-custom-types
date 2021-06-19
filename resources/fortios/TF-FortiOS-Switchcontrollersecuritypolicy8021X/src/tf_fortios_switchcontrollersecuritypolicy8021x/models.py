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
    AuthFailVlan: Optional[str]
    AuthFailVlanId: Optional[str]
    AuthFailVlanid: Optional[float]
    AuthserverTimeoutPeriod: Optional[float]
    AuthserverTimeoutVlan: Optional[str]
    AuthserverTimeoutVlanid: Optional[str]
    DynamicSortSubtable: Optional[str]
    EapAutoUntaggedVlans: Optional[str]
    EapPassthru: Optional[str]
    FramevidApply: Optional[str]
    GuestAuthDelay: Optional[float]
    GuestVlan: Optional[str]
    GuestVlanId: Optional[str]
    GuestVlanid: Optional[float]
    Id: Optional[str]
    MacAuthBypass: Optional[str]
    Name: Optional[str]
    OpenAuth: Optional[str]
    PolicyType: Optional[str]
    RadiusTimeoutOverwrite: Optional[str]
    SecurityMode: Optional[str]
    Vdomparam: Optional[str]
    UserGroup: Optional[Sequence["_UserGroupDefinition"]]

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
            AuthFailVlan=json_data.get("AuthFailVlan"),
            AuthFailVlanId=json_data.get("AuthFailVlanId"),
            AuthFailVlanid=json_data.get("AuthFailVlanid"),
            AuthserverTimeoutPeriod=json_data.get("AuthserverTimeoutPeriod"),
            AuthserverTimeoutVlan=json_data.get("AuthserverTimeoutVlan"),
            AuthserverTimeoutVlanid=json_data.get("AuthserverTimeoutVlanid"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EapAutoUntaggedVlans=json_data.get("EapAutoUntaggedVlans"),
            EapPassthru=json_data.get("EapPassthru"),
            FramevidApply=json_data.get("FramevidApply"),
            GuestAuthDelay=json_data.get("GuestAuthDelay"),
            GuestVlan=json_data.get("GuestVlan"),
            GuestVlanId=json_data.get("GuestVlanId"),
            GuestVlanid=json_data.get("GuestVlanid"),
            Id=json_data.get("Id"),
            MacAuthBypass=json_data.get("MacAuthBypass"),
            Name=json_data.get("Name"),
            OpenAuth=json_data.get("OpenAuth"),
            PolicyType=json_data.get("PolicyType"),
            RadiusTimeoutOverwrite=json_data.get("RadiusTimeoutOverwrite"),
            SecurityMode=json_data.get("SecurityMode"),
            Vdomparam=json_data.get("Vdomparam"),
            UserGroup=deserialize_list(json_data.get("UserGroup"), UserGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserGroupDefinition = UserGroupDefinition


