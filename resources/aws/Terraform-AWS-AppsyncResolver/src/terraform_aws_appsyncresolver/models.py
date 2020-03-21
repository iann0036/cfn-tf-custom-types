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
    ApiId: Optional[str]
    Arn: Optional[str]
    DataSource: Optional[str]
    Field: Optional[str]
    Kind: Optional[str]
    RequestTemplate: Optional[str]
    ResponseTemplate: Optional[str]
    Type: Optional[str]
    PipelineConfig: Optional[Sequence["_PipelineConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiId=json_data.get("ApiId"),
            Arn=json_data.get("Arn"),
            DataSource=json_data.get("DataSource"),
            Field=json_data.get("Field"),
            Kind=json_data.get("Kind"),
            RequestTemplate=json_data.get("RequestTemplate"),
            ResponseTemplate=json_data.get("ResponseTemplate"),
            Type=json_data.get("Type"),
            PipelineConfig=json_data.get("PipelineConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PipelineConfig:
    Functions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineConfig"]:
        if not json_data:
            return None
        return cls(
            Functions=json_data.get("Functions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineConfig = PipelineConfig


