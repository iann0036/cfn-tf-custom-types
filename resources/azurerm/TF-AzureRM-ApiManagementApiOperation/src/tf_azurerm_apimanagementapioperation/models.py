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
    ApiManagementName: Optional[str]
    ApiName: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Method: Optional[str]
    OperationId: Optional[str]
    ResourceGroupName: Optional[str]
    UrlTemplate: Optional[str]
    Request: Optional[Sequence["_RequestDefinition"]]
    Response: Optional[Sequence["_ResponseDefinition"]]
    TemplateParameter: Optional[Sequence["_TemplateParameterDefinition"]]
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
            ApiManagementName=json_data.get("ApiManagementName"),
            ApiName=json_data.get("ApiName"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Method=json_data.get("Method"),
            OperationId=json_data.get("OperationId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            UrlTemplate=json_data.get("UrlTemplate"),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
            Response=deserialize_list(json_data.get("Response"), ResponseDefinition),
            TemplateParameter=deserialize_list(json_data.get("TemplateParameter"), TemplateParameterDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestDefinition(BaseModel):
    Description: Optional[str]
    Header: Optional[Sequence["_HeaderDefinition"]]
    QueryParameter: Optional[Sequence["_QueryParameterDefinition"]]
    Representation: Optional[Sequence["_RepresentationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            QueryParameter=deserialize_list(json_data.get("QueryParameter"), QueryParameterDefinition),
            Representation=deserialize_list(json_data.get("Representation"), RepresentationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestDefinition = RequestDefinition


@dataclass
class HeaderDefinition(BaseModel):
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
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
_HeaderDefinition = HeaderDefinition


@dataclass
class QueryParameterDefinition(BaseModel):
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameterDefinition"]:
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
_QueryParameterDefinition = QueryParameterDefinition


@dataclass
class RepresentationDefinition(BaseModel):
    ContentType: Optional[str]
    Sample: Optional[str]
    SchemaId: Optional[str]
    TypeName: Optional[str]
    FormParameter: Optional[Sequence["_FormParameterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RepresentationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepresentationDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            Sample=json_data.get("Sample"),
            SchemaId=json_data.get("SchemaId"),
            TypeName=json_data.get("TypeName"),
            FormParameter=deserialize_list(json_data.get("FormParameter"), FormParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepresentationDefinition = RepresentationDefinition


@dataclass
class FormParameterDefinition(BaseModel):
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FormParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormParameterDefinition"]:
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
_FormParameterDefinition = FormParameterDefinition


@dataclass
class ResponseDefinition(BaseModel):
    Description: Optional[str]
    StatusCode: Optional[float]
    Header: Optional[Sequence["_HeaderDefinition"]]
    Representation: Optional[Sequence["_RepresentationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            StatusCode=json_data.get("StatusCode"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            Representation=deserialize_list(json_data.get("Representation"), RepresentationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseDefinition = ResponseDefinition


@dataclass
class TemplateParameterDefinition(BaseModel):
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateParameterDefinition"]:
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
_TemplateParameterDefinition = TemplateParameterDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


