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
    DeleteServiceOnDestroy: Optional[bool]
    EnvVariables: Optional[Sequence["_EnvVariables"]]
    Id: Optional[str]
    InstanceClass: Optional[str]
    Name: Optional[str]
    NoopOnDestroy: Optional[bool]
    Project: Optional[str]
    Runtime: Optional[str]
    RuntimeApiVersion: Optional[str]
    Service: Optional[str]
    Threadsafe: Optional[bool]
    VersionId: Optional[str]
    Deployment: Optional[Sequence["_Deployment"]]
    Entrypoint: Optional[Sequence["_Entrypoint"]]
    Handlers: Optional[Sequence["_Handlers"]]
    Libraries: Optional[Sequence["_Libraries"]]
    Timeouts: Optional["_Timeouts"]
    Files: Optional[Sequence["_Files"]]
    Zip: Optional[Sequence["_Zip"]]
    Script: Optional[Sequence["_Script"]]
    StaticFiles: Optional[Sequence["_StaticFiles"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeleteServiceOnDestroy=json_data.get("DeleteServiceOnDestroy"),
            EnvVariables=json_data.get("EnvVariables"),
            Id=json_data.get("Id"),
            InstanceClass=json_data.get("InstanceClass"),
            Name=json_data.get("Name"),
            NoopOnDestroy=json_data.get("NoopOnDestroy"),
            Project=json_data.get("Project"),
            Runtime=json_data.get("Runtime"),
            RuntimeApiVersion=json_data.get("RuntimeApiVersion"),
            Service=json_data.get("Service"),
            Threadsafe=json_data.get("Threadsafe"),
            VersionId=json_data.get("VersionId"),
            Deployment=json_data.get("Deployment"),
            Entrypoint=json_data.get("Entrypoint"),
            Handlers=json_data.get("Handlers"),
            Libraries=json_data.get("Libraries"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Files=json_data.get("Files"),
            Zip=json_data.get("Zip"),
            Script=json_data.get("Script"),
            StaticFiles=json_data.get("StaticFiles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvVariables:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvVariables"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvVariables = EnvVariables


@dataclass
class Deployment:
    Files: Optional[Sequence["_Files"]]
    Zip: Optional[Sequence["_Zip"]]

    @classmethod
    def _deserialize(
        cls: Type["_Deployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deployment"]:
        if not json_data:
            return None
        return cls(
            Files=json_data.get("Files"),
            Zip=json_data.get("Zip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deployment = Deployment


@dataclass
class Files:
    Name: Optional[str]
    Sha1Sum: Optional[str]
    SourceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Files"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Files"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Sha1Sum=json_data.get("Sha1Sum"),
            SourceUrl=json_data.get("SourceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Files = Files


@dataclass
class Zip:
    FilesCount: Optional[float]
    SourceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Zip"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Zip"]:
        if not json_data:
            return None
        return cls(
            FilesCount=json_data.get("FilesCount"),
            SourceUrl=json_data.get("SourceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Zip = Zip


@dataclass
class Entrypoint:
    Shell: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Entrypoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Entrypoint"]:
        if not json_data:
            return None
        return cls(
            Shell=json_data.get("Shell"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Entrypoint = Entrypoint


@dataclass
class Handlers:
    AuthFailAction: Optional[str]
    Login: Optional[str]
    RedirectHttpResponseCode: Optional[str]
    SecurityLevel: Optional[str]
    UrlRegex: Optional[str]
    Script: Optional[Sequence["_Script"]]
    StaticFiles: Optional[Sequence["_StaticFiles"]]

    @classmethod
    def _deserialize(
        cls: Type["_Handlers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Handlers"]:
        if not json_data:
            return None
        return cls(
            AuthFailAction=json_data.get("AuthFailAction"),
            Login=json_data.get("Login"),
            RedirectHttpResponseCode=json_data.get("RedirectHttpResponseCode"),
            SecurityLevel=json_data.get("SecurityLevel"),
            UrlRegex=json_data.get("UrlRegex"),
            Script=json_data.get("Script"),
            StaticFiles=json_data.get("StaticFiles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Handlers = Handlers


@dataclass
class Script:
    ScriptPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Script"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Script"]:
        if not json_data:
            return None
        return cls(
            ScriptPath=json_data.get("ScriptPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Script = Script


@dataclass
class StaticFiles:
    ApplicationReadable: Optional[bool]
    Expiration: Optional[str]
    HttpHeaders: Optional[Sequence["_HttpHeaders"]]
    MimeType: Optional[str]
    Path: Optional[str]
    RequireMatchingFile: Optional[bool]
    UploadPathRegex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticFiles"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticFiles"]:
        if not json_data:
            return None
        return cls(
            ApplicationReadable=json_data.get("ApplicationReadable"),
            Expiration=json_data.get("Expiration"),
            HttpHeaders=json_data.get("HttpHeaders"),
            MimeType=json_data.get("MimeType"),
            Path=json_data.get("Path"),
            RequireMatchingFile=json_data.get("RequireMatchingFile"),
            UploadPathRegex=json_data.get("UploadPathRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticFiles = StaticFiles


@dataclass
class HttpHeaders:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaders"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaders = HttpHeaders


@dataclass
class Libraries:
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Libraries"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Libraries"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Libraries = Libraries


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


