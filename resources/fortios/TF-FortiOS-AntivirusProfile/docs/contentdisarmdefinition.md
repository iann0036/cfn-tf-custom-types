# TF::FortiOS::AntivirusProfile ContentDisarmDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#coverpage" title="CoverPage">CoverPage</a>" : <i>String</i>,
    "<a href="#detectonly" title="DetectOnly">DetectOnly</a>" : <i>String</i>,
    "<a href="#erroraction" title="ErrorAction">ErrorAction</a>" : <i>String</i>,
    "<a href="#officeaction" title="OfficeAction">OfficeAction</a>" : <i>String</i>,
    "<a href="#officedde" title="OfficeDde">OfficeDde</a>" : <i>String</i>,
    "<a href="#officeembed" title="OfficeEmbed">OfficeEmbed</a>" : <i>String</i>,
    "<a href="#officehylink" title="OfficeHylink">OfficeHylink</a>" : <i>String</i>,
    "<a href="#officelinked" title="OfficeLinked">OfficeLinked</a>" : <i>String</i>,
    "<a href="#officemacro" title="OfficeMacro">OfficeMacro</a>" : <i>String</i>,
    "<a href="#originalfiledestination" title="OriginalFileDestination">OriginalFileDestination</a>" : <i>String</i>,
    "<a href="#pdfactform" title="PdfActForm">PdfActForm</a>" : <i>String</i>,
    "<a href="#pdfactgotor" title="PdfActGotor">PdfActGotor</a>" : <i>String</i>,
    "<a href="#pdfactjava" title="PdfActJava">PdfActJava</a>" : <i>String</i>,
    "<a href="#pdfactlaunch" title="PdfActLaunch">PdfActLaunch</a>" : <i>String</i>,
    "<a href="#pdfactmovie" title="PdfActMovie">PdfActMovie</a>" : <i>String</i>,
    "<a href="#pdfactsound" title="PdfActSound">PdfActSound</a>" : <i>String</i>,
    "<a href="#pdfembedfile" title="PdfEmbedfile">PdfEmbedfile</a>" : <i>String</i>,
    "<a href="#pdfhyperlink" title="PdfHyperlink">PdfHyperlink</a>" : <i>String</i>,
    "<a href="#pdfjavacode" title="PdfJavacode">PdfJavacode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#coverpage" title="CoverPage">CoverPage</a>: <i>String</i>
<a href="#detectonly" title="DetectOnly">DetectOnly</a>: <i>String</i>
<a href="#erroraction" title="ErrorAction">ErrorAction</a>: <i>String</i>
<a href="#officeaction" title="OfficeAction">OfficeAction</a>: <i>String</i>
<a href="#officedde" title="OfficeDde">OfficeDde</a>: <i>String</i>
<a href="#officeembed" title="OfficeEmbed">OfficeEmbed</a>: <i>String</i>
<a href="#officehylink" title="OfficeHylink">OfficeHylink</a>: <i>String</i>
<a href="#officelinked" title="OfficeLinked">OfficeLinked</a>: <i>String</i>
<a href="#officemacro" title="OfficeMacro">OfficeMacro</a>: <i>String</i>
<a href="#originalfiledestination" title="OriginalFileDestination">OriginalFileDestination</a>: <i>String</i>
<a href="#pdfactform" title="PdfActForm">PdfActForm</a>: <i>String</i>
<a href="#pdfactgotor" title="PdfActGotor">PdfActGotor</a>: <i>String</i>
<a href="#pdfactjava" title="PdfActJava">PdfActJava</a>: <i>String</i>
<a href="#pdfactlaunch" title="PdfActLaunch">PdfActLaunch</a>: <i>String</i>
<a href="#pdfactmovie" title="PdfActMovie">PdfActMovie</a>: <i>String</i>
<a href="#pdfactsound" title="PdfActSound">PdfActSound</a>: <i>String</i>
<a href="#pdfembedfile" title="PdfEmbedfile">PdfEmbedfile</a>: <i>String</i>
<a href="#pdfhyperlink" title="PdfHyperlink">PdfHyperlink</a>: <i>String</i>
<a href="#pdfjavacode" title="PdfJavacode">PdfJavacode</a>: <i>String</i>
</pre>

## Properties

#### CoverPage

Enable/disable inserting a cover page into the disarmed document. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectOnly

Enable/disable only detect disarmable files, do not alter content. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorAction

Action to be taken if CDR engine encounters an unrecoverable error. Valid values: `block`, `log-only`, `ignore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficeAction

Enable/disable stripping of PowerPoint action events in Microsoft Office documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficeDde

Enable/disable stripping of Dynamic Data Exchange events in Microsoft Office documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficeEmbed

Enable/disable stripping of embedded objects in Microsoft Office documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficeHylink

Enable/disable stripping of hyperlinks in Microsoft Office documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficeLinked

Enable/disable stripping of linked objects in Microsoft Office documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficeMacro

Enable/disable stripping of macros in Microsoft Office documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalFileDestination

Destination to send original file if active content is removed. Valid values: `fortisandbox`, `quarantine`, `discard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfActForm

Enable/disable stripping of actions that submit data to other targets in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfActGotor

Enable/disable stripping of links to other PDFs in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfActJava

Enable/disable stripping of actions that execute JavaScript code in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfActLaunch

Enable/disable stripping of links to external applications in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfActMovie

Enable/disable stripping of embedded movies in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfActSound

Enable/disable stripping of embedded sound files in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfEmbedfile

Enable/disable stripping of embedded files in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfHyperlink

Enable/disable stripping of hyperlinks from PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdfJavacode

Enable/disable stripping of JavaScript code in PDF documents. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

