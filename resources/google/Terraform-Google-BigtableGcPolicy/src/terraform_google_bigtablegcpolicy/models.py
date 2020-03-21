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
    ColumnFamily: Optional[str]
    InstanceName: Optional[str]
    Mode: Optional[str]
    Project: Optional[str]
    Table: Optional[str]
    MaxAge: Optional[Sequence["_MaxAge"]]
    MaxVersion: Optional[Sequence["_MaxVersion"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ColumnFamily=json_data.get("ColumnFamily"),
            InstanceName=json_data.get("InstanceName"),
            Mode=json_data.get("Mode"),
            Project=json_data.get("Project"),
            Table=json_data.get("Table"),
            MaxAge=json_data.get("MaxAge"),
            MaxVersion=json_data.get("MaxVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MaxAge:
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaxAge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxAge"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxAge = MaxAge


@dataclass
class MaxVersion:
    Number: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaxVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxVersion"]:
        if not json_data:
            return None
        return cls(
            Number=json_data.get("Number"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxVersion = MaxVersion


