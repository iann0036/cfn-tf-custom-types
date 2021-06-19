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
    ApiDesc: Optional[str]
    ApiName: Optional[str]
    AuthType: Optional[str]
    CreateTime: Optional[str]
    EnableCors: Optional[bool]
    Id: Optional[str]
    PreLimit: Optional[float]
    Protocol: Optional[str]
    ReleaseLimit: Optional[float]
    RequestConfigMethod: Optional[str]
    RequestConfigPath: Optional[str]
    ResponseFailExample: Optional[str]
    ResponseSuccessExample: Optional[str]
    ResponseType: Optional[str]
    ServiceConfigMethod: Optional[str]
    ServiceConfigMockReturnMessage: Optional[str]
    ServiceConfigPath: Optional[str]
    ServiceConfigProduct: Optional[str]
    ServiceConfigScfFunctionName: Optional[str]
    ServiceConfigScfFunctionNamespace: Optional[str]
    ServiceConfigScfFunctionQualifier: Optional[str]
    ServiceConfigTimeout: Optional[float]
    ServiceConfigType: Optional[str]
    ServiceConfigUrl: Optional[str]
    ServiceConfigVpcId: Optional[str]
    ServiceId: Optional[str]
    TestLimit: Optional[float]
    UpdateTime: Optional[str]
    RequestParameters: Optional[Sequence["_RequestParametersDefinition"]]
    ResponseErrorCodes: Optional[Sequence["_ResponseErrorCodesDefinition"]]

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
            ApiDesc=json_data.get("ApiDesc"),
            ApiName=json_data.get("ApiName"),
            AuthType=json_data.get("AuthType"),
            CreateTime=json_data.get("CreateTime"),
            EnableCors=json_data.get("EnableCors"),
            Id=json_data.get("Id"),
            PreLimit=json_data.get("PreLimit"),
            Protocol=json_data.get("Protocol"),
            ReleaseLimit=json_data.get("ReleaseLimit"),
            RequestConfigMethod=json_data.get("RequestConfigMethod"),
            RequestConfigPath=json_data.get("RequestConfigPath"),
            ResponseFailExample=json_data.get("ResponseFailExample"),
            ResponseSuccessExample=json_data.get("ResponseSuccessExample"),
            ResponseType=json_data.get("ResponseType"),
            ServiceConfigMethod=json_data.get("ServiceConfigMethod"),
            ServiceConfigMockReturnMessage=json_data.get("ServiceConfigMockReturnMessage"),
            ServiceConfigPath=json_data.get("ServiceConfigPath"),
            ServiceConfigProduct=json_data.get("ServiceConfigProduct"),
            ServiceConfigScfFunctionName=json_data.get("ServiceConfigScfFunctionName"),
            ServiceConfigScfFunctionNamespace=json_data.get("ServiceConfigScfFunctionNamespace"),
            ServiceConfigScfFunctionQualifier=json_data.get("ServiceConfigScfFunctionQualifier"),
            ServiceConfigTimeout=json_data.get("ServiceConfigTimeout"),
            ServiceConfigType=json_data.get("ServiceConfigType"),
            ServiceConfigUrl=json_data.get("ServiceConfigUrl"),
            ServiceConfigVpcId=json_data.get("ServiceConfigVpcId"),
            ServiceId=json_data.get("ServiceId"),
            TestLimit=json_data.get("TestLimit"),
            UpdateTime=json_data.get("UpdateTime"),
            RequestParameters=deserialize_list(json_data.get("RequestParameters"), RequestParametersDefinition),
            ResponseErrorCodes=deserialize_list(json_data.get("ResponseErrorCodes"), ResponseErrorCodesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestParametersDefinition(BaseModel):
    DefaultValue: Optional[str]
    Desc: Optional[str]
    Name: Optional[str]
    Position: Optional[str]
    Required: Optional[bool]
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
            Desc=json_data.get("Desc"),
            Name=json_data.get("Name"),
            Position=json_data.get("Position"),
            Required=json_data.get("Required"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestParametersDefinition = RequestParametersDefinition


@dataclass
class ResponseErrorCodesDefinition(BaseModel):
    Code: Optional[float]
    ConvertedCode: Optional[float]
    Desc: Optional[str]
    Msg: Optional[str]
    NeedConvert: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseErrorCodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseErrorCodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            ConvertedCode=json_data.get("ConvertedCode"),
            Desc=json_data.get("Desc"),
            Msg=json_data.get("Msg"),
            NeedConvert=json_data.get("NeedConvert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseErrorCodesDefinition = ResponseErrorCodesDefinition


