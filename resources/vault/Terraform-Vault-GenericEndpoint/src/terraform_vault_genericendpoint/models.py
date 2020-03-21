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
    DataJson: Optional[str]
    DisableDelete: Optional[bool]
    DisableRead: Optional[bool]
    Id: Optional[str]
    IgnoreAbsentFields: Optional[bool]
    Path: Optional[str]
    WriteData: Optional[Sequence["_WriteData"]]
    WriteDataJson: Optional[str]
    WriteFields: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DataJson=json_data.get("DataJson"),
            DisableDelete=json_data.get("DisableDelete"),
            DisableRead=json_data.get("DisableRead"),
            Id=json_data.get("Id"),
            IgnoreAbsentFields=json_data.get("IgnoreAbsentFields"),
            Path=json_data.get("Path"),
            WriteData=json_data.get("WriteData"),
            WriteDataJson=json_data.get("WriteDataJson"),
            WriteFields=json_data.get("WriteFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class WriteData:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WriteData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WriteData"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WriteData = WriteData


