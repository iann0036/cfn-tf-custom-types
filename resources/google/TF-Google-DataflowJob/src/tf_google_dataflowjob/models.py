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
    AdditionalExperiments: Optional[Sequence[str]]
    EnableStreamingEngine: Optional[bool]
    Id: Optional[str]
    IpConfiguration: Optional[str]
    JobId: Optional[str]
    KmsKeyName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MachineType: Optional[str]
    MaxWorkers: Optional[float]
    Name: Optional[str]
    Network: Optional[str]
    OnDelete: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    Project: Optional[str]
    Region: Optional[str]
    ServiceAccountEmail: Optional[str]
    State: Optional[str]
    Subnetwork: Optional[str]
    TempGcsLocation: Optional[str]
    TemplateGcsPath: Optional[str]
    TransformNameMapping: Optional[Sequence["_TransformNameMappingDefinition"]]
    Type: Optional[str]
    Zone: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AdditionalExperiments=json_data.get("AdditionalExperiments"),
            EnableStreamingEngine=json_data.get("EnableStreamingEngine"),
            Id=json_data.get("Id"),
            IpConfiguration=json_data.get("IpConfiguration"),
            JobId=json_data.get("JobId"),
            KmsKeyName=json_data.get("KmsKeyName"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MachineType=json_data.get("MachineType"),
            MaxWorkers=json_data.get("MaxWorkers"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            OnDelete=json_data.get("OnDelete"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            State=json_data.get("State"),
            Subnetwork=json_data.get("Subnetwork"),
            TempGcsLocation=json_data.get("TempGcsLocation"),
            TemplateGcsPath=json_data.get("TemplateGcsPath"),
            TransformNameMapping=deserialize_list(json_data.get("TransformNameMapping"), TransformNameMappingDefinition),
            Type=json_data.get("Type"),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TransformNameMappingDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransformNameMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformNameMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformNameMappingDefinition = TransformNameMappingDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


