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
    CodeFilename: Optional[str]
    CodeType: Optional[str]
    CodeUrl: Optional[str]
    Description: Optional[str]
    FuncCode: Optional[str]
    Handler: Optional[str]
    Id: Optional[str]
    MemorySize: Optional[float]
    Name: Optional[str]
    Package: Optional[str]
    Runtime: Optional[str]
    Timeout: Optional[float]
    UserData: Optional[str]
    Xrole: Optional[str]
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
            CodeFilename=json_data.get("CodeFilename"),
            CodeType=json_data.get("CodeType"),
            CodeUrl=json_data.get("CodeUrl"),
            Description=json_data.get("Description"),
            FuncCode=json_data.get("FuncCode"),
            Handler=json_data.get("Handler"),
            Id=json_data.get("Id"),
            MemorySize=json_data.get("MemorySize"),
            Name=json_data.get("Name"),
            Package=json_data.get("Package"),
            Runtime=json_data.get("Runtime"),
            Timeout=json_data.get("Timeout"),
            UserData=json_data.get("UserData"),
            Xrole=json_data.get("Xrole"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


