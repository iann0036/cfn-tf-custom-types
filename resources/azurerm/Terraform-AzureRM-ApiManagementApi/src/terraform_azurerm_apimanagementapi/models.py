# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    ApiManagementName: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsCurrent: Optional[bool]
    IsOnline: Optional[bool]
    Name: Optional[str]
    Path: Optional[str]
    Protocols: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Revision: Optional[str]
    ServiceUrl: Optional[str]
    SoapPassThrough: Optional[bool]
    Version: Optional[str]
    VersionSetId: Optional[str]
    Import: Optional[Sequence["_Import"]]
    SubscriptionKeyParameterNames: Optional[Sequence["_SubscriptionKeyParameterNames"]]
    Timeouts: Optional["_Timeouts"]
    WsdlSelector: Optional[Sequence["_WsdlSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiManagementName=json_data.get("ApiManagementName"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsCurrent=json_data.get("IsCurrent"),
            IsOnline=json_data.get("IsOnline"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Protocols=json_data.get("Protocols"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Revision=json_data.get("Revision"),
            ServiceUrl=json_data.get("ServiceUrl"),
            SoapPassThrough=json_data.get("SoapPassThrough"),
            Version=json_data.get("Version"),
            VersionSetId=json_data.get("VersionSetId"),
            Import=json_data.get("Import"),
            SubscriptionKeyParameterNames=json_data.get("SubscriptionKeyParameterNames"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WsdlSelector=json_data.get("WsdlSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Import:
    ContentFormat: Optional[str]
    ContentValue: Optional[str]
    WsdlSelector: Optional[Sequence["_WsdlSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_Import"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Import"]:
        if not json_data:
            return None
        return cls(
            ContentFormat=json_data.get("ContentFormat"),
            ContentValue=json_data.get("ContentValue"),
            WsdlSelector=json_data.get("WsdlSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Import = Import


@dataclass
class WsdlSelector:
    EndpointName: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WsdlSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WsdlSelector"]:
        if not json_data:
            return None
        return cls(
            EndpointName=json_data.get("EndpointName"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WsdlSelector = WsdlSelector


@dataclass
class SubscriptionKeyParameterNames:
    Header: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubscriptionKeyParameterNames"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubscriptionKeyParameterNames"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubscriptionKeyParameterNames = SubscriptionKeyParameterNames


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


