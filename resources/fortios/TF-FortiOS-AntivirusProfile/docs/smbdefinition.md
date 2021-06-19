# TF::FortiOS::AntivirusProfile SmbDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#archiveblock" title="ArchiveBlock">ArchiveBlock</a>" : <i>String</i>,
    "<a href="#archivelog" title="ArchiveLog">ArchiveLog</a>" : <i>String</i>,
    "<a href="#emulator" title="Emulator">Emulator</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#outbreakprevention" title="OutbreakPrevention">OutbreakPrevention</a>" : <i>[ <a href="outbreakpreventiondefinition.md">OutbreakPreventionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#archiveblock" title="ArchiveBlock">ArchiveBlock</a>: <i>String</i>
<a href="#archivelog" title="ArchiveLog">ArchiveLog</a>: <i>String</i>
<a href="#emulator" title="Emulator">Emulator</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#outbreakprevention" title="OutbreakPrevention">OutbreakPrevention</a>: <i>
      - <a href="outbreakpreventiondefinition.md">OutbreakPreventionDefinition</a></i>
</pre>

## Properties

#### ArchiveBlock

Select the archive types to block. Valid values: `encrypted`, `corrupted`, `partiallycorrupted`, `multipart`, `nested`, `mailbomb`, `fileslimit`, `timeout`, `unhandled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArchiveLog

Select the archive types to log. Valid values: `encrypted`, `corrupted`, `partiallycorrupted`, `multipart`, `nested`, `mailbomb`, `fileslimit`, `timeout`, `unhandled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Emulator

Enable/disable the virus emulator. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Enable/disable SMB AntiVirus scanning, monitoring, and quarantine. Valid values: `scan`, `avmonitor`, `quarantine`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPrevention

_Required_: No

_Type_: List of <a href="outbreakpreventiondefinition.md">OutbreakPreventionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

