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
    AlgProcessing: Optional[str]
    DisableIpFwSessions: Optional[float]
    ExtendedMatching: Optional[str]
    Id: Optional[str]
    ListenOnPortTimeout: Optional[float]
    NatipDdosProtection: Optional[str]
    PermitDefaultAction: Optional[str]
    RespondToUserMac: Optional[float]
    Uuid: Optional[str]
    DisableAppList: Optional[Sequence["_DisableAppListDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

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
            AlgProcessing=json_data.get("AlgProcessing"),
            DisableIpFwSessions=json_data.get("DisableIpFwSessions"),
            ExtendedMatching=json_data.get("ExtendedMatching"),
            Id=json_data.get("Id"),
            ListenOnPortTimeout=json_data.get("ListenOnPortTimeout"),
            NatipDdosProtection=json_data.get("NatipDdosProtection"),
            PermitDefaultAction=json_data.get("PermitDefaultAction"),
            RespondToUserMac=json_data.get("RespondToUserMac"),
            Uuid=json_data.get("Uuid"),
            DisableAppList=deserialize_list(json_data.get("DisableAppList"), DisableAppListDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DisableAppListDefinition(BaseModel):
    DisableApplicationCategory: Optional[str]
    DisableApplicationProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DisableAppListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisableAppListDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableApplicationCategory=json_data.get("DisableApplicationCategory"),
            DisableApplicationProtocol=json_data.get("DisableApplicationProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisableAppListDefinition = DisableAppListDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


