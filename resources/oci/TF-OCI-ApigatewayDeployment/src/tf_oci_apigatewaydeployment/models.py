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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    Endpoint: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    GatewayId: Optional[str]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    PathPrefix: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Specification: Optional[Sequence["_SpecificationDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            Endpoint=json_data.get("Endpoint"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            GatewayId=json_data.get("GatewayId"),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            PathPrefix=json_data.get("PathPrefix"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Specification=deserialize_list(json_data.get("Specification"), SpecificationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class SpecificationDefinition(BaseModel):
    LoggingPolicies: Optional[Sequence["_LoggingPoliciesDefinition"]]
    RequestPolicies: Optional[Sequence["_RequestPoliciesDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            LoggingPolicies=deserialize_list(json_data.get("LoggingPolicies"), LoggingPoliciesDefinition),
            RequestPolicies=deserialize_list(json_data.get("RequestPolicies"), RequestPoliciesDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecificationDefinition = SpecificationDefinition


@dataclass
class LoggingPoliciesDefinition(BaseModel):
    AccessLog: Optional[Sequence["_AccessLogDefinition"]]
    ExecutionLog: Optional[Sequence["_ExecutionLogDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessLog=deserialize_list(json_data.get("AccessLog"), AccessLogDefinition),
            ExecutionLog=deserialize_list(json_data.get("ExecutionLog"), ExecutionLogDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingPoliciesDefinition = LoggingPoliciesDefinition


@dataclass
class AccessLogDefinition(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogDefinition = AccessLogDefinition


@dataclass
class ExecutionLogDefinition(BaseModel):
    IsEnabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionLogDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionLogDefinition = ExecutionLogDefinition


@dataclass
class RequestPoliciesDefinition(BaseModel):
    Authorization: Optional[Sequence["_AuthorizationDefinition"]]
    BodyValidation: Optional[Sequence["_BodyValidationDefinition"]]
    Cors: Optional[Sequence["_CorsDefinition"]]
    HeaderTransformations: Optional[Sequence["_HeaderTransformationsDefinition"]]
    HeaderValidations: Optional[Sequence["_HeaderValidationsDefinition"]]
    QueryParameterTransformations: Optional[Sequence["_QueryParameterTransformationsDefinition"]]
    QueryParameterValidations: Optional[Sequence["_QueryParameterValidationsDefinition"]]
    ResponseCacheLookup: Optional[Sequence["_ResponseCacheLookupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Authorization=deserialize_list(json_data.get("Authorization"), AuthorizationDefinition),
            BodyValidation=deserialize_list(json_data.get("BodyValidation"), BodyValidationDefinition),
            Cors=deserialize_list(json_data.get("Cors"), CorsDefinition),
            HeaderTransformations=deserialize_list(json_data.get("HeaderTransformations"), HeaderTransformationsDefinition),
            HeaderValidations=deserialize_list(json_data.get("HeaderValidations"), HeaderValidationsDefinition),
            QueryParameterTransformations=deserialize_list(json_data.get("QueryParameterTransformations"), QueryParameterTransformationsDefinition),
            QueryParameterValidations=deserialize_list(json_data.get("QueryParameterValidations"), QueryParameterValidationsDefinition),
            ResponseCacheLookup=deserialize_list(json_data.get("ResponseCacheLookup"), ResponseCacheLookupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestPoliciesDefinition = RequestPoliciesDefinition


@dataclass
class AuthorizationDefinition(BaseModel):
    AllowedScope: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedScope=json_data.get("AllowedScope"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationDefinition = AuthorizationDefinition


@dataclass
class BodyValidationDefinition(BaseModel):
    Required: Optional[bool]
    ValidationMode: Optional[str]
    Content: Optional[Sequence["_ContentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BodyValidationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyValidationDefinition"]:
        if not json_data:
            return None
        return cls(
            Required=json_data.get("Required"),
            ValidationMode=json_data.get("ValidationMode"),
            Content=deserialize_list(json_data.get("Content"), ContentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyValidationDefinition = BodyValidationDefinition


@dataclass
class ContentDefinition(BaseModel):
    MediaType: Optional[str]
    ValidationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentDefinition"]:
        if not json_data:
            return None
        return cls(
            MediaType=json_data.get("MediaType"),
            ValidationType=json_data.get("ValidationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentDefinition = ContentDefinition


@dataclass
class CorsDefinition(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    IsAllowCredentialsEnabled: Optional[bool]
    MaxAgeInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposedHeaders=json_data.get("ExposedHeaders"),
            IsAllowCredentialsEnabled=json_data.get("IsAllowCredentialsEnabled"),
            MaxAgeInSeconds=json_data.get("MaxAgeInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsDefinition = CorsDefinition


@dataclass
class HeaderTransformationsDefinition(BaseModel):
    FilterHeaders: Optional[Sequence["_FilterHeadersDefinition"]]
    RenameHeaders: Optional[Sequence["_RenameHeadersDefinition"]]
    SetHeaders: Optional[Sequence["_SetHeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderTransformationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderTransformationsDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterHeaders=deserialize_list(json_data.get("FilterHeaders"), FilterHeadersDefinition),
            RenameHeaders=deserialize_list(json_data.get("RenameHeaders"), RenameHeadersDefinition),
            SetHeaders=deserialize_list(json_data.get("SetHeaders"), SetHeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderTransformationsDefinition = HeaderTransformationsDefinition


@dataclass
class FilterHeadersDefinition(BaseModel):
    Type: Optional[str]
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterHeadersDefinition = FilterHeadersDefinition


@dataclass
class ItemsDefinition(BaseModel):
    IfExists: Optional[str]
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ItemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemsDefinition"]:
        if not json_data:
            return None
        return cls(
            IfExists=json_data.get("IfExists"),
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemsDefinition = ItemsDefinition


@dataclass
class RenameHeadersDefinition(BaseModel):
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RenameHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RenameHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RenameHeadersDefinition = RenameHeadersDefinition


@dataclass
class SetHeadersDefinition(BaseModel):
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SetHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetHeadersDefinition = SetHeadersDefinition


@dataclass
class HeaderValidationsDefinition(BaseModel):
    ValidationMode: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderValidationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderValidationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ValidationMode=json_data.get("ValidationMode"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderValidationsDefinition = HeaderValidationsDefinition


@dataclass
class HeadersDefinition(BaseModel):
    Name: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class QueryParameterTransformationsDefinition(BaseModel):
    FilterQueryParameters: Optional[Sequence["_FilterQueryParametersDefinition"]]
    RenameQueryParameters: Optional[Sequence["_RenameQueryParametersDefinition"]]
    SetQueryParameters: Optional[Sequence["_SetQueryParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameterTransformationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameterTransformationsDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterQueryParameters=deserialize_list(json_data.get("FilterQueryParameters"), FilterQueryParametersDefinition),
            RenameQueryParameters=deserialize_list(json_data.get("RenameQueryParameters"), RenameQueryParametersDefinition),
            SetQueryParameters=deserialize_list(json_data.get("SetQueryParameters"), SetQueryParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParameterTransformationsDefinition = QueryParameterTransformationsDefinition


@dataclass
class FilterQueryParametersDefinition(BaseModel):
    Type: Optional[str]
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterQueryParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterQueryParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterQueryParametersDefinition = FilterQueryParametersDefinition


@dataclass
class RenameQueryParametersDefinition(BaseModel):
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RenameQueryParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RenameQueryParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RenameQueryParametersDefinition = RenameQueryParametersDefinition


@dataclass
class SetQueryParametersDefinition(BaseModel):
    Items: Optional[Sequence["_ItemsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SetQueryParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetQueryParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetQueryParametersDefinition = SetQueryParametersDefinition


@dataclass
class QueryParameterValidationsDefinition(BaseModel):
    ValidationMode: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameterValidationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameterValidationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ValidationMode=json_data.get("ValidationMode"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParameterValidationsDefinition = QueryParameterValidationsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Name: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class ResponseCacheLookupDefinition(BaseModel):
    CacheKeyAdditions: Optional[Sequence[str]]
    IsEnabled: Optional[bool]
    IsPrivateCachingEnabled: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseCacheLookupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseCacheLookupDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheKeyAdditions=json_data.get("CacheKeyAdditions"),
            IsEnabled=json_data.get("IsEnabled"),
            IsPrivateCachingEnabled=json_data.get("IsPrivateCachingEnabled"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseCacheLookupDefinition = ResponseCacheLookupDefinition


@dataclass
class RoutesDefinition(BaseModel):
    Methods: Optional[Sequence[str]]
    Path: Optional[str]
    Backend: Optional[Sequence["_BackendDefinition"]]
    LoggingPolicies: Optional[Sequence["_LoggingPoliciesDefinition"]]
    RequestPolicies: Optional[Sequence["_RequestPoliciesDefinition"]]
    ResponsePolicies: Optional[Sequence["_ResponsePoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Methods=json_data.get("Methods"),
            Path=json_data.get("Path"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
            LoggingPolicies=deserialize_list(json_data.get("LoggingPolicies"), LoggingPoliciesDefinition),
            RequestPolicies=deserialize_list(json_data.get("RequestPolicies"), RequestPoliciesDefinition),
            ResponsePolicies=deserialize_list(json_data.get("ResponsePolicies"), ResponsePoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class BackendDefinition(BaseModel):
    Body: Optional[str]
    ConnectTimeoutInSeconds: Optional[float]
    FunctionId: Optional[str]
    IsSslVerifyDisabled: Optional[bool]
    ReadTimeoutInSeconds: Optional[float]
    SendTimeoutInSeconds: Optional[float]
    Status: Optional[float]
    Type: Optional[str]
    Url: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            ConnectTimeoutInSeconds=json_data.get("ConnectTimeoutInSeconds"),
            FunctionId=json_data.get("FunctionId"),
            IsSslVerifyDisabled=json_data.get("IsSslVerifyDisabled"),
            ReadTimeoutInSeconds=json_data.get("ReadTimeoutInSeconds"),
            SendTimeoutInSeconds=json_data.get("SendTimeoutInSeconds"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefinition = BackendDefinition


@dataclass
class ResponsePoliciesDefinition(BaseModel):
    HeaderTransformations: Optional[Sequence["_HeaderTransformationsDefinition"]]
    ResponseCacheStore: Optional[Sequence["_ResponseCacheStoreDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResponsePoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponsePoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderTransformations=deserialize_list(json_data.get("HeaderTransformations"), HeaderTransformationsDefinition),
            ResponseCacheStore=deserialize_list(json_data.get("ResponseCacheStore"), ResponseCacheStoreDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponsePoliciesDefinition = ResponsePoliciesDefinition


@dataclass
class ResponseCacheStoreDefinition(BaseModel):
    TimeToLiveInSeconds: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseCacheStoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseCacheStoreDefinition"]:
        if not json_data:
            return None
        return cls(
            TimeToLiveInSeconds=json_data.get("TimeToLiveInSeconds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseCacheStoreDefinition = ResponseCacheStoreDefinition


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


