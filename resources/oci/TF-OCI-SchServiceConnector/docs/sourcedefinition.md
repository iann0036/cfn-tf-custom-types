# TF::OCI::SchServiceConnector SourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
    "<a href="#streamid" title="StreamId">StreamId</a>" : <i>String</i>,
    "<a href="#cursor" title="Cursor">Cursor</a>" : <i>[ <a href="cursordefinition.md">CursorDefinition</a>, ... ]</i>,
    "<a href="#logsources" title="LogSources">LogSources</a>" : <i>[ <a href="logsourcesdefinition.md">LogSourcesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#kind" title="Kind">Kind</a>: <i>String</i>
<a href="#streamid" title="StreamId">StreamId</a>: <i>String</i>
<a href="#cursor" title="Cursor">Cursor</a>: <i>
      - <a href="cursordefinition.md">CursorDefinition</a></i>
<a href="#logsources" title="LogSources">LogSources</a>: <i>
      - <a href="logsourcesdefinition.md">LogSourcesDefinition</a></i>
</pre>

## Properties

#### Kind

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cursor

_Required_: No

_Type_: List of <a href="cursordefinition.md">CursorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSources

_Required_: No

_Type_: List of <a href="logsourcesdefinition.md">LogSourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

