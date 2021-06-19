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
    CreatedBy: Optional[str]
    CreatedTs: Optional[float]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IntegrationId: Optional[str]
    IntegrationType: Optional[str]
    LastModifiedBy: Optional[str]
    LastModifiedTs: Optional[float]
    Name: Optional[str]
    Reason: Optional[Sequence["_ReasonDefinition2"]]
    Status: Optional[str]
    Valid: Optional[bool]
    IntegrationConfig: Optional[Sequence["_IntegrationConfigDefinition"]]

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
            CreatedBy=json_data.get("CreatedBy"),
            CreatedTs=json_data.get("CreatedTs"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IntegrationId=json_data.get("IntegrationId"),
            IntegrationType=json_data.get("IntegrationType"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            LastModifiedTs=json_data.get("LastModifiedTs"),
            Name=json_data.get("Name"),
            Reason=deserialize_list(json_data.get("Reason"), ReasonDefinition2),
            Status=json_data.get("Status"),
            Valid=json_data.get("Valid"),
            IntegrationConfig=deserialize_list(json_data.get("IntegrationConfig"), IntegrationConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReasonDefinition2(BaseModel):
    Details: Optional[Sequence["_ReasonDefinition"]]
    ErrorType: Optional[str]
    LastUpdated: Optional[float]
    Message: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReasonDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReasonDefinition2"]:
        if not json_data:
            return None
        return cls(
            Details=deserialize_list(json_data.get("Details"), ReasonDefinition),
            ErrorType=json_data.get("ErrorType"),
            LastUpdated=json_data.get("LastUpdated"),
            Message=json_data.get("Message"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReasonDefinition2 = ReasonDefinition2


@dataclass
class ReasonDefinition(BaseModel):
    Message: Optional[str]
    StatusCode: Optional[float]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReasonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReasonDefinition"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            StatusCode=json_data.get("StatusCode"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReasonDefinition = ReasonDefinition


@dataclass
class IntegrationConfigDefinition(BaseModel):
    AuthToken: Optional[str]
    BaseUrl: Optional[str]
    HostUrl: Optional[str]
    IntegrationKey: Optional[str]
    Login: Optional[str]
    Password: Optional[str]
    QueueUrl: Optional[str]
    Tables: Optional[Sequence["_TablesDefinition"]]
    Url: Optional[str]
    Version: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthToken=json_data.get("AuthToken"),
            BaseUrl=json_data.get("BaseUrl"),
            HostUrl=json_data.get("HostUrl"),
            IntegrationKey=json_data.get("IntegrationKey"),
            Login=json_data.get("Login"),
            Password=json_data.get("Password"),
            QueueUrl=json_data.get("QueueUrl"),
            Tables=deserialize_list(json_data.get("Tables"), TablesDefinition),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationConfigDefinition = IntegrationConfigDefinition


@dataclass
class TablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TablesDefinition = TablesDefinition


@dataclass
class HeadersDefinition(BaseModel):
    Key: Optional[str]
    ReadOnly: Optional[bool]
    Secure: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            ReadOnly=json_data.get("ReadOnly"),
            Secure=json_data.get("Secure"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


