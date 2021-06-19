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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExtendedLog: Optional[str]
    External: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    AddressList: Optional[Sequence["_AddressListDefinition"]]
    Constraint: Optional[Sequence["_ConstraintDefinition"]]
    Method: Optional[Sequence["_MethodDefinition"]]
    Signature: Optional[Sequence["_SignatureDefinition"]]
    UrlAccess: Optional[Sequence["_UrlAccessDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExtendedLog=json_data.get("ExtendedLog"),
            External=json_data.get("External"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            AddressList=deserialize_list(json_data.get("AddressList"), AddressListDefinition),
            Constraint=deserialize_list(json_data.get("Constraint"), ConstraintDefinition),
            Method=deserialize_list(json_data.get("Method"), MethodDefinition),
            Signature=deserialize_list(json_data.get("Signature"), SignatureDefinition),
            UrlAccess=deserialize_list(json_data.get("UrlAccess"), UrlAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressListDefinition(BaseModel):
    BlockedLog: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]
    BlockedAddress: Optional[Sequence["_BlockedAddressDefinition"]]
    TrustedAddress: Optional[Sequence["_TrustedAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockedLog=json_data.get("BlockedLog"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
            BlockedAddress=deserialize_list(json_data.get("BlockedAddress"), BlockedAddressDefinition),
            TrustedAddress=deserialize_list(json_data.get("TrustedAddress"), TrustedAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressListDefinition = AddressListDefinition


@dataclass
class BlockedAddressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockedAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockedAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockedAddressDefinition = BlockedAddressDefinition


@dataclass
class TrustedAddressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedAddressDefinition = TrustedAddressDefinition


@dataclass
class ConstraintDefinition(BaseModel):
    ContentLength: Optional[Sequence["_ContentLengthDefinition"]]
    Exception: Optional[Sequence["_ExceptionDefinition"]]
    HeaderLength: Optional[Sequence["_HeaderLengthDefinition"]]
    Hostname: Optional[Sequence["_HostnameDefinition"]]
    LineLength: Optional[Sequence["_LineLengthDefinition"]]
    Malformed: Optional[Sequence["_MalformedDefinition"]]
    MaxCookie: Optional[Sequence["_MaxCookieDefinition"]]
    MaxHeaderLine: Optional[Sequence["_MaxHeaderLineDefinition"]]
    MaxRangeSegment: Optional[Sequence["_MaxRangeSegmentDefinition"]]
    MaxUrlParam: Optional[Sequence["_MaxUrlParamDefinition"]]
    Method: Optional[Sequence["_MethodDefinition"]]
    ParamLength: Optional[Sequence["_ParamLengthDefinition"]]
    UrlParamLength: Optional[Sequence["_UrlParamLengthDefinition"]]
    Version: Optional[Sequence["_VersionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentLength=deserialize_list(json_data.get("ContentLength"), ContentLengthDefinition),
            Exception=deserialize_list(json_data.get("Exception"), ExceptionDefinition),
            HeaderLength=deserialize_list(json_data.get("HeaderLength"), HeaderLengthDefinition),
            Hostname=deserialize_list(json_data.get("Hostname"), HostnameDefinition),
            LineLength=deserialize_list(json_data.get("LineLength"), LineLengthDefinition),
            Malformed=deserialize_list(json_data.get("Malformed"), MalformedDefinition),
            MaxCookie=deserialize_list(json_data.get("MaxCookie"), MaxCookieDefinition),
            MaxHeaderLine=deserialize_list(json_data.get("MaxHeaderLine"), MaxHeaderLineDefinition),
            MaxRangeSegment=deserialize_list(json_data.get("MaxRangeSegment"), MaxRangeSegmentDefinition),
            MaxUrlParam=deserialize_list(json_data.get("MaxUrlParam"), MaxUrlParamDefinition),
            Method=deserialize_list(json_data.get("Method"), MethodDefinition),
            ParamLength=deserialize_list(json_data.get("ParamLength"), ParamLengthDefinition),
            UrlParamLength=deserialize_list(json_data.get("UrlParamLength"), UrlParamLengthDefinition),
            Version=deserialize_list(json_data.get("Version"), VersionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintDefinition = ConstraintDefinition


@dataclass
class ContentLengthDefinition(BaseModel):
    Action: Optional[str]
    Length: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentLengthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentLengthDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Length=json_data.get("Length"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentLengthDefinition = ContentLengthDefinition


@dataclass
class ExceptionDefinition(BaseModel):
    Address: Optional[str]
    ContentLength: Optional[str]
    HeaderLength: Optional[str]
    Hostname: Optional[str]
    Id: Optional[float]
    LineLength: Optional[str]
    Malformed: Optional[str]
    MaxCookie: Optional[str]
    MaxHeaderLine: Optional[str]
    MaxRangeSegment: Optional[str]
    MaxUrlParam: Optional[str]
    Method: Optional[str]
    ParamLength: Optional[str]
    Pattern: Optional[str]
    Regex: Optional[str]
    UrlParamLength: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExceptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExceptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            ContentLength=json_data.get("ContentLength"),
            HeaderLength=json_data.get("HeaderLength"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            LineLength=json_data.get("LineLength"),
            Malformed=json_data.get("Malformed"),
            MaxCookie=json_data.get("MaxCookie"),
            MaxHeaderLine=json_data.get("MaxHeaderLine"),
            MaxRangeSegment=json_data.get("MaxRangeSegment"),
            MaxUrlParam=json_data.get("MaxUrlParam"),
            Method=json_data.get("Method"),
            ParamLength=json_data.get("ParamLength"),
            Pattern=json_data.get("Pattern"),
            Regex=json_data.get("Regex"),
            UrlParamLength=json_data.get("UrlParamLength"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExceptionDefinition = ExceptionDefinition


@dataclass
class HeaderLengthDefinition(BaseModel):
    Action: Optional[str]
    Length: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderLengthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderLengthDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Length=json_data.get("Length"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderLengthDefinition = HeaderLengthDefinition


@dataclass
class HostnameDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostnameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostnameDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostnameDefinition = HostnameDefinition


@dataclass
class LineLengthDefinition(BaseModel):
    Action: Optional[str]
    Length: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LineLengthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineLengthDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Length=json_data.get("Length"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineLengthDefinition = LineLengthDefinition


@dataclass
class MalformedDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MalformedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MalformedDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MalformedDefinition = MalformedDefinition


@dataclass
class MaxCookieDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    MaxCookie: Optional[float]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxCookieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxCookieDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            MaxCookie=json_data.get("MaxCookie"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxCookieDefinition = MaxCookieDefinition


@dataclass
class MaxHeaderLineDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    MaxHeaderLine: Optional[float]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxHeaderLineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxHeaderLineDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            MaxHeaderLine=json_data.get("MaxHeaderLine"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxHeaderLineDefinition = MaxHeaderLineDefinition


@dataclass
class MaxRangeSegmentDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    MaxRangeSegment: Optional[float]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxRangeSegmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxRangeSegmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            MaxRangeSegment=json_data.get("MaxRangeSegment"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxRangeSegmentDefinition = MaxRangeSegmentDefinition


@dataclass
class MaxUrlParamDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    MaxUrlParam: Optional[float]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxUrlParamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxUrlParamDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            MaxUrlParam=json_data.get("MaxUrlParam"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxUrlParamDefinition = MaxUrlParamDefinition


@dataclass
class MethodDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodDefinition = MethodDefinition


@dataclass
class ParamLengthDefinition(BaseModel):
    Action: Optional[str]
    Length: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamLengthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamLengthDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Length=json_data.get("Length"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamLengthDefinition = ParamLengthDefinition


@dataclass
class UrlParamLengthDefinition(BaseModel):
    Action: Optional[str]
    Length: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlParamLengthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlParamLengthDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Length=json_data.get("Length"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlParamLengthDefinition = UrlParamLengthDefinition


@dataclass
class VersionDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionDefinition = VersionDefinition


@dataclass
class SignatureDefinition(BaseModel):
    CreditCardDetectionThreshold: Optional[float]
    CustomSignature: Optional[Sequence["_CustomSignatureDefinition"]]
    DisabledSignature: Optional[Sequence["_DisabledSignatureDefinition"]]
    DisabledSubClass: Optional[Sequence["_DisabledSubClassDefinition"]]
    MainClass: Optional[Sequence["_MainClassDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SignatureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignatureDefinition"]:
        if not json_data:
            return None
        return cls(
            CreditCardDetectionThreshold=json_data.get("CreditCardDetectionThreshold"),
            CustomSignature=deserialize_list(json_data.get("CustomSignature"), CustomSignatureDefinition),
            DisabledSignature=deserialize_list(json_data.get("DisabledSignature"), DisabledSignatureDefinition),
            DisabledSubClass=deserialize_list(json_data.get("DisabledSubClass"), DisabledSubClassDefinition),
            MainClass=deserialize_list(json_data.get("MainClass"), MainClassDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignatureDefinition = SignatureDefinition


@dataclass
class CustomSignatureDefinition(BaseModel):
    Action: Optional[str]
    CaseSensitivity: Optional[str]
    Direction: Optional[str]
    Log: Optional[str]
    Name: Optional[str]
    Pattern: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSignatureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSignatureDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CaseSensitivity=json_data.get("CaseSensitivity"),
            Direction=json_data.get("Direction"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Pattern=json_data.get("Pattern"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSignatureDefinition = CustomSignatureDefinition


@dataclass
class DisabledSignatureDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DisabledSignatureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisabledSignatureDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisabledSignatureDefinition = DisabledSignatureDefinition


@dataclass
class DisabledSubClassDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DisabledSubClassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisabledSubClassDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisabledSubClassDefinition = DisabledSubClassDefinition


@dataclass
class MainClassDefinition(BaseModel):
    Action: Optional[str]
    Id: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MainClassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MainClassDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MainClassDefinition = MainClassDefinition


@dataclass
class UrlAccessDefinition(BaseModel):
    Action: Optional[str]
    Address: Optional[str]
    Id: Optional[float]
    Log: Optional[str]
    Severity: Optional[str]
    AccessPattern: Optional[Sequence["_AccessPatternDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UrlAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Address=json_data.get("Address"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
            Severity=json_data.get("Severity"),
            AccessPattern=deserialize_list(json_data.get("AccessPattern"), AccessPatternDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlAccessDefinition = UrlAccessDefinition


@dataclass
class AccessPatternDefinition(BaseModel):
    Id: Optional[float]
    Negate: Optional[str]
    Pattern: Optional[str]
    Regex: Optional[str]
    Srcaddr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPatternDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPatternDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Negate=json_data.get("Negate"),
            Pattern=json_data.get("Pattern"),
            Regex=json_data.get("Regex"),
            Srcaddr=json_data.get("Srcaddr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPatternDefinition = AccessPatternDefinition


