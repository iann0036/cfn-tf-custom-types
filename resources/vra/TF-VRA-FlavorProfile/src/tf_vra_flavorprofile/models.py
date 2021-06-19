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
    CloudAccountId: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    ExternalRegionId: Optional[str]
    Id: Optional[str]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    RegionId: Optional[str]
    UpdatedAt: Optional[str]
    FlavorMapping: Optional[Sequence["_FlavorMappingDefinition"]]

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
            CloudAccountId=json_data.get("CloudAccountId"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            Id=json_data.get("Id"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            RegionId=json_data.get("RegionId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            FlavorMapping=deserialize_list(json_data.get("FlavorMapping"), FlavorMappingDefinition),
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
class FlavorMappingDefinition(BaseModel):
    CpuCount: Optional[float]
    InstanceType: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FlavorMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlavorMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuCount=json_data.get("CpuCount"),
            InstanceType=json_data.get("InstanceType"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlavorMappingDefinition = FlavorMappingDefinition


