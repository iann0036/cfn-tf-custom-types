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
    Arn: Optional[str]
    DeliveryS3Bucket: Optional[str]
    DeliveryS3KeyPrefix: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    TemplateBody: Optional[str]
    TemplateS3Uri: Optional[str]
    InputParameter: Optional[Sequence["_InputParameterDefinition"]]

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
            Arn=json_data.get("Arn"),
            DeliveryS3Bucket=json_data.get("DeliveryS3Bucket"),
            DeliveryS3KeyPrefix=json_data.get("DeliveryS3KeyPrefix"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateS3Uri=json_data.get("TemplateS3Uri"),
            InputParameter=deserialize_list(json_data.get("InputParameter"), InputParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InputParameterDefinition(BaseModel):
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputParameterDefinition = InputParameterDefinition


