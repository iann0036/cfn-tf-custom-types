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
    ApiName: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Method: Optional[str]
    OperationId: Optional[str]
    ResourceGroupName: Optional[str]
    UrlTemplate: Optional[str]
    Request: Optional[Sequence["_Request"]]
    Response: Optional[Sequence["_Response"]]
    TemplateParameter: Optional[Sequence["_TemplateParameter"]]
    Timeouts: Optional["_Timeouts"]
    Header: Optional[Sequence["_Header"]]
    QueryParameter: Optional[Sequence["_QueryParameter"]]
    Representation: Optional[Sequence["_Representation"]]
    FormParameter: Optional[Sequence["_FormParameter"]]

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
            ApiName=json_data.get("ApiName"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Method=json_data.get("Method"),
            OperationId=json_data.get("OperationId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            UrlTemplate=json_data.get("UrlTemplate"),
            Request=json_data.get("Request"),
            Response=json_data.get("Response"),
            TemplateParameter=json_data.get("TemplateParameter"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Header=json_data.get("Header"),
            QueryParameter=json_data.get("QueryParameter"),
            Representation=json_data.get("Representation"),
            FormParameter=json_data.get("FormParameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Request:
    Description: Optional[str]
    Header: Optional[Sequence["_Header"]]
    QueryParameter: Optional[Sequence["_QueryParameter"]]
    Representation: Optional[Sequence["_Representation"]]

    @classmethod
    def _deserialize(
        cls: Type["_Request"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Request"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Header=json_data.get("Header"),
            QueryParameter=json_data.get("QueryParameter"),
            Representation=json_data.get("Representation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Request = Request


@dataclass
class Header:
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Header = Header


@dataclass
class QueryParameter:
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameter"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParameter = QueryParameter


@dataclass
class Representation:
    ContentType: Optional[str]
    Sample: Optional[str]
    SchemaId: Optional[str]
    TypeName: Optional[str]
    FormParameter: Optional[Sequence["_FormParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Representation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Representation"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            Sample=json_data.get("Sample"),
            SchemaId=json_data.get("SchemaId"),
            TypeName=json_data.get("TypeName"),
            FormParameter=json_data.get("FormParameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Representation = Representation


@dataclass
class FormParameter:
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FormParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormParameter"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormParameter = FormParameter


@dataclass
class Response:
    Description: Optional[str]
    StatusCode: Optional[float]
    Header: Optional[Sequence["_Header"]]
    Representation: Optional[Sequence["_Representation"]]

    @classmethod
    def _deserialize(
        cls: Type["_Response"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Response"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            StatusCode=json_data.get("StatusCode"),
            Header=json_data.get("Header"),
            Representation=json_data.get("Representation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Response = Response


@dataclass
class TemplateParameter:
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateParameter"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateParameter = TemplateParameter


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


