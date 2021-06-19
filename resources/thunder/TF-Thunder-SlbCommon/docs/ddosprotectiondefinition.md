# TF::Thunder::SlbCommon DdosProtectionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipdenabletoggle" title="IpdEnableToggle">IpdEnableToggle</a>" : <i>String</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="loggingdefinition.md">LoggingDefinition</a>, ... ]</i>,
    "<a href="#packetspersecond" title="PacketsPerSecond">PacketsPerSecond</a>" : <i>[ <a href="packetsperseconddefinition.md">PacketsPerSecondDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipdenabletoggle" title="IpdEnableToggle">IpdEnableToggle</a>: <i>String</i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="loggingdefinition.md">LoggingDefinition</a></i>
<a href="#packetspersecond" title="PacketsPerSecond">PacketsPerSecond</a>: <i>
      - <a href="packetsperseconddefinition.md">PacketsPerSecondDefinition</a></i>
</pre>

## Properties

#### IpdEnableToggle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="loggingdefinition.md">LoggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketsPerSecond

_Required_: No

_Type_: List of <a href="packetsperseconddefinition.md">PacketsPerSecondDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

