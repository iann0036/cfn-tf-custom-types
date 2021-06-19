# TF::FortiOS::SshfilterProfile FileFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#scanarchivecontents" title="ScanArchiveContents">ScanArchiveContents</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#entries" title="Entries">Entries</a>" : <i>[ <a href="entriesdefinition.md">EntriesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#scanarchivecontents" title="ScanArchiveContents">ScanArchiveContents</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#entries" title="Entries">Entries</a>: <i>
      - <a href="entriesdefinition.md">EntriesDefinition</a></i>
</pre>

## Properties

#### Log

Enable/disable file filter logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanArchiveContents

Enable/disable file filter archive contents scan. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable file filter. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entries

_Required_: No

_Type_: List of <a href="entriesdefinition.md">EntriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

