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
    AuthType: Optional[str]
    BackendType: Optional[str]
    Cors: Optional[bool]
    Description: Optional[str]
    ExampleFailureResponse: Optional[str]
    ExampleSuccessResponse: Optional[str]
    GroupId: Optional[str]
    GroupName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RequestMethod: Optional[str]
    RequestProtocol: Optional[str]
    RequestUri: Optional[str]
    Tags: Optional[Sequence[str]]
    Version: Optional[str]
    Visibility: Optional[float]
    BackendParameter: Optional[Sequence["_BackendParameter"]]
    FunctionBackend: Optional[Sequence["_FunctionBackend"]]
    HttpBackend: Optional[Sequence["_HttpBackend"]]
    MockBackend: Optional[Sequence["_MockBackend"]]
    RequestParameter: Optional[Sequence["_RequestParameter"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthType=json_data.get("AuthType"),
            BackendType=json_data.get("BackendType"),
            Cors=json_data.get("Cors"),
            Description=json_data.get("Description"),
            ExampleFailureResponse=json_data.get("ExampleFailureResponse"),
            ExampleSuccessResponse=json_data.get("ExampleSuccessResponse"),
            GroupId=json_data.get("GroupId"),
            GroupName=json_data.get("GroupName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RequestMethod=json_data.get("RequestMethod"),
            RequestProtocol=json_data.get("RequestProtocol"),
            RequestUri=json_data.get("RequestUri"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            Visibility=json_data.get("Visibility"),
            BackendParameter=json_data.get("BackendParameter"),
            FunctionBackend=json_data.get("FunctionBackend"),
            HttpBackend=json_data.get("HttpBackend"),
            MockBackend=json_data.get("MockBackend"),
            RequestParameter=json_data.get("RequestParameter"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendParameter:
    Description: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendParameter"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendParameter = BackendParameter


@dataclass
class FunctionBackend:
    FunctionUrn: Optional[str]
    InvocationType: Optional[str]
    Timeout: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionBackend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionBackend"]:
        if not json_data:
            return None
        return cls(
            FunctionUrn=json_data.get("FunctionUrn"),
            InvocationType=json_data.get("InvocationType"),
            Timeout=json_data.get("Timeout"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionBackend = FunctionBackend


@dataclass
class HttpBackend:
    Method: Optional[str]
    Protocol: Optional[str]
    Timeout: Optional[float]
    Uri: Optional[str]
    UrlDomain: Optional[str]
    VpcChannel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpBackend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpBackend"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Protocol=json_data.get("Protocol"),
            Timeout=json_data.get("Timeout"),
            Uri=json_data.get("Uri"),
            UrlDomain=json_data.get("UrlDomain"),
            VpcChannel=json_data.get("VpcChannel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpBackend = HttpBackend


@dataclass
class MockBackend:
    Description: Optional[str]
    ResultContent: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MockBackend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MockBackend"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            ResultContent=json_data.get("ResultContent"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MockBackend = MockBackend


@dataclass
class RequestParameter:
    Default: Optional[str]
    Description: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Required: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestParameter"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Description=json_data.get("Description"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestParameter = RequestParameter


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


