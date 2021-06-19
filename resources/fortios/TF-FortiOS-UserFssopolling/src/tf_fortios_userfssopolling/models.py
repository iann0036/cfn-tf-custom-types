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
    DefaultDomain: Optional[str]
    DynamicSortSubtable: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    LdapServer: Optional[str]
    LogonHistory: Optional[float]
    Password: Optional[str]
    PollingFrequency: Optional[float]
    Port: Optional[float]
    Server: Optional[str]
    SmbNtlmv1Auth: Optional[str]
    Smbv1: Optional[str]
    Status: Optional[str]
    User: Optional[str]
    Vdomparam: Optional[str]
    Adgrp: Optional[Sequence["_AdgrpDefinition"]]

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
            DefaultDomain=json_data.get("DefaultDomain"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            LdapServer=json_data.get("LdapServer"),
            LogonHistory=json_data.get("LogonHistory"),
            Password=json_data.get("Password"),
            PollingFrequency=json_data.get("PollingFrequency"),
            Port=json_data.get("Port"),
            Server=json_data.get("Server"),
            SmbNtlmv1Auth=json_data.get("SmbNtlmv1Auth"),
            Smbv1=json_data.get("Smbv1"),
            Status=json_data.get("Status"),
            User=json_data.get("User"),
            Vdomparam=json_data.get("Vdomparam"),
            Adgrp=deserialize_list(json_data.get("Adgrp"), AdgrpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdgrpDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdgrpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdgrpDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdgrpDefinition = AdgrpDefinition


