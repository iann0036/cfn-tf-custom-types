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
    DefaultContentKeyPolicyName: Optional[str]
    Id: Optional[str]
    MediaServicesAccountName: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    CommonEncryptionCbcs: Optional[Sequence["_CommonEncryptionCbcsDefinition"]]
    CommonEncryptionCenc: Optional[Sequence["_CommonEncryptionCencDefinition"]]
    NoEncryptionEnabledProtocols: Optional[Sequence["_NoEncryptionEnabledProtocolsDefinition"]]
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
            DefaultContentKeyPolicyName=json_data.get("DefaultContentKeyPolicyName"),
            Id=json_data.get("Id"),
            MediaServicesAccountName=json_data.get("MediaServicesAccountName"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            CommonEncryptionCbcs=deserialize_list(json_data.get("CommonEncryptionCbcs"), CommonEncryptionCbcsDefinition),
            CommonEncryptionCenc=deserialize_list(json_data.get("CommonEncryptionCenc"), CommonEncryptionCencDefinition),
            NoEncryptionEnabledProtocols=deserialize_list(json_data.get("NoEncryptionEnabledProtocols"), NoEncryptionEnabledProtocolsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CommonEncryptionCbcsDefinition(BaseModel):
    DefaultContentKey: Optional[Sequence["_DefaultContentKeyDefinition"]]
    DrmFairplay: Optional[Sequence["_DrmFairplayDefinition"]]
    EnabledProtocols: Optional[Sequence["_EnabledProtocolsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CommonEncryptionCbcsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommonEncryptionCbcsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultContentKey=deserialize_list(json_data.get("DefaultContentKey"), DefaultContentKeyDefinition),
            DrmFairplay=deserialize_list(json_data.get("DrmFairplay"), DrmFairplayDefinition),
            EnabledProtocols=deserialize_list(json_data.get("EnabledProtocols"), EnabledProtocolsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommonEncryptionCbcsDefinition = CommonEncryptionCbcsDefinition


@dataclass
class DefaultContentKeyDefinition(BaseModel):
    Label: Optional[str]
    PolicyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultContentKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultContentKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            PolicyName=json_data.get("PolicyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultContentKeyDefinition = DefaultContentKeyDefinition


@dataclass
class DrmFairplayDefinition(BaseModel):
    AllowPersistentLicense: Optional[bool]
    CustomLicenseAcquisitionUrlTemplate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DrmFairplayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrmFairplayDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowPersistentLicense=json_data.get("AllowPersistentLicense"),
            CustomLicenseAcquisitionUrlTemplate=json_data.get("CustomLicenseAcquisitionUrlTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrmFairplayDefinition = DrmFairplayDefinition


@dataclass
class EnabledProtocolsDefinition(BaseModel):
    Dash: Optional[bool]
    Download: Optional[bool]
    Hls: Optional[bool]
    SmoothStreaming: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnabledProtocolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnabledProtocolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Dash=json_data.get("Dash"),
            Download=json_data.get("Download"),
            Hls=json_data.get("Hls"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnabledProtocolsDefinition = EnabledProtocolsDefinition


@dataclass
class CommonEncryptionCencDefinition(BaseModel):
    DrmWidevineCustomLicenseAcquisitionUrlTemplate: Optional[str]
    DefaultContentKey: Optional[Sequence["_DefaultContentKeyDefinition"]]
    DrmPlayready: Optional[Sequence["_DrmPlayreadyDefinition"]]
    EnabledProtocols: Optional[Sequence["_EnabledProtocolsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CommonEncryptionCencDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommonEncryptionCencDefinition"]:
        if not json_data:
            return None
        return cls(
            DrmWidevineCustomLicenseAcquisitionUrlTemplate=json_data.get("DrmWidevineCustomLicenseAcquisitionUrlTemplate"),
            DefaultContentKey=deserialize_list(json_data.get("DefaultContentKey"), DefaultContentKeyDefinition),
            DrmPlayready=deserialize_list(json_data.get("DrmPlayready"), DrmPlayreadyDefinition),
            EnabledProtocols=deserialize_list(json_data.get("EnabledProtocols"), EnabledProtocolsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommonEncryptionCencDefinition = CommonEncryptionCencDefinition


@dataclass
class DrmPlayreadyDefinition(BaseModel):
    CustomAttributes: Optional[str]
    CustomLicenseAcquisitionUrlTemplate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DrmPlayreadyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrmPlayreadyDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomAttributes=json_data.get("CustomAttributes"),
            CustomLicenseAcquisitionUrlTemplate=json_data.get("CustomLicenseAcquisitionUrlTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrmPlayreadyDefinition = DrmPlayreadyDefinition


@dataclass
class NoEncryptionEnabledProtocolsDefinition(BaseModel):
    Dash: Optional[bool]
    Download: Optional[bool]
    Hls: Optional[bool]
    SmoothStreaming: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NoEncryptionEnabledProtocolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoEncryptionEnabledProtocolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Dash=json_data.get("Dash"),
            Download=json_data.get("Download"),
            Hls=json_data.get("Hls"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoEncryptionEnabledProtocolsDefinition = NoEncryptionEnabledProtocolsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


