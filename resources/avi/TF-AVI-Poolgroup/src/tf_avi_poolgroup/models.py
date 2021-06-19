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
    CloudConfigCksum: Optional[str]
    CloudRef: Optional[str]
    CreatedBy: Optional[str]
    DeploymentPolicyRef: Optional[str]
    Description: Optional[str]
    EnableHttp2: Optional[bool]
    Id: Optional[str]
    ImplicitPriorityLabels: Optional[bool]
    MinServers: Optional[float]
    Name: Optional[str]
    PriorityLabelsRef: Optional[str]
    ServiceMetadata: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    FailAction: Optional[Sequence["_FailActionDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Members: Optional[Sequence["_MembersDefinition"]]

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
            CloudConfigCksum=json_data.get("CloudConfigCksum"),
            CloudRef=json_data.get("CloudRef"),
            CreatedBy=json_data.get("CreatedBy"),
            DeploymentPolicyRef=json_data.get("DeploymentPolicyRef"),
            Description=json_data.get("Description"),
            EnableHttp2=json_data.get("EnableHttp2"),
            Id=json_data.get("Id"),
            ImplicitPriorityLabels=json_data.get("ImplicitPriorityLabels"),
            MinServers=json_data.get("MinServers"),
            Name=json_data.get("Name"),
            PriorityLabelsRef=json_data.get("PriorityLabelsRef"),
            ServiceMetadata=json_data.get("ServiceMetadata"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            FailAction=deserialize_list(json_data.get("FailAction"), FailActionDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FailActionDefinition(BaseModel):
    Type: Optional[str]
    LocalRsp: Optional[Sequence["_LocalRspDefinition"]]
    Redirect: Optional[Sequence["_RedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FailActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            LocalRsp=deserialize_list(json_data.get("LocalRsp"), LocalRspDefinition),
            Redirect=deserialize_list(json_data.get("Redirect"), RedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailActionDefinition = FailActionDefinition


@dataclass
class LocalRspDefinition(BaseModel):
    StatusCode: Optional[str]
    File: Optional[Sequence["_FileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LocalRspDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalRspDefinition"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
            File=deserialize_list(json_data.get("File"), FileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalRspDefinition = LocalRspDefinition


@dataclass
class FileDefinition(BaseModel):
    ContentType: Optional[str]
    FileContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            FileContent=json_data.get("FileContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileDefinition = FileDefinition


@dataclass
class RedirectDefinition(BaseModel):
    Host: Optional[str]
    Path: Optional[str]
    Protocol: Optional[str]
    Query: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Protocol=json_data.get("Protocol"),
            Query=json_data.get("Query"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectDefinition = RedirectDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class MembersDefinition(BaseModel):
    DeploymentState: Optional[str]
    PoolRef: Optional[str]
    PriorityLabel: Optional[str]
    Ratio: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            DeploymentState=json_data.get("DeploymentState"),
            PoolRef=json_data.get("PoolRef"),
            PriorityLabel=json_data.get("PriorityLabel"),
            Ratio=json_data.get("Ratio"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


