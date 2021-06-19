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
    AlertCategories: Optional[Sequence[str]]
    AllowCategories: Optional[Sequence[str]]
    AllowList: Optional[Sequence[str]]
    BlockCategories: Optional[Sequence[str]]
    BlockList: Optional[Sequence[str]]
    BlockListAction: Optional[str]
    ContinueCategories: Optional[Sequence[str]]
    Description: Optional[str]
    DeviceGroup: Optional[str]
    DynamicUrl: Optional[bool]
    ExpiredLicenseAction: Optional[bool]
    Id: Optional[str]
    LogContainerPageOnly: Optional[bool]
    LogHttpHeaderReferer: Optional[bool]
    LogHttpHeaderUserAgent: Optional[bool]
    LogHttpHeaderXff: Optional[bool]
    MachineLearningExceptions: Optional[Sequence[str]]
    Name: Optional[str]
    OverrideCategories: Optional[Sequence[str]]
    SafeSearchEnforcement: Optional[bool]
    TrackContainerPage: Optional[bool]
    UcdAlertCategories: Optional[Sequence[str]]
    UcdAllowCategories: Optional[Sequence[str]]
    UcdBlockCategories: Optional[Sequence[str]]
    UcdContinueCategories: Optional[Sequence[str]]
    UcdLogSeverity: Optional[str]
    UcdMode: Optional[str]
    UcdModeGroupMapping: Optional[str]
    Vsys: Optional[str]
    HttpHeaderInsertion: Optional[Sequence["_HttpHeaderInsertionDefinition"]]
    MachineLearningModel: Optional[Sequence["_MachineLearningModelDefinition"]]

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
            AlertCategories=json_data.get("AlertCategories"),
            AllowCategories=json_data.get("AllowCategories"),
            AllowList=json_data.get("AllowList"),
            BlockCategories=json_data.get("BlockCategories"),
            BlockList=json_data.get("BlockList"),
            BlockListAction=json_data.get("BlockListAction"),
            ContinueCategories=json_data.get("ContinueCategories"),
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            DynamicUrl=json_data.get("DynamicUrl"),
            ExpiredLicenseAction=json_data.get("ExpiredLicenseAction"),
            Id=json_data.get("Id"),
            LogContainerPageOnly=json_data.get("LogContainerPageOnly"),
            LogHttpHeaderReferer=json_data.get("LogHttpHeaderReferer"),
            LogHttpHeaderUserAgent=json_data.get("LogHttpHeaderUserAgent"),
            LogHttpHeaderXff=json_data.get("LogHttpHeaderXff"),
            MachineLearningExceptions=json_data.get("MachineLearningExceptions"),
            Name=json_data.get("Name"),
            OverrideCategories=json_data.get("OverrideCategories"),
            SafeSearchEnforcement=json_data.get("SafeSearchEnforcement"),
            TrackContainerPage=json_data.get("TrackContainerPage"),
            UcdAlertCategories=json_data.get("UcdAlertCategories"),
            UcdAllowCategories=json_data.get("UcdAllowCategories"),
            UcdBlockCategories=json_data.get("UcdBlockCategories"),
            UcdContinueCategories=json_data.get("UcdContinueCategories"),
            UcdLogSeverity=json_data.get("UcdLogSeverity"),
            UcdMode=json_data.get("UcdMode"),
            UcdModeGroupMapping=json_data.get("UcdModeGroupMapping"),
            Vsys=json_data.get("Vsys"),
            HttpHeaderInsertion=deserialize_list(json_data.get("HttpHeaderInsertion"), HttpHeaderInsertionDefinition),
            MachineLearningModel=deserialize_list(json_data.get("MachineLearningModel"), MachineLearningModelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HttpHeaderInsertionDefinition(BaseModel):
    Domains: Optional[Sequence[str]]
    Name: Optional[str]
    Type: Optional[str]
    HttpHeader: Optional[Sequence["_HttpHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderInsertionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderInsertionDefinition"]:
        if not json_data:
            return None
        return cls(
            Domains=json_data.get("Domains"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            HttpHeader=deserialize_list(json_data.get("HttpHeader"), HttpHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderInsertionDefinition = HttpHeaderInsertionDefinition


@dataclass
class HttpHeaderDefinition(BaseModel):
    Header: Optional[str]
    Log: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Log=json_data.get("Log"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderDefinition = HttpHeaderDefinition


@dataclass
class MachineLearningModelDefinition(BaseModel):
    Action: Optional[str]
    Model: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineLearningModelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineLearningModelDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Model=json_data.get("Model"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineLearningModelDefinition = MachineLearningModelDefinition


