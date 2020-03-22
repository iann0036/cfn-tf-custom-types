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
    Body: Optional[str]
    ClearHeaders: Optional[Sequence[str]]
    Domain: Optional[str]
    ErrorCodes: Optional[Sequence[float]]
    Id: Optional[str]
    ListenerId: Optional[str]
    NewErrorCode: Optional[float]
    SetHeaders: Optional[Sequence["_SetHeaders"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Body=json_data.get("Body"),
            ClearHeaders=json_data.get("ClearHeaders"),
            Domain=json_data.get("Domain"),
            ErrorCodes=json_data.get("ErrorCodes"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            NewErrorCode=json_data.get("NewErrorCode"),
            SetHeaders=json_data.get("SetHeaders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SetHeaders:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetHeaders"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetHeaders = SetHeaders


