# TF::Panos::DataFilteringSecurityProfile RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertthreshold" title="AlertThreshold">AlertThreshold</a>" : <i>Double</i>,
    "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
    "<a href="#blockthreshold" title="BlockThreshold">BlockThreshold</a>" : <i>Double</i>,
    "<a href="#datapattern" title="DataPattern">DataPattern</a>" : <i>String</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#filetypes" title="FileTypes">FileTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#logseverity" title="LogSeverity">LogSeverity</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#alertthreshold" title="AlertThreshold">AlertThreshold</a>: <i>Double</i>
<a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
<a href="#blockthreshold" title="BlockThreshold">BlockThreshold</a>: <i>Double</i>
<a href="#datapattern" title="DataPattern">DataPattern</a>: <i>String</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#filetypes" title="FileTypes">FileTypes</a>: <i>
      - String</i>
<a href="#logseverity" title="LogSeverity">LogSeverity</a>: <i>String</i>
</pre>

## Properties

#### AlertThreshold

Alert threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

List of applications.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockThreshold

Block threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataPattern

The data pattern name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

Direction.  Valid values are `both` (default),
`download`, or `upload`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTypes

List of file types.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSeverity

Log severity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

