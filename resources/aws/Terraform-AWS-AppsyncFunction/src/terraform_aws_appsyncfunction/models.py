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
    Description: Optional[str]
    FunctionId: Optional[str]
    FunctionVersion: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RequestMappingTemplate: Optional[str]
    ResponseMappingTemplate: Optional[str]

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
            Description=json_data.get("Description"),
            FunctionId=json_data.get("FunctionId"),
            FunctionVersion=json_data.get("FunctionVersion"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RequestMappingTemplate=json_data.get("RequestMappingTemplate"),
            ResponseMappingTemplate=json_data.get("ResponseMappingTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


