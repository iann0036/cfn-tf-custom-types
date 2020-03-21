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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    Endpoint: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    GatewayId: Optional[str]
    LifecycleDetails: Optional[str]
    PathPrefix: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Specification: Optional[Sequence["_Specification"]]
    Timeouts: Optional["_Timeouts"]
    LoggingPolicies: Optional[Sequence["_LoggingPolicies"]]
    RequestPolicies: Optional[Sequence["_RequestPolicies"]]
    Routes: Optional[Sequence["_Routes"]]
    AccessLog: Optional[Sequence["_AccessLog"]]
    ExecutionLog: Optional[Sequence["_ExecutionLog"]]
    Authentication: Optional[Sequence["_Authentication"]]
    Cors: Optional[Sequence["_Cors"]]
    RateLimiting: Optional[Sequence["_RateLimiting"]]
    Backend: Optional[Sequence["_Backend"]]
    Headers: Optional[Sequence["_Headers"]]
    Authorization: Optional[Sequence["_Authorization"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            Endpoint=json_data.get("Endpoint"),
            FreeformTags=json_data.get("FreeformTags"),
            GatewayId=json_data.get("GatewayId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            PathPrefix=json_data.get("PathPrefix"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Specification=json_data.get("Specification"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            LoggingPolicies=json_data.get("LoggingPolicies"),
            RequestPolicies=json_data.get("RequestPolicies"),
            Routes=json_data.get("Routes"),
            AccessLog=json_data.get("AccessLog"),
            ExecutionLog=json_data.get("ExecutionLog"),
            Authentication=json_data.get("Authentication"),
            Cors=json_data.get("Cors"),
            RateLimiting=json_data.get("RateLimiting"),
            Backend=json_data.get("Backend"),
            Headers=json_data.get("Headers"),
            Authorization=json_data.get("Authorization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Specification:
    LoggingPolicies: Optional[Sequence["_LoggingPolicies"]]
    RequestPolicies: Optional[Sequence["_RequestPolicies"]]
    Routes: Optional[Sequence["_Routes"]]

    @classmethod
    def _deserialize(
        cls: Type["_Specification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Specification"]:
        if not json_data:
            return None
        return cls(
            LoggingPolicies=json_data.get("LoggingPolicies"),
            RequestPolicies=json_data.get("RequestPolicies"),
            Routes=json_data.get("Routes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Specification = Specification


@dataclass
class LoggingPolicies:
    AccessLog: Optional[Sequence["_AccessLog"]]
    ExecutionLog: Optional[Sequence["_ExecutionLog"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingPolicies"]:
        if not json_data:
            return None
        return cls(
            AccessLog=json_data.get("AccessLog"),
            ExecutionLog=json_data.get("ExecutionLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingPolicies = LoggingPolicies


@dataclass
class AccessLog:
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLog"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLog = AccessLog


@dataclass
class ExecutionLog:
    IsEnabled: Optional[bool]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionLog"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionLog = ExecutionLog


@dataclass
class RequestPolicies:
    Authorization: Optional[Sequence["_Authorization"]]
    Cors: Optional[Sequence["_Cors"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestPolicies"]:
        if not json_data:
            return None
        return cls(
            Authorization=json_data.get("Authorization"),
            Cors=json_data.get("Cors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestPolicies = RequestPolicies


@dataclass
class Authorization:
    AllowedScope: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Authorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Authorization"]:
        if not json_data:
            return None
        return cls(
            AllowedScope=json_data.get("AllowedScope"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Authorization = Authorization


@dataclass
class Cors:
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    IsAllowCredentialsEnabled: Optional[bool]
    MaxAgeInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Cors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cors"]:
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
_Cors = Cors


@dataclass
class Routes:
    Methods: Optional[Sequence[str]]
    Path: Optional[str]
    Backend: Optional[Sequence["_Backend"]]
    LoggingPolicies: Optional[Sequence["_LoggingPolicies"]]
    RequestPolicies: Optional[Sequence["_RequestPolicies"]]

    @classmethod
    def _deserialize(
        cls: Type["_Routes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Routes"]:
        if not json_data:
            return None
        return cls(
            Methods=json_data.get("Methods"),
            Path=json_data.get("Path"),
            Backend=json_data.get("Backend"),
            LoggingPolicies=json_data.get("LoggingPolicies"),
            RequestPolicies=json_data.get("RequestPolicies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Routes = Routes


@dataclass
class Backend:
    Body: Optional[str]
    ConnectTimeoutInSeconds: Optional[float]
    FunctionId: Optional[str]
    IsSslVerifyDisabled: Optional[bool]
    ReadTimeoutInSeconds: Optional[float]
    SendTimeoutInSeconds: Optional[float]
    Status: Optional[float]
    Type: Optional[str]
    Url: Optional[str]
    Headers: Optional[Sequence["_Headers"]]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
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
            Headers=json_data.get("Headers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


@dataclass
class Headers:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class Authentication:
    FunctionId: Optional[str]
    IsAnonymousAccessAllowed: Optional[bool]
    TokenHeader: Optional[str]
    TokenQueryParam: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Authentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Authentication"]:
        if not json_data:
            return None
        return cls(
            FunctionId=json_data.get("FunctionId"),
            IsAnonymousAccessAllowed=json_data.get("IsAnonymousAccessAllowed"),
            TokenHeader=json_data.get("TokenHeader"),
            TokenQueryParam=json_data.get("TokenQueryParam"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Authentication = Authentication


@dataclass
class RateLimiting:
    RateInRequestsPerSecond: Optional[float]
    RateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimiting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimiting"]:
        if not json_data:
            return None
        return cls(
            RateInRequestsPerSecond=json_data.get("RateInRequestsPerSecond"),
            RateKey=json_data.get("RateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimiting = RateLimiting


