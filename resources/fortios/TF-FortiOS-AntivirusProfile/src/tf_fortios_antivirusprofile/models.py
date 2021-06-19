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
    AnalyticsAcceptFiletype: Optional[float]
    AnalyticsBlFiletype: Optional[float]
    AnalyticsDb: Optional[str]
    AnalyticsIgnoreFiletype: Optional[float]
    AnalyticsMaxUpload: Optional[float]
    AnalyticsWlFiletype: Optional[float]
    AvBlockLog: Optional[str]
    AvVirusLog: Optional[str]
    Comment: Optional[str]
    ExtendedLog: Optional[str]
    FeatureSet: Optional[str]
    FtgdAnalytics: Optional[str]
    Id: Optional[str]
    InspectionMode: Optional[str]
    MobileMalwareDb: Optional[str]
    Name: Optional[str]
    ReplacemsgGroup: Optional[str]
    ScanMode: Optional[str]
    Vdomparam: Optional[str]
    Cifs: Optional[Sequence["_CifsDefinition"]]
    ContentDisarm: Optional[Sequence["_ContentDisarmDefinition"]]
    Ftp: Optional[Sequence["_FtpDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Imap: Optional[Sequence["_ImapDefinition"]]
    Mapi: Optional[Sequence["_MapiDefinition"]]
    NacQuar: Optional[Sequence["_NacQuarDefinition"]]
    Nntp: Optional[Sequence["_NntpDefinition"]]
    OutbreakPrevention: Optional[Sequence["_OutbreakPreventionDefinition"]]
    Pop3: Optional[Sequence["_Pop3Definition"]]
    Smb: Optional[Sequence["_SmbDefinition"]]
    Smtp: Optional[Sequence["_SmtpDefinition"]]
    Ssh: Optional[Sequence["_SshDefinition"]]

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
            AnalyticsAcceptFiletype=json_data.get("AnalyticsAcceptFiletype"),
            AnalyticsBlFiletype=json_data.get("AnalyticsBlFiletype"),
            AnalyticsDb=json_data.get("AnalyticsDb"),
            AnalyticsIgnoreFiletype=json_data.get("AnalyticsIgnoreFiletype"),
            AnalyticsMaxUpload=json_data.get("AnalyticsMaxUpload"),
            AnalyticsWlFiletype=json_data.get("AnalyticsWlFiletype"),
            AvBlockLog=json_data.get("AvBlockLog"),
            AvVirusLog=json_data.get("AvVirusLog"),
            Comment=json_data.get("Comment"),
            ExtendedLog=json_data.get("ExtendedLog"),
            FeatureSet=json_data.get("FeatureSet"),
            FtgdAnalytics=json_data.get("FtgdAnalytics"),
            Id=json_data.get("Id"),
            InspectionMode=json_data.get("InspectionMode"),
            MobileMalwareDb=json_data.get("MobileMalwareDb"),
            Name=json_data.get("Name"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            ScanMode=json_data.get("ScanMode"),
            Vdomparam=json_data.get("Vdomparam"),
            Cifs=deserialize_list(json_data.get("Cifs"), CifsDefinition),
            ContentDisarm=deserialize_list(json_data.get("ContentDisarm"), ContentDisarmDefinition),
            Ftp=deserialize_list(json_data.get("Ftp"), FtpDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Imap=deserialize_list(json_data.get("Imap"), ImapDefinition),
            Mapi=deserialize_list(json_data.get("Mapi"), MapiDefinition),
            NacQuar=deserialize_list(json_data.get("NacQuar"), NacQuarDefinition),
            Nntp=deserialize_list(json_data.get("Nntp"), NntpDefinition),
            OutbreakPrevention=deserialize_list(json_data.get("OutbreakPrevention"), OutbreakPreventionDefinition),
            Pop3=deserialize_list(json_data.get("Pop3"), Pop3Definition),
            Smb=deserialize_list(json_data.get("Smb"), SmbDefinition),
            Smtp=deserialize_list(json_data.get("Smtp"), SmtpDefinition),
            Ssh=deserialize_list(json_data.get("Ssh"), SshDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CifsDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    Emulator: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CifsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CifsDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            Emulator=json_data.get("Emulator"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CifsDefinition = CifsDefinition


@dataclass
class ContentDisarmDefinition(BaseModel):
    CoverPage: Optional[str]
    DetectOnly: Optional[str]
    ErrorAction: Optional[str]
    OfficeAction: Optional[str]
    OfficeDde: Optional[str]
    OfficeEmbed: Optional[str]
    OfficeHylink: Optional[str]
    OfficeLinked: Optional[str]
    OfficeMacro: Optional[str]
    OriginalFileDestination: Optional[str]
    PdfActForm: Optional[str]
    PdfActGotor: Optional[str]
    PdfActJava: Optional[str]
    PdfActLaunch: Optional[str]
    PdfActMovie: Optional[str]
    PdfActSound: Optional[str]
    PdfEmbedfile: Optional[str]
    PdfHyperlink: Optional[str]
    PdfJavacode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentDisarmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentDisarmDefinition"]:
        if not json_data:
            return None
        return cls(
            CoverPage=json_data.get("CoverPage"),
            DetectOnly=json_data.get("DetectOnly"),
            ErrorAction=json_data.get("ErrorAction"),
            OfficeAction=json_data.get("OfficeAction"),
            OfficeDde=json_data.get("OfficeDde"),
            OfficeEmbed=json_data.get("OfficeEmbed"),
            OfficeHylink=json_data.get("OfficeHylink"),
            OfficeLinked=json_data.get("OfficeLinked"),
            OfficeMacro=json_data.get("OfficeMacro"),
            OriginalFileDestination=json_data.get("OriginalFileDestination"),
            PdfActForm=json_data.get("PdfActForm"),
            PdfActGotor=json_data.get("PdfActGotor"),
            PdfActJava=json_data.get("PdfActJava"),
            PdfActLaunch=json_data.get("PdfActLaunch"),
            PdfActMovie=json_data.get("PdfActMovie"),
            PdfActSound=json_data.get("PdfActSound"),
            PdfEmbedfile=json_data.get("PdfEmbedfile"),
            PdfHyperlink=json_data.get("PdfHyperlink"),
            PdfJavacode=json_data.get("PdfJavacode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentDisarmDefinition = ContentDisarmDefinition


@dataclass
class FtpDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    Emulator: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtpDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            Emulator=json_data.get("Emulator"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtpDefinition = FtpDefinition


@dataclass
class HttpDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    ContentDisarm: Optional[str]
    Emulator: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            ContentDisarm=json_data.get("ContentDisarm"),
            Emulator=json_data.get("Emulator"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class ImapDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    ContentDisarm: Optional[str]
    Emulator: Optional[str]
    Executables: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImapDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            ContentDisarm=json_data.get("ContentDisarm"),
            Emulator=json_data.get("Emulator"),
            Executables=json_data.get("Executables"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImapDefinition = ImapDefinition


@dataclass
class MapiDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    Emulator: Optional[str]
    Executables: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapiDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            Emulator=json_data.get("Emulator"),
            Executables=json_data.get("Executables"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapiDefinition = MapiDefinition


@dataclass
class NacQuarDefinition(BaseModel):
    Expiry: Optional[str]
    Infected: Optional[str]
    Log: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NacQuarDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NacQuarDefinition"]:
        if not json_data:
            return None
        return cls(
            Expiry=json_data.get("Expiry"),
            Infected=json_data.get("Infected"),
            Log=json_data.get("Log"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NacQuarDefinition = NacQuarDefinition


@dataclass
class NntpDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    Emulator: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NntpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NntpDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            Emulator=json_data.get("Emulator"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NntpDefinition = NntpDefinition


@dataclass
class OutbreakPreventionDefinition(BaseModel):
    ExternalBlocklist: Optional[str]
    FtgdService: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutbreakPreventionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutbreakPreventionDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalBlocklist=json_data.get("ExternalBlocklist"),
            FtgdService=json_data.get("FtgdService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutbreakPreventionDefinition = OutbreakPreventionDefinition


@dataclass
class Pop3Definition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    ContentDisarm: Optional[str]
    Emulator: Optional[str]
    Executables: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Pop3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pop3Definition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            ContentDisarm=json_data.get("ContentDisarm"),
            Emulator=json_data.get("Emulator"),
            Executables=json_data.get("Executables"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pop3Definition = Pop3Definition


@dataclass
class SmbDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    Emulator: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmbDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            Emulator=json_data.get("Emulator"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmbDefinition = SmbDefinition


@dataclass
class SmtpDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    ContentDisarm: Optional[str]
    Emulator: Optional[str]
    Executables: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            ContentDisarm=json_data.get("ContentDisarm"),
            Emulator=json_data.get("Emulator"),
            Executables=json_data.get("Executables"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpDefinition = SmtpDefinition


@dataclass
class SshDefinition(BaseModel):
    ArchiveBlock: Optional[str]
    ArchiveLog: Optional[str]
    Emulator: Optional[str]
    Options: Optional[str]
    OutbreakPrevention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshDefinition"]:
        if not json_data:
            return None
        return cls(
            ArchiveBlock=json_data.get("ArchiveBlock"),
            ArchiveLog=json_data.get("ArchiveLog"),
            Emulator=json_data.get("Emulator"),
            Options=json_data.get("Options"),
            OutbreakPrevention=json_data.get("OutbreakPrevention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshDefinition = SshDefinition


