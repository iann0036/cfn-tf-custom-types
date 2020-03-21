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
    ApiId: Optional[str]
    AuthType: Optional[str]
    Description: Optional[str]
    GroupId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServiceType: Optional[str]
    StageNames: Optional[Sequence[str]]
    ConstantParameters: Optional[Sequence["_ConstantParameters"]]
    FcServiceConfig: Optional[Sequence["_FcServiceConfig"]]
    HttpServiceConfig: Optional[Sequence["_HttpServiceConfig"]]
    HttpVpcServiceConfig: Optional[Sequence["_HttpVpcServiceConfig"]]
    MockServiceConfig: Optional[Sequence["_MockServiceConfig"]]
    RequestConfig: Optional[Sequence["_RequestConfig"]]
    RequestParameters: Optional[Sequence["_RequestParameters"]]
    SystemParameters: Optional[Sequence["_SystemParameters"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiId=json_data.get("ApiId"),
            AuthType=json_data.get("AuthType"),
            Description=json_data.get("Description"),
            GroupId=json_data.get("GroupId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServiceType=json_data.get("ServiceType"),
            StageNames=json_data.get("StageNames"),
            ConstantParameters=json_data.get("ConstantParameters"),
            FcServiceConfig=json_data.get("FcServiceConfig"),
            HttpServiceConfig=json_data.get("HttpServiceConfig"),
            HttpVpcServiceConfig=json_data.get("HttpVpcServiceConfig"),
            MockServiceConfig=json_data.get("MockServiceConfig"),
            RequestConfig=json_data.get("RequestConfig"),
            RequestParameters=json_data.get("RequestParameters"),
            SystemParameters=json_data.get("SystemParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConstantParameters:
    Description: Optional[str]
    In: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConstantParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstantParameters"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            In=json_data.get("In"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstantParameters = ConstantParameters


@dataclass
class FcServiceConfig:
    ArnRole: Optional[str]
    FunctionName: Optional[str]
    Region: Optional[str]
    ServiceName: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FcServiceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FcServiceConfig"]:
        if not json_data:
            return None
        return cls(
            ArnRole=json_data.get("ArnRole"),
            FunctionName=json_data.get("FunctionName"),
            Region=json_data.get("Region"),
            ServiceName=json_data.get("ServiceName"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FcServiceConfig = FcServiceConfig


@dataclass
class HttpServiceConfig:
    Address: Optional[str]
    AoneName: Optional[str]
    Method: Optional[str]
    Path: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpServiceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpServiceConfig"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            AoneName=json_data.get("AoneName"),
            Method=json_data.get("Method"),
            Path=json_data.get("Path"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpServiceConfig = HttpServiceConfig


@dataclass
class HttpVpcServiceConfig:
    AoneName: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpVpcServiceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpVpcServiceConfig"]:
        if not json_data:
            return None
        return cls(
            AoneName=json_data.get("AoneName"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpVpcServiceConfig = HttpVpcServiceConfig


@dataclass
class MockServiceConfig:
    AoneName: Optional[str]
    Result: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MockServiceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MockServiceConfig"]:
        if not json_data:
            return None
        return cls(
            AoneName=json_data.get("AoneName"),
            Result=json_data.get("Result"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MockServiceConfig = MockServiceConfig


@dataclass
class RequestConfig:
    BodyFormat: Optional[str]
    Method: Optional[str]
    Mode: Optional[str]
    Path: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestConfig"]:
        if not json_data:
            return None
        return cls(
            BodyFormat=json_data.get("BodyFormat"),
            Method=json_data.get("Method"),
            Mode=json_data.get("Mode"),
            Path=json_data.get("Path"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestConfig = RequestConfig


@dataclass
class RequestParameters:
    DefaultValue: Optional[str]
    Description: Optional[str]
    In: Optional[str]
    InService: Optional[str]
    Name: Optional[str]
    NameService: Optional[str]
    Required: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestParameters"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            In=json_data.get("In"),
            InService=json_data.get("InService"),
            Name=json_data.get("Name"),
            NameService=json_data.get("NameService"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestParameters = RequestParameters


@dataclass
class SystemParameters:
    In: Optional[str]
    Name: Optional[str]
    NameService: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemParameters"]:
        if not json_data:
            return None
        return cls(
            In=json_data.get("In"),
            Name=json_data.get("Name"),
            NameService=json_data.get("NameService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemParameters = SystemParameters


