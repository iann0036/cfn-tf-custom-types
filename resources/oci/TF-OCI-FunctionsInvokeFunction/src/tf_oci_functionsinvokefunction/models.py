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
    Base64EncodeContent: Optional[bool]
    Content: Optional[str]
    FnIntent: Optional[str]
    FnInvokeType: Optional[str]
    FunctionId: Optional[str]
    Id: Optional[str]
    InputBodySourcePath: Optional[str]
    InvokeEndpoint: Optional[str]
    InvokeFunctionBody: Optional[str]
    InvokeFunctionBodyBase64Encoded: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Base64EncodeContent=json_data.get("Base64EncodeContent"),
            Content=json_data.get("Content"),
            FnIntent=json_data.get("FnIntent"),
            FnInvokeType=json_data.get("FnInvokeType"),
            FunctionId=json_data.get("FunctionId"),
            Id=json_data.get("Id"),
            InputBodySourcePath=json_data.get("InputBodySourcePath"),
            InvokeEndpoint=json_data.get("InvokeEndpoint"),
            InvokeFunctionBody=json_data.get("InvokeFunctionBody"),
            InvokeFunctionBodyBase64Encoded=json_data.get("InvokeFunctionBodyBase64Encoded"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


