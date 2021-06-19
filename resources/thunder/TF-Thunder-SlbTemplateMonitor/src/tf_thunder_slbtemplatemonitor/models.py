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
    Id2: Optional[float]
    MonitorRelation: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    ClearCfg: Optional[Sequence["_ClearCfgDefinition"]]
    LinkDisableCfg: Optional[Sequence["_LinkDisableCfgDefinition"]]
    LinkDownCfg: Optional[Sequence["_LinkDownCfgDefinition"]]
    LinkEnableCfg: Optional[Sequence["_LinkEnableCfgDefinition"]]
    LinkUpCfg: Optional[Sequence["_LinkUpCfgDefinition"]]

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
            Id2=json_data.get("Id2"),
            MonitorRelation=json_data.get("MonitorRelation"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            ClearCfg=deserialize_list(json_data.get("ClearCfg"), ClearCfgDefinition),
            LinkDisableCfg=deserialize_list(json_data.get("LinkDisableCfg"), LinkDisableCfgDefinition),
            LinkDownCfg=deserialize_list(json_data.get("LinkDownCfg"), LinkDownCfgDefinition),
            LinkEnableCfg=deserialize_list(json_data.get("LinkEnableCfg"), LinkEnableCfgDefinition),
            LinkUpCfg=deserialize_list(json_data.get("LinkUpCfg"), LinkUpCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClearCfgDefinition(BaseModel):
    ClearAllSequence: Optional[float]
    ClearSequence: Optional[float]
    Sessions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClearCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClearCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            ClearAllSequence=json_data.get("ClearAllSequence"),
            ClearSequence=json_data.get("ClearSequence"),
            Sessions=json_data.get("Sessions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClearCfgDefinition = ClearCfgDefinition


@dataclass
class LinkDisableCfgDefinition(BaseModel):
    DisSequence: Optional[float]
    Diseth: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LinkDisableCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkDisableCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            DisSequence=json_data.get("DisSequence"),
            Diseth=json_data.get("Diseth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkDisableCfgDefinition = LinkDisableCfgDefinition


@dataclass
class LinkDownCfgDefinition(BaseModel):
    LinkDownSequence1: Optional[float]
    LinkDownSequence2: Optional[float]
    LinkDownSequence3: Optional[float]
    LinkdownEthernet1: Optional[float]
    LinkdownEthernet2: Optional[float]
    LinkdownEthernet3: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LinkDownCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkDownCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkDownSequence1=json_data.get("LinkDownSequence1"),
            LinkDownSequence2=json_data.get("LinkDownSequence2"),
            LinkDownSequence3=json_data.get("LinkDownSequence3"),
            LinkdownEthernet1=json_data.get("LinkdownEthernet1"),
            LinkdownEthernet2=json_data.get("LinkdownEthernet2"),
            LinkdownEthernet3=json_data.get("LinkdownEthernet3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkDownCfgDefinition = LinkDownCfgDefinition


@dataclass
class LinkEnableCfgDefinition(BaseModel):
    EnaSequence: Optional[float]
    Enaeth: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LinkEnableCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkEnableCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            EnaSequence=json_data.get("EnaSequence"),
            Enaeth=json_data.get("Enaeth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkEnableCfgDefinition = LinkEnableCfgDefinition


@dataclass
class LinkUpCfgDefinition(BaseModel):
    LinkUpSequence1: Optional[float]
    LinkUpSequence2: Optional[float]
    LinkUpSequence3: Optional[float]
    LinkupEthernet1: Optional[float]
    LinkupEthernet2: Optional[float]
    LinkupEthernet3: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LinkUpCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkUpCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkUpSequence1=json_data.get("LinkUpSequence1"),
            LinkUpSequence2=json_data.get("LinkUpSequence2"),
            LinkUpSequence3=json_data.get("LinkUpSequence3"),
            LinkupEthernet1=json_data.get("LinkupEthernet1"),
            LinkupEthernet2=json_data.get("LinkupEthernet2"),
            LinkupEthernet3=json_data.get("LinkupEthernet3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkUpCfgDefinition = LinkUpCfgDefinition


