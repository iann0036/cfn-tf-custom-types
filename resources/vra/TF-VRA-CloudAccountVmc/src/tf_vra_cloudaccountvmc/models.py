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
    AcceptSelfSignedCert: Optional[bool]
    ApiToken: Optional[str]
    CreatedAt: Optional[str]
    DcId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    NsxHostname: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    RegionIds: Optional[Sequence[str]]
    Regions: Optional[Sequence[str]]
    SddcName: Optional[str]
    UpdatedAt: Optional[str]
    VcenterHostname: Optional[str]
    VcenterPassword: Optional[str]
    VcenterUsername: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]

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
            AcceptSelfSignedCert=json_data.get("AcceptSelfSignedCert"),
            ApiToken=json_data.get("ApiToken"),
            CreatedAt=json_data.get("CreatedAt"),
            DcId=json_data.get("DcId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            NsxHostname=json_data.get("NsxHostname"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            RegionIds=json_data.get("RegionIds"),
            Regions=json_data.get("Regions"),
            SddcName=json_data.get("SddcName"),
            UpdatedAt=json_data.get("UpdatedAt"),
            VcenterHostname=json_data.get("VcenterHostname"),
            VcenterPassword=json_data.get("VcenterPassword"),
            VcenterUsername=json_data.get("VcenterUsername"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LinksDefinition(BaseModel):
    Href: Optional[str]
    Hrefs: Optional[Sequence[str]]
    Rel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinksDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Hrefs=json_data.get("Hrefs"),
            Rel=json_data.get("Rel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinksDefinition = LinksDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


