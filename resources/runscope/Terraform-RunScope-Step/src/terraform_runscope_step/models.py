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
    BeforeScripts: Optional[Sequence[str]]
    Body: Optional[str]
    BucketId: Optional[str]
    Id: Optional[str]
    Method: Optional[str]
    Note: Optional[str]
    Scripts: Optional[Sequence[str]]
    StepType: Optional[str]
    TestId: Optional[str]
    Url: Optional[str]
    Assertions: Optional[Sequence["_Assertions"]]
    Auth: Optional[Sequence["_Auth"]]
    Headers: Optional[Sequence["_Headers"]]
    Variables: Optional[Sequence["_Variables"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BeforeScripts=json_data.get("BeforeScripts"),
            Body=json_data.get("Body"),
            BucketId=json_data.get("BucketId"),
            Id=json_data.get("Id"),
            Method=json_data.get("Method"),
            Note=json_data.get("Note"),
            Scripts=json_data.get("Scripts"),
            StepType=json_data.get("StepType"),
            TestId=json_data.get("TestId"),
            Url=json_data.get("Url"),
            Assertions=json_data.get("Assertions"),
            Auth=json_data.get("Auth"),
            Headers=json_data.get("Headers"),
            Variables=json_data.get("Variables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Assertions:
    Comparison: Optional[str]
    Property: Optional[str]
    Source: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Assertions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Assertions"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Property=json_data.get("Property"),
            Source=json_data.get("Source"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Assertions = Assertions


@dataclass
class Auth:
    AuthType: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Auth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Auth"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Auth = Auth


@dataclass
class Headers:
    Header: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class Variables:
    Name: Optional[str]
    Property: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Variables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Variables"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Property=json_data.get("Property"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Variables = Variables


