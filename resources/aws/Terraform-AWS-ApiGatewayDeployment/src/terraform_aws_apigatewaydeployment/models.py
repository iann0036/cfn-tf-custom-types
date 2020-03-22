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
    CreatedDate: Optional[str]
    Description: Optional[str]
    ExecutionArn: Optional[str]
    Id: Optional[str]
    InvokeUrl: Optional[str]
    RestApiId: Optional[str]
    StageDescription: Optional[str]
    StageName: Optional[str]
    Variables: Optional[Sequence["_Variables"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            ExecutionArn=json_data.get("ExecutionArn"),
            Id=json_data.get("Id"),
            InvokeUrl=json_data.get("InvokeUrl"),
            RestApiId=json_data.get("RestApiId"),
            StageDescription=json_data.get("StageDescription"),
            StageName=json_data.get("StageName"),
            Variables=json_data.get("Variables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Variables:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Variables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Variables"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Variables = Variables


