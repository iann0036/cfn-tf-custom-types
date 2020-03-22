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
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


