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
    FqdnEnabled: Optional[bool]
    FqdnMode: Optional[str]
    FqdnTag: Optional[str]
    Id: Optional[str]
    ManageDomainNames: Optional[bool]
    DomainNames: Optional[Sequence["_DomainNamesDefinition"]]
    GwFilterTagList: Optional[Sequence["_GwFilterTagListDefinition"]]

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
            FqdnEnabled=json_data.get("FqdnEnabled"),
            FqdnMode=json_data.get("FqdnMode"),
            FqdnTag=json_data.get("FqdnTag"),
            Id=json_data.get("Id"),
            ManageDomainNames=json_data.get("ManageDomainNames"),
            DomainNames=deserialize_list(json_data.get("DomainNames"), DomainNamesDefinition),
            GwFilterTagList=deserialize_list(json_data.get("GwFilterTagList"), GwFilterTagListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DomainNamesDefinition(BaseModel):
    Action: Optional[str]
    Fqdn: Optional[str]
    Port: Optional[str]
    Proto: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Fqdn=json_data.get("Fqdn"),
            Port=json_data.get("Port"),
            Proto=json_data.get("Proto"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainNamesDefinition = DomainNamesDefinition


@dataclass
class GwFilterTagListDefinition(BaseModel):
    GwName: Optional[str]
    SourceIpList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GwFilterTagListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GwFilterTagListDefinition"]:
        if not json_data:
            return None
        return cls(
            GwName=json_data.get("GwName"),
            SourceIpList=json_data.get("SourceIpList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GwFilterTagListDefinition = GwFilterTagListDefinition


