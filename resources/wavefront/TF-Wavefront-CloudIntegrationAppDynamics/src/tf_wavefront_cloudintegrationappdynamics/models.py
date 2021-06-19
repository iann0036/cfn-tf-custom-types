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
    AdditionalTags: Optional[Sequence["_AdditionalTagsDefinition"]]
    AppFilterRegex: Optional[Sequence[str]]
    ControllerName: Optional[str]
    EnableAppInfraMetrics: Optional[bool]
    EnableBackendMetrics: Optional[bool]
    EnableBusinessTrxMetrics: Optional[bool]
    EnableErrorMetrics: Optional[bool]
    EnableIndividualNodeMetrics: Optional[bool]
    EnableOverallPerfMetrics: Optional[bool]
    EnableRollup: Optional[bool]
    EnableServiceEndpointMetrics: Optional[bool]
    EncryptedPassword: Optional[str]
    ForceSave: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Service: Optional[str]
    ServiceRefreshRateInMinutes: Optional[float]
    UserName: Optional[str]

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
            AdditionalTags=deserialize_list(json_data.get("AdditionalTags"), AdditionalTagsDefinition),
            AppFilterRegex=json_data.get("AppFilterRegex"),
            ControllerName=json_data.get("ControllerName"),
            EnableAppInfraMetrics=json_data.get("EnableAppInfraMetrics"),
            EnableBackendMetrics=json_data.get("EnableBackendMetrics"),
            EnableBusinessTrxMetrics=json_data.get("EnableBusinessTrxMetrics"),
            EnableErrorMetrics=json_data.get("EnableErrorMetrics"),
            EnableIndividualNodeMetrics=json_data.get("EnableIndividualNodeMetrics"),
            EnableOverallPerfMetrics=json_data.get("EnableOverallPerfMetrics"),
            EnableRollup=json_data.get("EnableRollup"),
            EnableServiceEndpointMetrics=json_data.get("EnableServiceEndpointMetrics"),
            EncryptedPassword=json_data.get("EncryptedPassword"),
            ForceSave=json_data.get("ForceSave"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Service=json_data.get("Service"),
            ServiceRefreshRateInMinutes=json_data.get("ServiceRefreshRateInMinutes"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalTagsDefinition = AdditionalTagsDefinition


