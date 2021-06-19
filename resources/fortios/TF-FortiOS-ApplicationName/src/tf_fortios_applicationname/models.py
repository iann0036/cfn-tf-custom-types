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
    Category: Optional[float]
    DynamicSortSubtable: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Parameter: Optional[str]
    Popularity: Optional[float]
    Protocol: Optional[str]
    Risk: Optional[float]
    SubCategory: Optional[float]
    Technology: Optional[str]
    Vdomparam: Optional[str]
    Vendor: Optional[str]
    Weight: Optional[float]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

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
            Category=json_data.get("Category"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parameter=json_data.get("Parameter"),
            Popularity=json_data.get("Popularity"),
            Protocol=json_data.get("Protocol"),
            Risk=json_data.get("Risk"),
            SubCategory=json_data.get("SubCategory"),
            Technology=json_data.get("Technology"),
            Vdomparam=json_data.get("Vdomparam"),
            Vendor=json_data.get("Vendor"),
            Weight=json_data.get("Weight"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Id: Optional[float]
    Metaid: Optional[float]
    Valueid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Metaid=json_data.get("Metaid"),
            Valueid=json_data.get("Valueid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


