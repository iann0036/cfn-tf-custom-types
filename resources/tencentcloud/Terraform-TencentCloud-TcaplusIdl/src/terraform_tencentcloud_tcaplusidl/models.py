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
    AppId: Optional[str]
    FileContent: Optional[str]
    FileExtType: Optional[str]
    FileName: Optional[str]
    FileType: Optional[str]
    TableInfos: Optional[Sequence["_TableInfos"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppId=json_data.get("AppId"),
            FileContent=json_data.get("FileContent"),
            FileExtType=json_data.get("FileExtType"),
            FileName=json_data.get("FileName"),
            FileType=json_data.get("FileType"),
            TableInfos=json_data.get("TableInfos"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TableInfos:
    Error: Optional[str]
    IndexKeySet: Optional[str]
    KeyFields: Optional[str]
    SumKeyFieldSize: Optional[float]
    SumValueFieldSize: Optional[float]
    TableName: Optional[str]
    ValueFields: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableInfos"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableInfos"]:
        if not json_data:
            return None
        return cls(
            Error=json_data.get("Error"),
            IndexKeySet=json_data.get("IndexKeySet"),
            KeyFields=json_data.get("KeyFields"),
            SumKeyFieldSize=json_data.get("SumKeyFieldSize"),
            SumValueFieldSize=json_data.get("SumValueFieldSize"),
            TableName=json_data.get("TableName"),
            ValueFields=json_data.get("ValueFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableInfos = TableInfos


