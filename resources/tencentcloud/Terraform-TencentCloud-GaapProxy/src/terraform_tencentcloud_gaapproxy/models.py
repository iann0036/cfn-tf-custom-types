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
    AccessRegion: Optional[str]
    Bandwidth: Optional[float]
    Concurrent: Optional[float]
    CreateTime: Optional[str]
    Domain: Optional[str]
    Enable: Optional[bool]
    ForwardIp: Optional[str]
    Id: Optional[str]
    Ip: Optional[str]
    Name: Optional[str]
    ProjectId: Optional[float]
    RealserverRegion: Optional[str]
    Scalable: Optional[bool]
    Status: Optional[str]
    SupportProtocols: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessRegion=json_data.get("AccessRegion"),
            Bandwidth=json_data.get("Bandwidth"),
            Concurrent=json_data.get("Concurrent"),
            CreateTime=json_data.get("CreateTime"),
            Domain=json_data.get("Domain"),
            Enable=json_data.get("Enable"),
            ForwardIp=json_data.get("ForwardIp"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            RealserverRegion=json_data.get("RealserverRegion"),
            Scalable=json_data.get("Scalable"),
            Status=json_data.get("Status"),
            SupportProtocols=json_data.get("SupportProtocols"),
            Tags=json_data.get("Tags"),
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


