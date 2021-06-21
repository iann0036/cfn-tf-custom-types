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
    Distribution: Optional[str]
    Id: Optional[str]
    ImageId: Optional[float]
    MinDiskSize: Optional[float]
    Name: Optional[str]
    Public: Optional[bool]
    Regions: Optional[Sequence[str]]
    SizeGigabytes: Optional[float]
    Slug: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    Url: Optional[str]

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
            Distribution=json_data.get("Distribution"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            MinDiskSize=json_data.get("MinDiskSize"),
            Name=json_data.get("Name"),
            Public=json_data.get("Public"),
            Regions=json_data.get("Regions"),
            SizeGigabytes=json_data.get("SizeGigabytes"),
            Slug=json_data.get("Slug"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

