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
    CreatedAt: Optional[str]
    Description: Optional[str]
    ExternalRegionId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    RegionId: Optional[str]
    UpdatedAt: Optional[str]
    ImageMapping: Optional[Sequence["_ImageMappingDefinition"]]

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
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            RegionId=json_data.get("RegionId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            ImageMapping=deserialize_list(json_data.get("ImageMapping"), ImageMappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ImageMappingDefinition(BaseModel):
    CloudConfig: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    Name: Optional[str]
    Constraints: Optional[Sequence["_ConstraintsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudConfig=json_data.get("CloudConfig"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            Name=json_data.get("Name"),
            Constraints=deserialize_list(json_data.get("Constraints"), ConstraintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageMappingDefinition = ImageMappingDefinition


@dataclass
class ConstraintsDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition = ConstraintsDefinition


