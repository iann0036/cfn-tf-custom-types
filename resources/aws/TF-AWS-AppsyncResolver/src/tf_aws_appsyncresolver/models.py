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
    ApiId: Optional[str]
    Arn: Optional[str]
    DataSource: Optional[str]
    Field: Optional[str]
    Id: Optional[str]
    Kind: Optional[str]
    RequestTemplate: Optional[str]
    ResponseTemplate: Optional[str]
    Type: Optional[str]
    CachingConfig: Optional[Sequence["_CachingConfigDefinition"]]
    PipelineConfig: Optional[Sequence["_PipelineConfigDefinition"]]

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
            ApiId=json_data.get("ApiId"),
            Arn=json_data.get("Arn"),
            DataSource=json_data.get("DataSource"),
            Field=json_data.get("Field"),
            Id=json_data.get("Id"),
            Kind=json_data.get("Kind"),
            RequestTemplate=json_data.get("RequestTemplate"),
            ResponseTemplate=json_data.get("ResponseTemplate"),
            Type=json_data.get("Type"),
            CachingConfig=deserialize_list(json_data.get("CachingConfig"), CachingConfigDefinition),
            PipelineConfig=deserialize_list(json_data.get("PipelineConfig"), PipelineConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CachingConfigDefinition(BaseModel):
    CachingKeys: Optional[Sequence[str]]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CachingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CachingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CachingKeys=json_data.get("CachingKeys"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CachingConfigDefinition = CachingConfigDefinition


@dataclass
class PipelineConfigDefinition(BaseModel):
    Functions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Functions=json_data.get("Functions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineConfigDefinition = PipelineConfigDefinition


