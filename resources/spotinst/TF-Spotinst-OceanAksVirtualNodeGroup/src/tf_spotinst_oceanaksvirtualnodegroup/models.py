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
    Id: Optional[str]
    Name: Optional[str]
    OceanId: Optional[str]
    Autoscale: Optional[Sequence["_AutoscaleDefinition"]]
    Label: Optional[Sequence["_LabelDefinition"]]
    LaunchSpecification: Optional[Sequence["_LaunchSpecificationDefinition"]]
    ResourceLimits: Optional[Sequence["_ResourceLimitsDefinition"]]
    Taint: Optional[Sequence["_TaintDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OceanId=json_data.get("OceanId"),
            Autoscale=deserialize_list(json_data.get("Autoscale"), AutoscaleDefinition),
            Label=deserialize_list(json_data.get("Label"), LabelDefinition),
            LaunchSpecification=deserialize_list(json_data.get("LaunchSpecification"), LaunchSpecificationDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
            Taint=deserialize_list(json_data.get("Taint"), TaintDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscaleDefinition(BaseModel):
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDefinition = AutoscaleDefinition


@dataclass
class AutoscaleHeadroomDefinition(BaseModel):
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroomDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroomDefinition = AutoscaleHeadroomDefinition


@dataclass
class LabelDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelDefinition = LabelDefinition


@dataclass
class LaunchSpecificationDefinition(BaseModel):
    OsDisk: Optional[Sequence["_OsDiskDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            OsDisk=deserialize_list(json_data.get("OsDisk"), OsDiskDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchSpecificationDefinition = LaunchSpecificationDefinition


@dataclass
class OsDiskDefinition(BaseModel):
    SizeGb: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            SizeGb=json_data.get("SizeGb"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDiskDefinition = OsDiskDefinition


@dataclass
class TagDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class ResourceLimitsDefinition(BaseModel):
    MaxInstanceCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxInstanceCount=json_data.get("MaxInstanceCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitsDefinition = ResourceLimitsDefinition


@dataclass
class TaintDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintDefinition = TaintDefinition


