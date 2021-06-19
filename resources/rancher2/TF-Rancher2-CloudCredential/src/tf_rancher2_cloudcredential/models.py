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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Driver: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Amazonec2CredentialConfig: Optional[Sequence["_Amazonec2CredentialConfigDefinition"]]
    AzureCredentialConfig: Optional[Sequence["_AzureCredentialConfigDefinition"]]
    DigitaloceanCredentialConfig: Optional[Sequence["_DigitaloceanCredentialConfigDefinition"]]
    GoogleCredentialConfig: Optional[Sequence["_GoogleCredentialConfigDefinition"]]
    LinodeCredentialConfig: Optional[Sequence["_LinodeCredentialConfigDefinition"]]
    OpenstackCredentialConfig: Optional[Sequence["_OpenstackCredentialConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VsphereCredentialConfig: Optional[Sequence["_VsphereCredentialConfigDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Driver=json_data.get("Driver"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Amazonec2CredentialConfig=deserialize_list(json_data.get("Amazonec2CredentialConfig"), Amazonec2CredentialConfigDefinition),
            AzureCredentialConfig=deserialize_list(json_data.get("AzureCredentialConfig"), AzureCredentialConfigDefinition),
            DigitaloceanCredentialConfig=deserialize_list(json_data.get("DigitaloceanCredentialConfig"), DigitaloceanCredentialConfigDefinition),
            GoogleCredentialConfig=deserialize_list(json_data.get("GoogleCredentialConfig"), GoogleCredentialConfigDefinition),
            LinodeCredentialConfig=deserialize_list(json_data.get("LinodeCredentialConfig"), LinodeCredentialConfigDefinition),
            OpenstackCredentialConfig=deserialize_list(json_data.get("OpenstackCredentialConfig"), OpenstackCredentialConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VsphereCredentialConfig=deserialize_list(json_data.get("VsphereCredentialConfig"), VsphereCredentialConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class Amazonec2CredentialConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Amazonec2CredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Amazonec2CredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Amazonec2CredentialConfigDefinition = Amazonec2CredentialConfigDefinition


@dataclass
class AzureCredentialConfigDefinition(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    SubscriptionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureCredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureCredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            SubscriptionId=json_data.get("SubscriptionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureCredentialConfigDefinition = AzureCredentialConfigDefinition


@dataclass
class DigitaloceanCredentialConfigDefinition(BaseModel):
    AccessToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DigitaloceanCredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DigitaloceanCredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DigitaloceanCredentialConfigDefinition = DigitaloceanCredentialConfigDefinition


@dataclass
class GoogleCredentialConfigDefinition(BaseModel):
    AuthEncodedJson: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleCredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleCredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthEncodedJson=json_data.get("AuthEncodedJson"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleCredentialConfigDefinition = GoogleCredentialConfigDefinition


@dataclass
class LinodeCredentialConfigDefinition(BaseModel):
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinodeCredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinodeCredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinodeCredentialConfigDefinition = LinodeCredentialConfigDefinition


@dataclass
class OpenstackCredentialConfigDefinition(BaseModel):
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackCredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackCredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackCredentialConfigDefinition = OpenstackCredentialConfigDefinition


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


@dataclass
class VsphereCredentialConfigDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]
    Vcenter: Optional[str]
    VcenterPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereCredentialConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereCredentialConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
            Vcenter=json_data.get("Vcenter"),
            VcenterPort=json_data.get("VcenterPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereCredentialConfigDefinition = VsphereCredentialConfigDefinition


