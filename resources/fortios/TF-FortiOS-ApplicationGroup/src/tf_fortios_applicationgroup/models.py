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
    Behavior: Optional[str]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Popularity: Optional[str]
    Protocols: Optional[str]
    Technology: Optional[str]
    Type: Optional[str]
    Vdomparam: Optional[str]
    Vendor: Optional[str]
    Application: Optional[Sequence["_ApplicationDefinition"]]
    Category: Optional[Sequence["_CategoryDefinition"]]
    Risk: Optional[Sequence["_RiskDefinition"]]

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
            Behavior=json_data.get("Behavior"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Popularity=json_data.get("Popularity"),
            Protocols=json_data.get("Protocols"),
            Technology=json_data.get("Technology"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            Vendor=json_data.get("Vendor"),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
            Category=deserialize_list(json_data.get("Category"), CategoryDefinition),
            Risk=deserialize_list(json_data.get("Risk"), RiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDefinition = ApplicationDefinition


@dataclass
class CategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryDefinition = CategoryDefinition


@dataclass
class RiskDefinition(BaseModel):
    Level: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RiskDefinition = RiskDefinition


