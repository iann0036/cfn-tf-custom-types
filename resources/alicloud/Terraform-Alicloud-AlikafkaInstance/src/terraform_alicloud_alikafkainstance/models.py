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
    DeployType: Optional[float]
    DiskSize: Optional[float]
    DiskType: Optional[float]
    EipMax: Optional[float]
    Id: Optional[str]
    IoMax: Optional[float]
    Name: Optional[str]
    PaidType: Optional[str]
    SpecType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TopicQuota: Optional[float]
    VpcId: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeployType=json_data.get("DeployType"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            EipMax=json_data.get("EipMax"),
            Id=json_data.get("Id"),
            IoMax=json_data.get("IoMax"),
            Name=json_data.get("Name"),
            PaidType=json_data.get("PaidType"),
            SpecType=json_data.get("SpecType"),
            Tags=json_data.get("Tags"),
            TopicQuota=json_data.get("TopicQuota"),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
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


