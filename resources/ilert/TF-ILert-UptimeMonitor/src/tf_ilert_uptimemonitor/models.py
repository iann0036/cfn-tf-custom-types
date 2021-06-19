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
    CheckType: Optional[str]
    CreateIncidentAfterFailedChecks: Optional[float]
    EmbedUrl: Optional[str]
    EscalationPolicy: Optional[str]
    Id: Optional[str]
    IntervalSec: Optional[float]
    Name: Optional[str]
    Paused: Optional[bool]
    Region: Optional[str]
    ShareUrl: Optional[str]
    Status: Optional[str]
    TimeoutMs: Optional[float]
    CheckParams: Optional[Sequence["_CheckParamsDefinition"]]

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
            CheckType=json_data.get("CheckType"),
            CreateIncidentAfterFailedChecks=json_data.get("CreateIncidentAfterFailedChecks"),
            EmbedUrl=json_data.get("EmbedUrl"),
            EscalationPolicy=json_data.get("EscalationPolicy"),
            Id=json_data.get("Id"),
            IntervalSec=json_data.get("IntervalSec"),
            Name=json_data.get("Name"),
            Paused=json_data.get("Paused"),
            Region=json_data.get("Region"),
            ShareUrl=json_data.get("ShareUrl"),
            Status=json_data.get("Status"),
            TimeoutMs=json_data.get("TimeoutMs"),
            CheckParams=deserialize_list(json_data.get("CheckParams"), CheckParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CheckParamsDefinition(BaseModel):
    Host: Optional[str]
    Port: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CheckParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckParamsDefinition = CheckParamsDefinition


