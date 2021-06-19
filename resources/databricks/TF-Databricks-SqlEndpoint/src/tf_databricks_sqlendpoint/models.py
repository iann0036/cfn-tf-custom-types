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
    AutoStopMins: Optional[float]
    ClusterSize: Optional[str]
    DataSourceId: Optional[str]
    EnablePhoton: Optional[bool]
    Id: Optional[str]
    InstanceProfileArn: Optional[str]
    JdbcUrl: Optional[str]
    MaxNumClusters: Optional[float]
    MinNumClusters: Optional[float]
    Name: Optional[str]
    NumClusters: Optional[float]
    SpotInstancePolicy: Optional[str]
    State: Optional[str]
    OdbcParams: Optional[Sequence["_OdbcParamsDefinition"]]
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
            AutoStopMins=json_data.get("AutoStopMins"),
            ClusterSize=json_data.get("ClusterSize"),
            DataSourceId=json_data.get("DataSourceId"),
            EnablePhoton=json_data.get("EnablePhoton"),
            Id=json_data.get("Id"),
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            JdbcUrl=json_data.get("JdbcUrl"),
            MaxNumClusters=json_data.get("MaxNumClusters"),
            MinNumClusters=json_data.get("MinNumClusters"),
            Name=json_data.get("Name"),
            NumClusters=json_data.get("NumClusters"),
            SpotInstancePolicy=json_data.get("SpotInstancePolicy"),
            State=json_data.get("State"),
            OdbcParams=deserialize_list(json_data.get("OdbcParams"), OdbcParamsDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OdbcParamsDefinition(BaseModel):
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OdbcParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OdbcParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OdbcParamsDefinition = OdbcParamsDefinition


@dataclass
class TagsDefinition(BaseModel):
    CustomTags: Optional[Sequence["_CustomTagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomTags=deserialize_list(json_data.get("CustomTags"), CustomTagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class CustomTagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTagsDefinition = CustomTagsDefinition


