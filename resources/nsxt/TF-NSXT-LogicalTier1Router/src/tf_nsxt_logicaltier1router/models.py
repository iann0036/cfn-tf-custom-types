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
    AdvertiseConfigRevision: Optional[float]
    AdvertiseConnectedRoutes: Optional[bool]
    AdvertiseLbSnatIpRoutes: Optional[bool]
    AdvertiseLbVipRoutes: Optional[bool]
    AdvertiseNatRoutes: Optional[bool]
    AdvertiseStaticRoutes: Optional[bool]
    Description: Optional[str]
    DisplayName: Optional[str]
    EdgeClusterId: Optional[str]
    EnableRouterAdvertisement: Optional[bool]
    FailoverMode: Optional[str]
    Id: Optional[str]
    Revision: Optional[float]
    FirewallSections: Optional[Sequence["_FirewallSectionsDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            AdvertiseConfigRevision=json_data.get("AdvertiseConfigRevision"),
            AdvertiseConnectedRoutes=json_data.get("AdvertiseConnectedRoutes"),
            AdvertiseLbSnatIpRoutes=json_data.get("AdvertiseLbSnatIpRoutes"),
            AdvertiseLbVipRoutes=json_data.get("AdvertiseLbVipRoutes"),
            AdvertiseNatRoutes=json_data.get("AdvertiseNatRoutes"),
            AdvertiseStaticRoutes=json_data.get("AdvertiseStaticRoutes"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EdgeClusterId=json_data.get("EdgeClusterId"),
            EnableRouterAdvertisement=json_data.get("EnableRouterAdvertisement"),
            FailoverMode=json_data.get("FailoverMode"),
            Id=json_data.get("Id"),
            Revision=json_data.get("Revision"),
            FirewallSections=deserialize_list(json_data.get("FirewallSections"), FirewallSectionsDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallSectionsDefinition(BaseModel):
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallSectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallSectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallSectionsDefinition = FirewallSectionsDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


