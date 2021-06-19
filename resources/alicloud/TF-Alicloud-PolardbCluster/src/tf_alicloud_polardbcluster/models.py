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
    AutoRenewPeriod: Optional[float]
    CollectorStatus: Optional[str]
    ConnectionString: Optional[str]
    DbNodeClass: Optional[str]
    DbNodeCount: Optional[float]
    DbType: Optional[str]
    DbVersion: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    MaintainTime: Optional[str]
    ModifyType: Optional[str]
    PayType: Optional[str]
    Period: Optional[float]
    RenewalStatus: Optional[str]
    ResourceGroupId: Optional[str]
    SecurityIps: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TdeStatus: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
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
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            CollectorStatus=json_data.get("CollectorStatus"),
            ConnectionString=json_data.get("ConnectionString"),
            DbNodeClass=json_data.get("DbNodeClass"),
            DbNodeCount=json_data.get("DbNodeCount"),
            DbType=json_data.get("DbType"),
            DbVersion=json_data.get("DbVersion"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaintainTime=json_data.get("MaintainTime"),
            ModifyType=json_data.get("ModifyType"),
            PayType=json_data.get("PayType"),
            Period=json_data.get("Period"),
            RenewalStatus=json_data.get("RenewalStatus"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityIps=json_data.get("SecurityIps"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TdeStatus=json_data.get("TdeStatus"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


