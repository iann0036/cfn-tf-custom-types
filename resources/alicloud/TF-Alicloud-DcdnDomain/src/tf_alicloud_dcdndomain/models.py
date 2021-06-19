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
    CertName: Optional[str]
    CertType: Optional[str]
    CheckUrl: Optional[str]
    DomainName: Optional[str]
    ForceSet: Optional[str]
    Id: Optional[str]
    ResourceGroupId: Optional[str]
    Scope: Optional[str]
    SecurityToken: Optional[str]
    SslPri: Optional[str]
    SslProtocol: Optional[str]
    SslPub: Optional[str]
    Status: Optional[str]
    TopLevelDomain: Optional[str]
    Sources: Optional[Sequence["_SourcesDefinition"]]
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
            CertName=json_data.get("CertName"),
            CertType=json_data.get("CertType"),
            CheckUrl=json_data.get("CheckUrl"),
            DomainName=json_data.get("DomainName"),
            ForceSet=json_data.get("ForceSet"),
            Id=json_data.get("Id"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Scope=json_data.get("Scope"),
            SecurityToken=json_data.get("SecurityToken"),
            SslPri=json_data.get("SslPri"),
            SslProtocol=json_data.get("SslProtocol"),
            SslPub=json_data.get("SslPub"),
            Status=json_data.get("Status"),
            TopLevelDomain=json_data.get("TopLevelDomain"),
            Sources=deserialize_list(json_data.get("Sources"), SourcesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SourcesDefinition(BaseModel):
    Content: Optional[str]
    Port: Optional[float]
    Priority: Optional[str]
    Type: Optional[str]
    Weight: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcesDefinition = SourcesDefinition


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


