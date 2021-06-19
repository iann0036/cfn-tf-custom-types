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
    Label: Optional[str]
    PartitionType: Optional[str]
    TaggedOnly: Optional[bool]
    Unknowns: Optional[str]
    AuthenticationData: Optional[Sequence["_AuthenticationDataDefinition"]]
    SupportingServicesToMonitor: Optional[Sequence["_SupportingServicesToMonitorDefinition"]]
    TagsToMonitor: Optional[Sequence["_TagsToMonitorDefinition"]]

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
            Label=json_data.get("Label"),
            PartitionType=json_data.get("PartitionType"),
            TaggedOnly=json_data.get("TaggedOnly"),
            Unknowns=json_data.get("Unknowns"),
            AuthenticationData=deserialize_list(json_data.get("AuthenticationData"), AuthenticationDataDefinition),
            SupportingServicesToMonitor=deserialize_list(json_data.get("SupportingServicesToMonitor"), SupportingServicesToMonitorDefinition),
            TagsToMonitor=deserialize_list(json_data.get("TagsToMonitor"), TagsToMonitorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthenticationDataDefinition(BaseModel):
    AccessKey: Optional[str]
    AccountId: Optional[str]
    ExternalId: Optional[str]
    IamRole: Optional[str]
    SecretKey: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            AccountId=json_data.get("AccountId"),
            ExternalId=json_data.get("ExternalId"),
            IamRole=json_data.get("IamRole"),
            SecretKey=json_data.get("SecretKey"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDataDefinition = AuthenticationDataDefinition


@dataclass
class SupportingServicesToMonitorDefinition(BaseModel):
    Name: Optional[str]
    Unknowns: Optional[str]
    MonitoredMetrics: Optional[Sequence["_MonitoredMetricsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupportingServicesToMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportingServicesToMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            MonitoredMetrics=deserialize_list(json_data.get("MonitoredMetrics"), MonitoredMetricsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportingServicesToMonitorDefinition = SupportingServicesToMonitorDefinition


@dataclass
class MonitoredMetricsDefinition(BaseModel):
    Dimensions: Optional[Sequence[str]]
    Name: Optional[str]
    Statistic: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoredMetricsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoredMetricsDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimensions=json_data.get("Dimensions"),
            Name=json_data.get("Name"),
            Statistic=json_data.get("Statistic"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoredMetricsDefinition = MonitoredMetricsDefinition


@dataclass
class TagsToMonitorDefinition(BaseModel):
    Name: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsToMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsToMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsToMonitorDefinition = TagsToMonitorDefinition


