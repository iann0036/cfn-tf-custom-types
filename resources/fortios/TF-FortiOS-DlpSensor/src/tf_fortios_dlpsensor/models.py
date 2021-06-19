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
    Comment: Optional[str]
    DlpLog: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExtendedLog: Optional[str]
    FeatureSet: Optional[str]
    FlowBased: Optional[str]
    FullArchiveProto: Optional[str]
    Id: Optional[str]
    NacQuarLog: Optional[str]
    Name: Optional[str]
    Options: Optional[str]
    ReplacemsgGroup: Optional[str]
    SummaryProto: Optional[str]
    Vdomparam: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

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
            Comment=json_data.get("Comment"),
            DlpLog=json_data.get("DlpLog"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExtendedLog=json_data.get("ExtendedLog"),
            FeatureSet=json_data.get("FeatureSet"),
            FlowBased=json_data.get("FlowBased"),
            FullArchiveProto=json_data.get("FullArchiveProto"),
            Id=json_data.get("Id"),
            NacQuarLog=json_data.get("NacQuarLog"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            SummaryProto=json_data.get("SummaryProto"),
            Vdomparam=json_data.get("Vdomparam"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterDefinition(BaseModel):
    Action: Optional[str]
    Archive: Optional[str]
    CompanyIdentifier: Optional[str]
    Expiry: Optional[str]
    FileSize: Optional[float]
    FileType: Optional[float]
    FilterBy: Optional[str]
    Id: Optional[float]
    MatchPercentage: Optional[float]
    Name: Optional[str]
    Proto: Optional[str]
    Regexp: Optional[str]
    Severity: Optional[str]
    Type: Optional[str]
    FpSensitivity: Optional[Sequence["_FpSensitivityDefinition"]]
    Sensitivity: Optional[Sequence["_SensitivityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Archive=json_data.get("Archive"),
            CompanyIdentifier=json_data.get("CompanyIdentifier"),
            Expiry=json_data.get("Expiry"),
            FileSize=json_data.get("FileSize"),
            FileType=json_data.get("FileType"),
            FilterBy=json_data.get("FilterBy"),
            Id=json_data.get("Id"),
            MatchPercentage=json_data.get("MatchPercentage"),
            Name=json_data.get("Name"),
            Proto=json_data.get("Proto"),
            Regexp=json_data.get("Regexp"),
            Severity=json_data.get("Severity"),
            Type=json_data.get("Type"),
            FpSensitivity=deserialize_list(json_data.get("FpSensitivity"), FpSensitivityDefinition),
            Sensitivity=deserialize_list(json_data.get("Sensitivity"), SensitivityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class FpSensitivityDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FpSensitivityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FpSensitivityDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FpSensitivityDefinition = FpSensitivityDefinition


@dataclass
class SensitivityDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SensitivityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitivityDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitivityDefinition = SensitivityDefinition


