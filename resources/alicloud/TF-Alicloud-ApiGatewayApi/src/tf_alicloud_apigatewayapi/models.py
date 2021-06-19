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
    ApiId: Optional[str]
    AuthType: Optional[str]
    Description: Optional[str]
    GroupId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServiceType: Optional[str]
    StageNames: Optional[Sequence[str]]
    ConstantParameters: Optional[Sequence["_ConstantParametersDefinition"]]
    FcServiceConfig: Optional[Sequence["_FcServiceConfigDefinition"]]
    HttpServiceConfig: Optional[Sequence["_HttpServiceConfigDefinition"]]
    HttpVpcServiceConfig: Optional[Sequence["_HttpVpcServiceConfigDefinition"]]
    MockServiceConfig: Optional[Sequence["_MockServiceConfigDefinition"]]
    RequestConfig: Optional[Sequence["_RequestConfigDefinition"]]
    RequestParameters: Optional[Sequence["_RequestParametersDefinition"]]
    SystemParameters: Optional[Sequence["_SystemParametersDefinition"]]

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
            ApiId=json_data.get("ApiId"),
            AuthType=json_data.get("AuthType"),
            Description=json_data.get("Description"),
            GroupId=json_data.get("GroupId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServiceType=json_data.get("ServiceType"),
            StageNames=json_data.get("StageNames"),
            ConstantParameters=deserialize_list(json_data.get("ConstantParameters"), ConstantParametersDefinition),
            FcServiceConfig=deserialize_list(json_data.get("FcServiceConfig"), FcServiceConfigDefinition),
            HttpServiceConfig=deserialize_list(json_data.get("HttpServiceConfig"), HttpServiceConfigDefinition),
            HttpVpcServiceConfig=deserialize_list(json_data.get("HttpVpcServiceConfig"), HttpVpcServiceConfigDefinition),
            MockServiceConfig=deserialize_list(json_data.get("MockServiceConfig"), MockServiceConfigDefinition),
            RequestConfig=deserialize_list(json_data.get("RequestConfig"), RequestConfigDefinition),
            RequestParameters=deserialize_list(json_data.get("RequestParameters"), RequestParametersDefinition),
            SystemParameters=deserialize_list(json_data.get("SystemParameters"), SystemParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConstantParametersDefinition(BaseModel):
    Description: Optional[str]
    In: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConstantParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstantParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            In=json_data.get("In"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstantParametersDefinition = ConstantParametersDefinition


@dataclass
class FcServiceConfigDefinition(BaseModel):
    ArnRole: Optional[str]
    FunctionName: Optional[str]
    Region: Optional[str]
    ServiceName: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FcServiceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FcServiceConfigDefinition"]:
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
_FcServiceConfigDefinition = FcServiceConfigDefinition


@dataclass
class HttpServiceConfigDefinition(BaseModel):
    Address: Optional[str]
    AoneName: Optional[str]
    Method: Optional[str]
    Path: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpServiceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpServiceConfigDefinition"]:
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
_HttpServiceConfigDefinition = HttpServiceConfigDefinition


@dataclass
class HttpVpcServiceConfigDefinition(BaseModel):
    AoneName: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpVpcServiceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpVpcServiceConfigDefinition"]:
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
_HttpVpcServiceConfigDefinition = HttpVpcServiceConfigDefinition


@dataclass
class MockServiceConfigDefinition(BaseModel):
    AoneName: Optional[str]
    Result: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MockServiceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MockServiceConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AoneName=json_data.get("AoneName"),
            Result=json_data.get("Result"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MockServiceConfigDefinition = MockServiceConfigDefinition


@dataclass
class RequestConfigDefinition(BaseModel):
    BodyFormat: Optional[str]
    Method: Optional[str]
    Mode: Optional[str]
    Path: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestConfigDefinition"]:
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
_RequestConfigDefinition = RequestConfigDefinition


@dataclass
class RequestParametersDefinition(BaseModel):
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
        cls: Type["_RequestParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestParametersDefinition"]:
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
_RequestParametersDefinition = RequestParametersDefinition


@dataclass
class SystemParametersDefinition(BaseModel):
    In: Optional[str]
    Name: Optional[str]
    NameService: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            In=json_data.get("In"),
            Name=json_data.get("Name"),
            NameService=json_data.get("NameService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemParametersDefinition = SystemParametersDefinition


