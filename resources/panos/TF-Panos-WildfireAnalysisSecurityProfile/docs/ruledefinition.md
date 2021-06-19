# TF::Panos::WildfireAnalysisSecurityProfile RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#analysis" title="Analysis">Analysis</a>" : <i>String</i>,
    "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#filetypes" title="FileTypes">FileTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#analysis" title="Analysis">Analysis</a>: <i>String</i>
<a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#filetypes" title="FileTypes">FileTypes</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Analysis

Analysis setting.  Valid values are `public-cloud` (default)
or `private-cloud`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

List of applications.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

Direction.  Valid values are `both` (default),
`upload`, or `download`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTypes

List of file types.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

