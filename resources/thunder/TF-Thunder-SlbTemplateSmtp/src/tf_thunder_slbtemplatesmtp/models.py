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
    ClientStarttlsType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServerDomain: Optional[str]
    ServerStarttlsType: Optional[str]
    ServiceReadyMsg: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    ClientDomainSwitching: Optional[Sequence["_ClientDomainSwitchingDefinition"]]
    CommandDisable: Optional[Sequence["_CommandDisableDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]

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
            ClientStarttlsType=json_data.get("ClientStarttlsType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServerDomain=json_data.get("ServerDomain"),
            ServerStarttlsType=json_data.get("ServerStarttlsType"),
            ServiceReadyMsg=json_data.get("ServiceReadyMsg"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            ClientDomainSwitching=deserialize_list(json_data.get("ClientDomainSwitching"), ClientDomainSwitchingDefinition),
            CommandDisable=deserialize_list(json_data.get("CommandDisable"), CommandDisableDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClientDomainSwitchingDefinition(BaseModel):
    MatchString: Optional[str]
    ServiceGroup: Optional[str]
    SwitchingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientDomainSwitchingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientDomainSwitchingDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchString=json_data.get("MatchString"),
            ServiceGroup=json_data.get("ServiceGroup"),
            SwitchingType=json_data.get("SwitchingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientDomainSwitchingDefinition = ClientDomainSwitchingDefinition


@dataclass
class CommandDisableDefinition(BaseModel):
    DisableType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CommandDisableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommandDisableDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableType=json_data.get("DisableType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommandDisableDefinition = CommandDisableDefinition


@dataclass
class TemplateDefinition(BaseModel):
    Logging: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Logging=json_data.get("Logging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


