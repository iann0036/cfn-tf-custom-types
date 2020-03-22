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
    Destination: Optional[str]
    Filter: Optional[str]
    Folder: Optional[str]
    Id: Optional[str]
    IncludeChildren: Optional[bool]
    Name: Optional[str]
    WriterIdentity: Optional[str]
    BigqueryOptions: Optional[Sequence["_BigqueryOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Destination=json_data.get("Destination"),
            Filter=json_data.get("Filter"),
            Folder=json_data.get("Folder"),
            Id=json_data.get("Id"),
            IncludeChildren=json_data.get("IncludeChildren"),
            Name=json_data.get("Name"),
            WriterIdentity=json_data.get("WriterIdentity"),
            BigqueryOptions=json_data.get("BigqueryOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BigqueryOptions:
    UsePartitionedTables: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryOptions"]:
        if not json_data:
            return None
        return cls(
            UsePartitionedTables=json_data.get("UsePartitionedTables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryOptions = BigqueryOptions


