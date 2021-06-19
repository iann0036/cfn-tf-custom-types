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
    CookieName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    GeoLocationMatch: Optional[Sequence["_GeoLocationMatchDefinition"]]
    HttpPolicyMatch: Optional[Sequence["_HttpPolicyMatchDefinition"]]

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
            CookieName=json_data.get("CookieName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            GeoLocationMatch=deserialize_list(json_data.get("GeoLocationMatch"), GeoLocationMatchDefinition),
            HttpPolicyMatch=deserialize_list(json_data.get("HttpPolicyMatch"), HttpPolicyMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GeoLocationMatchDefinition(BaseModel):
    GeoLocation: Optional[str]
    GeoLocationServiceGroup: Optional[str]
    GeoLocationTemplate: Optional[str]
    GeoLocationTemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoLocationMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoLocationMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            GeoLocation=json_data.get("GeoLocation"),
            GeoLocationServiceGroup=json_data.get("GeoLocationServiceGroup"),
            GeoLocationTemplate=json_data.get("GeoLocationTemplate"),
            GeoLocationTemplateName=json_data.get("GeoLocationTemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoLocationMatchDefinition = GeoLocationMatchDefinition


@dataclass
class HttpPolicyMatchDefinition(BaseModel):
    MatchString: Optional[str]
    MatchType: Optional[str]
    OtherMatchString: Optional[str]
    OtherMatchType: Optional[str]
    ServiceGroup: Optional[str]
    Template: Optional[str]
    TemplateName: Optional[str]
    Type: Optional[str]
    UrlUnderHost: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpPolicyMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpPolicyMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchString=json_data.get("MatchString"),
            MatchType=json_data.get("MatchType"),
            OtherMatchString=json_data.get("OtherMatchString"),
            OtherMatchType=json_data.get("OtherMatchType"),
            ServiceGroup=json_data.get("ServiceGroup"),
            Template=json_data.get("Template"),
            TemplateName=json_data.get("TemplateName"),
            Type=json_data.get("Type"),
            UrlUnderHost=json_data.get("UrlUnderHost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpPolicyMatchDefinition = HttpPolicyMatchDefinition


