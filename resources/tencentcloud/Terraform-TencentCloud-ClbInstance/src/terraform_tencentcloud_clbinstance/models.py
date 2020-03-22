# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    ClbName: Optional[str]
    ClbVips: Optional[Sequence[str]]
    Id: Optional[str]
    NetworkType: Optional[str]
    ProjectId: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetRegionInfoRegion: Optional[str]
    TargetRegionInfoVpcId: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClbName=json_data.get("ClbName"),
            ClbVips=json_data.get("ClbVips"),
            Id=json_data.get("Id"),
            NetworkType=json_data.get("NetworkType"),
            ProjectId=json_data.get("ProjectId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            TargetRegionInfoRegion=json_data.get("TargetRegionInfoRegion"),
            TargetRegionInfoVpcId=json_data.get("TargetRegionInfoVpcId"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


